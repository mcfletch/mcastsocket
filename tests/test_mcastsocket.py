#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mcastsocket
----------------------------------

Tests for `mcastsocket` module.
"""
import select
import socket
import unittest
from mcastsocket import mcastsocket


class TestMcastsocket(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def send_to_group(self, group, message, family=socket.AF_INET):
        addr = ('127.0.0.1',8001) if family == socket.AF_INET else ('::1',8001,0,0)
        sock = mcastsocket.create_socket(
            ('',8001) if family == socket.AF_INET else ('',8001,0,3),
            TTL=5,
            family=family
        )
        mcastsocket.join_group(
            sock,
            group=group,
            iface=addr[0],
        )
        sock.sendto(message, (group, 8000))
        _, writable, _ = select.select([], [sock], [], .5)
        sock.close()

    def test_create_socket_v2(self):
        group = '224.1.1.2'
        sock = mcastsocket.create_socket(
            ('', 8000),
            TTL=5,
        )
        mcastsocket.join_group(
            sock,
            group=group,
            iface='127.0.0.1',
        )
        self.send_to_group(group, b'moo')
        readable, writable, _ = select.select([sock], [], [], .5)
        assert readable, 'Nothing received'
        (content, address) = sock.recvfrom(65000)
        assert content == b'moo', content
        assert address == ('127.0.0.1', 8001), address
        mcastsocket.leave_group(
            sock,
            group=group,
            iface='127.0.0.1',
        )
        sock.close()

    def test_create_socket_v3(self):
        group = '224.1.1.2'
        sock = mcastsocket.create_socket(
            ('', 8000),
            TTL=5,
        )
        try:
            ssm = '198.51.100.23'
            mcastsocket.join_group(
                sock,
                group=group,
                iface='127.0.0.1',
                # If commented out, we get a failure,
                # if present, we filter... yay
                ssm=ssm,
            )
            try:
                self.send_to_group(group, b'moo')
                readable, writable, _ = select.select([sock], [], [], .5)
                if readable:
                    (content, address) = sock.recvfrom(65000)
                assert not readable, (
                    'Should not have received the message due to ssm filtering', address)
            finally:
                mcastsocket.leave_group(
                    sock,
                    group=group,
                    iface='127.0.0.1',
                    # If commented out, we get a failure,
                    # if present, we filter... yay
                    ssm=ssm,
                )
        finally:
            sock.close()

    def test_ipv6_basic(self):
        group = 'ff02::2'
        sock = mcastsocket.create_socket(
            ('', 8000,0,3),
            TTL=5,
            family=socket.AF_INET6,
        )
        assert sock.family == socket.AF_INET6, sock.family
        mcastsocket.join_group(
            sock,
            group=group,
            iface = '::1',
        )
        self.send_to_group(group, b'moo', family=socket.AF_INET6)
        readable, writable, _ = select.select([sock], [], [], .5)
        assert readable, 'Nothing received'
        (content, address) = sock.recvfrom(65000)
        assert content == b'moo', content
        assert address[1] == 8001, address
        mcastsocket.leave_group(
            sock,
            group=group,
        )
        sock.close()


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
