def loader(file_name: str, sock):
    '''
        Use MQTT protocol for communicate by socket with
        Bambu Lab printer sending JSON file with orders.
    '''
    content: str = ''
    # Join Lines in One Text In Order
    with open(f'/workspaces/grouper/connectors/MQTT/{file_name}', 'r') as part:
        for line in part.readlines():
            content += line
    # Send All joined For Prevent From mistakes        
    sock.send(bytes(content, 'utf-8'))
        

class PrinterSender:

    def __init__(self):
        '''
            Send Instructions To A Printer
            in the Printers Network.
        '''
        self.printer_ID: str = ''
        self.IP: str = 'x.x.x.x'
        self.order_number: int = 1
        
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
        PRINTING_BYTES = b'17'
        for copy in range(0, copies):
            if self.get_fails() < 3:
                self.load_bytes(PRINTING_BYTES)
                self.load_bytes(bytes(material, 'utf-8'))
                for color in colors.split(','):
                    # Use AMS lite Color System
                    self.load_bytes(bytes(color, 'utf-8'))
                if not self.get_printing():
                    break
    
    def load_bytes(self, load: bytes):
        '''
            Use Socket for send bytes to the
            printer.
        '''
        import socket
        # Create socket
        BYTE_LOADER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Get printer IP and connect socket with IoT port with MQTT (Message Queuing Telemetry Transport)
        BYTE_LOADER_SOCKET.connect((self.get_IP(), 8883))
        # Send bytes to the printer
        if (load == b'11'):
            loader('print-layer.json', BYTE_LOADER_SOCKET)
        elif (load == b'12'):
            loader('load-file.json', BYTE_LOADER_SOCKET)
        elif (load == b'13'):
            pass
        elif (load == b'14'):
            loader('shutdown.json', BYTE_LOADER_SOCKET)
        elif (load == b'16'):
            loader('verification.json', BYTE_LOADER_SOCKET)
        elif (load == b'17'):
            loader('settings.json', BYTE_LOADER_SOCKET)
            
        # Close socket connection for could be created again
        BYTE_LOADER_SOCKET.close()
        self.order_number += 1

    def get_printing(self) -> bool:
        '''
            Use WI-FI tools for
            check if the printer is printing.
        '''
        CHECK_BYTES = b'16'
        self.load_bytes(CHECK_BYTES)
        return True
    
    def get_fails(self) -> list[str]:
        '''
            Check connectivity, printing
            and material stock.
        '''
        import os
        fail: list[str] = []
        
        if not self.get_printing():
            fail.append('Not Printing')
        if os.system(f'ping -c1 {self.IP}') != 512:
            fail.append('Printer Without WI-FI')    
            del os
        if False:
            # No Material for make printer
            fail.append('Material Empty')    

        return fail

    def get_IP(self) -> str:
        '''
            Give The Printer IP address.
        '''
        return self.IP