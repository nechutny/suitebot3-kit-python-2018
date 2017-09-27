import threading
import unittest
import socket

import time

from suitebot3.server.simple_request_handler import SimpleRequestHandler
from suitebot3.server.simple_server import SimpleServer, SHUTDOWN_REQUEST

PORT = 4444

class TestSimpleServer(unittest.TestCase):

    def setUp(self):
        self.server = SimpleServer(PORT, ToLowerCaseRequestHandler())
        self.server_thread = threading.Thread(target=lambda: self.server.run())
        self.server_thread.start()

        super().setUp()

    def tearDown(self):
        if self.server_thread.is_alive():
            send_request(SHUTDOWN_REQUEST)

        self.server_thread.join(100)
        super().tearDown()

    def test_shutting_down(self):
        self.assertTrue(self.server_thread.is_alive())

        send_request(SHUTDOWN_REQUEST)
        time.sleep(0.1)

        self.assertFalse(self.server_thread.is_alive())

def send_request(request: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', PORT))

    bytes = bytearray(request, 'UTF-8')
    totalsent = 0
    while totalsent < len(bytes):
        sent = sock.send(bytes[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

    sock.close()

class ToLowerCaseRequestHandler(SimpleRequestHandler):
    def process_request(self, request: str) -> str:
        return str.lower(str)
