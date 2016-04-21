from mcastsocket import mcastsocket
import select


def main():
    # bind/listen on all interfaces, send with a TTL of 5
    group,port = '224.1.1.2',8000
    sock = mcastsocket.create_socket(
        ('',port),
        TTL=5,
    )
    mcastsocket.join_group(
        sock,
        group = group,
    )
    sock.sendto( b'message', (group,port))
    readable,[],[] = select.select([sock],[],[],.5)
    assert readable 
    message, address = sock.recvfrom( 65000 )
    print( 'Received %r from %r'%( message, address ))
    mcastsocket.leave_group(
        sock,
        group = group 
    )

if __name__ == "__main__":
    main()
