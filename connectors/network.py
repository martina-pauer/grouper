class PrintersNetwork:

    def __init__(self):
        '''
            Define Relations IP
            Address and ID for the
            printers network.
        '''
        self.Printers_IP_Addresses: list[str] = []

        self.Printers_Objs: list[str] = []

    def set_printer(self, IP_Address: str, obj):
        '''
            Make Pair IP with ID.
        '''
        self.Printers_IP_Addresses.append(IP_Address)
        self.Printers_Objs(obj)

    def get_printer_IP(self, ID) -> str:
        '''
            From One ID Get The Printer
            IP Address.
        '''
        Printer_ID: str = ''
        index: int = 0

        for printer in self.Printers_Objs:
            new_ID = printer.get_ID()
            # Check valid ID
            if new_ID == ID:
                Printer_ID = new_ID
                break
            # Inrease counter for next ID
            index += 1
        # Get IP from analog position to printer object    
        return self.Printers_IP_Addresses[index]
    
    def get_printer_Obj(self, ID):
        '''
            Give Obj3DPrinter object
        '''
        for printer_obj in self.Printers_Objs:
            if printer_obj.get_ID() == ID:
                return printer_obj
                break