from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def page() -> str:
    text: str = ''

    with open('index.html', 'r') as content:
        for line in content.readlines():
            if text.__contains__('CODE'):
                # Generate different ticket code in each running
                text += line.replace('CODE', hex(hash('CODE').__abs__()).replace('0x', 'c'))
            else:
                # Add HTML line to render web
                text += line    
    return text

@app.route('/delivery', methods = ['POST'])
def inform() -> str:
    import sqlite3

    data: list[str] =   [
                            request.cookies['grouper'],
                            request.form['copies'],
                            request.form['material']
                        ]
    
    # Load file binary content
    binary: list[bytes] = []

    for bin in data[0]:
        if (data.index(bin) % 2 == 0):
            # Add each Two digits digits As Bytes
            binary.append(bytes(int((bin + data[data.index(bin)] + 1), 16), 'utf-8'))
    # Write as binary file in models folder
    with open(f'models/user_{binary.__hash__()}.3mf', 'wb') as writer:
        for bin in binary:
            writer.write(bin)
                     
    return page()