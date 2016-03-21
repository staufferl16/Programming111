"""
Author: Ken Lambert
Edited By: Leigh Stauffer
File: doctorservergui.py
Project 11

GUI-based server for multiclient non-directive psychotherapy.
"""

from doctorserver import DoctorServer
from breezypythongui import EasyFrame
from socket import gethostname

class DoctorServerGUI(EasyFrame):
    """Represents the server's window."""

    COLOR = "#CCEEFF"
    CODE = "ascii"

    def __init__(self):
        """Initialize the frame and widgets."""
        EasyFrame.__init__(self, title = "Doctor Server",
                           background = DoctorServerGUI.COLOR)
        self.hostLabel = self.addLabel(row = 0, column = 0,
                                       text = "Host name")
        self.hostField = self.addTextField(row = 0, column = 1,
                                           text = gethostname())
        self.startButton = self.addButton(row = 1, column = 0,
                                          columnspan = 3,
                                          text = "Start server",
                                          command = self.startServer)
        self.statusArea = self.addTextField(row = 2, column = 0,
                                           columnspan = 3,
                                           text = "")
        self.hostLabel["background"] = DoctorServerGUI.COLOR


    def updateStatus(self, message):
        """Updates the status area with text."""
        self.statusArea.setText(message + "\n")                                         

    def startServer(self):
        """Starts up the server with the host, port, and view."""
        self.startButton["state"] = "disabled"
        host = self.hostField.getText()
        port = 50000
        self.server = DoctorServer(host, port, self)
        self.server.start()

def main():
    """Opens a window on a server and waits to start up."""
    theGUI = DoctorServerGUI()
    theGUI.mainloop()

if __name__ == "__main__":
    main()



