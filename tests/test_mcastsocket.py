#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mcastsocket
----------------------------------

Tests for `mcastsocket` module.
"""
import socket, select
import unittest
from mcastsocket import mcastsocket


class TestMcastsocket(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    def send_to_group(self,group,message):
        sock = mcastsocket.create_socket(('127.0.0.1',8000),TTL=5)
        mcastsocket.join_group(
            sock,
            group = group,
            iface = '127.0.0.1',
        )
        sock.sendto( message, (group,8000))
        _,writable,_ = select.select([],[sock],[],.5)
        sock.close()

    def test_create_socket_v2(self):
        sock = mcastsocket.create_socket(
            ('',8000),
            TTL=5,
        )
        group = '224.1.1.2'
        mcastsocket.join_group(
            sock,
            group = group,
        )
        self.send_to_group( group, b'moo' )
        
        readable,writable,_ = select.select([sock],[],[],.5)
        assert readable, 'Nothing received'
        (content,address) = sock.recvfrom(65000)
        assert content == b'moo', content 
        assert address == ('127.0.0.1',8000), address
        mcastsocket.leave_group(
            sock,
            group = group,
        )
        sock.close()

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
