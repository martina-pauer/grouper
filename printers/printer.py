class Obj3DPrinters:
    
    def __init__(self):
        '''
            Represent Each 3D printer
            of the network, data and operations.
        '''
        self.ID: str = '3DPrinter Default Name'
        # Some Commons are PLA, PETG and TPU Between Others Compatibles
        self.material: str = 'PETG'
        # Use One Hex Color Code Or Hex 2 To 4 Color Codes With AMS Lite
        self.colors: str = '#bf3333,#11ff21,#1122df,#7f7f81'
        # How Much Pieces Print
        self.copies: int = 1
        # List For contain Connectors objects for more flexibility and abstraction from them
        self.connectors: list = ['network.py', 'sender.py']
        
    def set_ID(self, value: str):
        '''
            Change 3D Printer Default name
            for be more unique and customized
            with the function to reach.
        '''
        self.ID = value

    def SETUP(self, copies: int, material: str, color: str):
        '''
            Make Settings and load to 3D Printer
            connected to WI-FI using connector code.
            
            Use 3 Printing Parameters: copies, plastic kind & Hex color CSV.
        '''
        self.copies = copies

        self.material = material

        self.colors = color
        # Use Object Created in main script To send data
        self.connectors[1].set_printer(self.connectors[0].get_printer_IP(self.get_ID())) 
        self.connectors[1].send (
                                    [
                                        self.copies, self.material,
                                        self.colors
                                    ]
                                )

    def get_ID(self) -> str:
        '''
            Give The 3D Printer Customized
            name.
        '''
        self.ID

    def is_printing(self) -> bool:
        '''
            Use Connectors Code for Check 
            if the printer continue printing 
            the piece.
        '''
        return self.connectors[1].get_printing()

    def fails(self) -> list[str]:
        '''
            Use Connector Code for get
            logs from the printer in a list
            with text values for use later 
            in easy to read web output.
        '''
        mistakes: list[str] = []
        # Read Logs and copy in readble way to mistakes list
        # Give mistakes getted
        return mistakes

    def turn_ON(self):
        '''
            Use Connector Code for
            Power On Printer.
        '''
        if not self.is_printing():
            pass

    def turn_OFF(self):
        '''
            Use Connector Code
            for Power Off the printer.
        '''
        pass

    def load_model(self, file_3D_handler):
        '''
            Use Conector Code For Send 
            The File To the Printer.
        '''
        pass

    def print(self):
        '''
            Use Connector Code For Print
            the loadel 3D Model.

            Use PrinterSender Object
        '''
        CONTINUE_PRINTING_BYTE = b'1'
        # Make Progressive Printing One Step At time
        while (self.is_printing() and self.fails().__len__() < 3):
            # Until 3 Common fails Could still printing
            self.connectors[1].load_bytes(CONTINUE_PRINTING_BYTE)

    def add_connectors(self, net, sending):
        '''
            Save at internal list the WI-FI connectors
            interface.
        '''
        self.connectors[0] = net
        self.connectors[1] = sending

class Status3DPrinters:
    
    def __init__(self):
        '''
            Make A Group Of Connected 3D
            Printers For Automatitation
            Coerence.
        '''
        self.printers_group: list[Obj3DPrinters] = []

    def get_printers(self) -> list[Obj3DPrinters]:
        '''
            Get All Printers In The Group
            From External Source.
        '''
        return self.printers_group

    def get_printer(self, ID: str) -> Obj3DPrinters:
        '''
            Search By ID and Return Printer
            That Have It.
        '''
        for searching in self.printers_group:
            if searching.get_ID() == ID:
                return searching
                break

    def add_printer(self, printer: Obj3DPrinters):
        '''
            Join New Printers To The Automatitation Group.
        '''
        self.printers_group.append(printer)

    def load_model(self, ID, file_handler):
        '''
            Load A 3D Model In Selected By ID Printer.
        '''
        self.get_printer(ID).load_model(file_handler)

    def turn_ON_all(self):
        '''
            Build All The Blocks In Short Time.
        '''
        for turning in self.get_printers():
            turning.turn_ON()

    def turn_OFF_all(self):
        '''
            Close The Factory Turning OFF
            All The Printers.
        '''
        for power in self.get_printers():
            power.turn_OFF()

    def print_all(self):
        '''
            Iterates Over All The Printers
            For Safe Up That All are Printing
            Each One His Piece.
        '''
        for printer in self.get_printers():
            printer.print()