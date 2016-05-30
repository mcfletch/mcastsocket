from __future__ import print_function
from mcastsocket import mcastsocket
import select, sys


def main():
    # bind/listen on all interfaces, send with a TTL of 5
    group, port = '224.1.1.2', 8053
    interface = sys.argv[1]
    sock = mcastsocket.create_socket(
        ('', port),
        TTL=5,
    )
    mcastsocket.join_group(
        sock,
        group=group,
        iface = interface,
    )
    try:
        print('Listening for traffic on %s:%s on ip %s'%(group,port,interface))
        while True:
            readable, _, _ = select.select([sock], [], [], .5)
            if readable:
                message, address = sock.recvfrom(65000)
                print('Received %r from %r' % (message, address))
    finally:
        mcastsocket.leave_group(
            sock,
            group=group,
            iface = interface,
        )

if __name__ == "__main__":
    main()
