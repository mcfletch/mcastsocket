#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mcastsocket
----------------------------------

Tests for `mcastsocket` module.
"""

import unittest
import netifaces
from mcastsocket import mcastsocket


class TestMcastsocket(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_socket_v2(self):
        sock = mcastsocket.create_socket(
            ('127.0.0.1',8000),
        )
        mcastsocket.join_group(
            sock,
            group = '224.1.1.2',
            iface = '127.0.0.1',
        )
        mcastsocket.leave_group(
            sock,
            group = '224.1.1.2',
            iface = '127.0.0.1',
        )
    

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
