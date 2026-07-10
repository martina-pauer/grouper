class PrintersNetwork:

    def __init__(self):
        '''
            Define Relations IP
            Address and ID for the
            printers network.
        '''
        self.Printers_IP_Addresses: list[str] = []

        self.Printers_IDs: list[str] = []

    def set_printer(self, IP_Address: str, ID: str):
        '''
            Make Pair IP with ID.
        '''
        self.Printers_IP_Addresses.append(IP_Address)
        self.Printers_IDs(ID)

    def get_printer_IP(self, ID) -> str:
        '''
            From One ID Get The Printer
            IP Address.
        '''
        return self.Printers_IP_Addresses[self.Printers_IDs.index(ID)]