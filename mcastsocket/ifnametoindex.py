"""Python 2.x implementation of name-to-index lookup

In IPv6 we can't specify the IP address of the interface
in order to use that for limiting, instead we have to specify
the interface index, which is available in Python 3, but not
in Python 2. This module is a small shim to provide the function
missing.
"""
import ctypes, ctypes.util, errno
try:
    unicode
except NameError:
    unicode = str

LIBC = None
def get_libc():
    """Load the libc library and cache reference to it"""
    global LIBC
    if LIBC is None:
        LIBC = ctypes.CDLL(
            ctypes.util.find_library('c')
        )
    return LIBC

def if_nametoindex(name):
    """Resolve an interface name into an interface index (integer)"""
    if isinstance(name,unicode):
        name=name.encode('utf-8')
    elif not isinstance(name,bytes):
        raise TypeError("Require unicode/bytes type for name")
    index = get_libc().if_nametoindex(name)
    if index == 0:
        error = ctypes.get_errno()
        try:
            message = os.strerror(error)
        except ValueError:
            message = 'if_nametoindex returned %s'%(error,)
        raise IOError(message, error, name)
    return index
