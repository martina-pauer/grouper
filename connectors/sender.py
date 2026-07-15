class PrinterSender:

    def __init__(self):
        '''
            Send Instructions To A Printer
            in the Printers Network.
        '''
        self.printer_ID: str = ''
        self.IP: str = 'x.x.x.x'
        
    def set_printer(self, ID: str):
        '''
            Select Printer from the group.
        '''
        self.printer_ID = ID

    def set_address(self, Address: str):
        '''
            Add IP addres asociated to the
            printer.
        '''
        self.IP = Address
        
    def send(self, copies: int, material: str, colors: str):
        '''
            Use WI-FI tools for say to the printer how much copies print,
            what material use and what colors (from 1 to 4 tex list) 
            going to use.
        '''
        pass
    
    def load_bytes(self):
        '''
            Use Socket for send bytes to the
            printer
        '''
        import socket
        # Create socket
        # Get printer IP and connect socket
        # Send bytes to the printer
        # Close socket connection for could be created again

    def get_printing(self) -> bool:
        '''
            Use WI-FI tools for
            check if the printer is printing.
        '''
        pass

    def get_fails(self) -> list[str]:
        '''
            Check connectivity, printing
            and material stock.
        '''
        fail: list[str] = []
        
        if not self.get_printing():
            fail.append('Not Printing')

        return fail