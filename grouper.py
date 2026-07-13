#!/usr/bin/python3
import time, os
# 'printers' folder modules load
from printers.printer import *
from printers.coordinator import *
from printers.status import *
# 'graphics' folder modules load
from graphics.polygon import *
from graphics.polygonal import *
# 'connectors' folder modules load
from connectors.network import *
from connectors.sender import *
# Make Debugging Files
info = HTMLSummary(f'logs/grouper-{time.asctime().replace(' ', '_')}.html')
del time
# Connectors For Printers
net = PrintersNetwork()
sending = PrinterSender()
# Printer Manager
coordinator = PrinterCoordination()
printers_group = Status3DPrinters()
# Add Printer from settings file
with open('printers/settings.csv', 'r') as setup:
    lines: list[str] = setup.readlines()
    for line in lines:
        line: list[str] = line.split(',')
        new_printer = Obj3DPrinters()
        # Get data for each printer
        new_printer.set_ID(line[0])
        # Asociate IP address and Printer name
        net.set_printer(line[1], line[0])
        sending.set_printer(line[0])
        # Say What and How Print To The Printer
        new_printer.SETUP(line[2], line[3], line[4], net, sending)
    # Clean memory from unned variables
    del lines
# nested list 3D model name to printer
model_to_printer: list[list[str]] = [['example.stl', 'Example A']]    
# Main Block
if __name__ == '__main__':
    # Load New logs file
    info.add_text(coordinator.check_group())
    info.save()
    # Load 3D models
    for model in model_to_printer:
        net.get_printer_Obj(model[1]).load_model