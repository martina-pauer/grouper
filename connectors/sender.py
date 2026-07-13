class PrinterSender:

    def __init__(self):
        '''
            Send Instructions To A Printer
            in the Printers Network.
        '''
        self.printer_ID: str = ''
        
    def set_printer(self, ID: str):
        '''
            Select Printer from the group.
        '''
        self.printer_ID = ID

    def send(self, copies: int, material: str, colors: str):
        '''
            Use WI-FI tools for say to the printer how much copies print,
            what material use and what colors (from 1 to 4 tex list) 
            going to use.
        '''
        pass
    
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