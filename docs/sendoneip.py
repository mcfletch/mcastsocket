from __future__ import print_function
from mcastsocket import mcastsocket
import select, time, sys


def main():
    # bind/listen on all interfaces, send with a TTL of 5
    group, port = '224.1.1.2', 8053
    interface = sys.argv[1]
    sock = mcastsocket.create_socket(
        ('', port),
        TTL=5,
        loop=True,
    )
    mcastsocket.join_group(
        sock,
        group=group,
        iface=interface,
    )
    try:
        print('Sending traffic on %s:%s %s'%(group,port,interface))
        while True:
            _, writable, _= select.select([], [sock], [], .5)
            if writable:
                sock.sendto(b'message', (group, port))
                time.sleep(.5)
    finally:
        mcastsocket.leave_group(
            sock,
            group=group,
            iface=interface,
        )

if __name__ == "__main__":
    main()
