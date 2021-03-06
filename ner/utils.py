#!/usr/bin/env python

import httplib
import socket

from contextlib import contextmanager


@contextmanager
def tcpip4_socket(host, port):
    """Open a TCP/IP4 socket to designated host/port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        yield s
    finally:
        s.shutdown(socket.SHUT_RDWR)
        s.close()

@contextmanager
def http_connection(host, port):
    """Open an HTTP connection to designated host/port."""
    c = httplib.HTTPConnection(host, port)
    try:
       yield c
    finally:
       c.close()


