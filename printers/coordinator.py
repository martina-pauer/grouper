class PrinterCoordination:
    
    def __init__(self):
        '''
            Coordinate Many Printer Groups
            For Manage Different Building Steps.
        '''
        self.groups[Status3DPrinters] = []
        
    def add_group(self, group):
        '''
            Add A New Group To The Groups Group.
        '''
        self.groups.append(group)

    def enable_group(self, group):
        '''
            Make Active the group
            If is in the groups list.
        '''
        for grouping in self.groups:
            if grouping.get_printers() == group.get_printers():
                grouping.turn_ON_all()
                break

    def disable_group(self, group):
        '''
            Disable printers Sub Set From
            group.
        '''
        for disabling in self.groups:
            if disabling.get_printers() == group.get_printers():
                disabling.turn_OFF_all()
                break

    def check_group(self, group) -> str:
        '''
            Give Logs from All Printers In 
            All Groups.
        '''
        checked: str = ''
        group_number: int = 1
        total_groups: int = self.groups.__len__()

        for checked_group in self.groups:
            checked += f'[ Group {group_number} / {total_groups}]\n'
            for checked_printer in self.check_group:
                checked += f"\t( Printer '{checked_printer.get_ID()}' )\n"
                for checked_fail in checked_printer.fails():
                    checked += f'\t\t-> {checked_fail}\n'