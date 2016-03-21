"""
Author: Ken Lambert
File: doctorclientgui.py
Project 11

GUI-based client for non-directive psychotherapy.
"""

from socket import *
from codecs import decode
from time import ctime
from breezypythongui import EasyFrame

class DoctorClientGUI(EasyFrame):
    """Represents the client and its window."""

    BUFSIZE = 1024
    COLOR = "#FFCCCC"
    CODE = "ascii"

    def __init__(self):
        """Initialize the frame."""
        self.server = None
        EasyFrame.__init__(self, title = "Doctor Client",
                           background = DoctorClientGUI.COLOR)
        self.hostLabel = self.addLabel(row = 0, column = 0,
                                       text = "Host name")
        self.nameLabel = self.addLabel(row = 1, column = 0,
                                       text = "Patient first name")
        self.doctorOutputLabel = self.addLabel(row = 2, column = 0,
                                               text = "Doctor")
        self.patientInputLabel = self.addLabel(row = 3, column = 0,
                                               text = "Patient")
        self.hostField = self.addTextField(row = 0, column = 1,
                                           text = "localhost")
        self.nameField = self.addTextField(row = 1, column = 1,
                                           text = "")
        self.doctorOutputField = self.addTextField(row = 2, column = 1,
                                                   text = "", width = 50,
                                                   state = "readonly")
        self.patientInputField = self.addTextField(row = 3, column = 1,
                                                   text = "", width = 50)
        self.startButton = self.addButton(row = 4, column = 0,
                                          text = "Connect",
                                          command = self.startClient)
        self.sendButton = self.addButton(row = 4, column = 1,
                                         text = "Send reply",
                                         state = "disabled",
                                         command = self.converse)
        self.hostLabel["background"] = DoctorClientGUI.COLOR
        self.nameLabel["background"] = DoctorClientGUI.COLOR
        self.patientInputLabel["background"] = DoctorClientGUI.COLOR
        self.doctorOutputLabel["background"] = DoctorClientGUI.COLOR


    def startClient(self):
        """Starts up the client."""
        self.doctorOutputField.setText("")
        name = self.nameField.getText()
        if name == "":
            self.messageBox(title = "Error",
                            message = "Please enter your first name!")
            return
        try:
            # Connect to the host aend patient name to server
            host = self.hostField.getText()
            port = 50000
            address = (host, port)
            self.server = socket(AF_INET, SOCK_STREAM)
            self.server.connect(address)                         
            self.server.send(bytes(name, DoctorClientGUI.CODE))  
            self.sendButton["state"] = "normal"
            self.startButton["state"] = "disabled"
            doctorReply = decode(self.server.recv(DoctorClientGUI.BUFSIZE),
                                 DoctorClientGUI.CODE)
            if not doctorReply:
                self.doctorOutputField.setText("Doctor disconnecting.")
                self.cleanUp()
            else:
                self.doctorOutputField.setText(doctorReply)
        except Exception as message:
            self.doctorOutputField.setText(str(message))
            self.cleanUp()

    def converse(self):
        """Sends the client's reply and receives the server's reply.
        The client sends an empty reply to quit."""
        try:
            patientReply = self.patientInputField.getText()
            if not patientReply:
                self.doctorOutputField.setText("Patient disconnecting.")
                self.cleanUp()
            else:
                self.server.send(bytes(patientReply,
                                       DoctorClientGUI.CODE))
                doctorReply = decode(self.server.recv(DoctorClientGUI.BUFSIZE),
                                     DoctorClientGUI.CODE)
                if not doctorReply:
                    self.doctorOutputField.setText("Doctor disconnecting.")
                    self.cleanUp()
                else:
                    self.doctorOutputField.setText(doctorReply)
                    self.patientInputField.setText("")
        except Exception as message:
            self.doctorOutputField.setText(str(message))
            self.cleanUp()

    def cleanUp(self):
        """Closes server socket if it exists, and resets states of the widgets."""
        if self.server:
            self.server.close()
            self.sendButton["state"] = "disabled"
            self.startButton["state"] = "normal"
            self.nameField.setText("")
            self.patientInputField.setText("")
                                               
def main():
    """Opens a window on a client and waits connect to server."""
    theGUI = DoctorClientGUI()
    theGUI.mainloop()

if __name__ == "__main__":
    main()


