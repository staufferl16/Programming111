"""
Author: Ken Lambert
File: doctorserver.py
Project 11

Server for a therapy session.  Handles multiple clients
concurrently.
"""

from socket import *
from threading import Thread
from codecs import decode
from doctor import Doctor

BUFSIZE = 1024
CODE = 'ascii'

class ClientHandler(Thread):
    """Represents a client handler for a therapy session."""
    
    def __init__(self, client, doctor, myView):
        Thread.__init__(self)
        self.client = client
        self.doctor = doctor
        self.myView = myView

    def run(self):
        self.client.send(bytes(self.doctor.greeting(), CODE))
        while True:
            message = decode(self.client.recv(BUFSIZE), CODE)
            if not message:
                self.doctor.saveHistory()
                self.myView.updateStatus('Patient disconnected')
                self.client.close()
                break
            else:
                self.client.send(bytes(self.doctor.reply(message), CODE))

class DoctorServer(Thread):
    """Represents a server to handle multiple clients."""

    def __init__(self, host, port, myView):
        """Sets the initial state of the server."""
        Thread.__init__(self)
        self.address = (host, port)
        self.myView = myView
        self.isRunning = True

    def run(self):
        """Opens the server's socket, waits for connections
        from clients, and serves them."""
        try:
            self.server = socket(AF_INET, SOCK_STREAM)
            self.server.bind(self.address)
            self.server.listen(5)           # Allows up to 5 waiting clients

            while True:
                self.myView.updateStatus('Waiting for connection ...')
                client, address = self.server.accept()
                patientName = decode(client.recv(BUFSIZE), CODE)
                self.myView.updateStatus('... connected from ' + \
                                         patientName + " at " + str(address))
                doctor = Doctor(patientName)
                handler = ClientHandler(client, doctor, self.myView)
                handler.start()

        except Exception as message:
            self.myView.updateStatus(message)
        self.server.close()
        self.myView.updateStatus("Server shutting down.")
