from flask import Flask, render_template
from flask import request

app = Flask(__name__)

inform_code: str = ''

def byte_translate(character) -> str:
    '''
        Decode character using table as byte 
        hexadecimal numeric text.
    '''
    state = character

    if character == 'x':
        state = 'A'
    elif character == 'g':
        state = 'B'
    elif character == 'h':
        state = 'C'
    elif character == 'i':
        state = 'D'
    elif character == 'j':
        state = 'E'
    elif character == 'k':
        state = 'F'
    elif character == 'l':
        state = '10'
    elif character == 'm':
        state = '11'
    elif character == 'n':
        state = '12'
    elif character == 'o':
        state = '13'
    elif character == 'p':
        state = '14'
    elif character == 'q':
        state = '15'
    elif character == 'r':
        state = '16'
    elif character == 's':
        state = '17'
    elif character == 't':
        state = '18'
    elif character == 'u':
        state = '19'
    elif character == 'v':
        state = '1A'
    elif character == 'w':
        state = '1B'
    elif character == 'y':
        state = '1C'
    elif character == 'z':
        state = '1D'
    elif character == '+':
        state = '1E'
    elif character == '*':
        state = '1F'
    elif character == '-':
        state = '20'
    elif  character == '/':
        state = '21'
    elif character == '.':
        state = '22'
    elif character == ',':
        state = '23'
    elif character == ';':
        state = '24'
    elif character == '{':
        state = '25'
    elif character == '}':
        state = '26'
    elif character == '(':
        state = '27'
    elif character == ')':
        state = '28'
    elif character == ':':
        state = '29'
    elif character == '@':
        state = '2A'
    elif character == '%':
        state = '2B'
    elif character == '=':
        state = '2C'
    elif character == '?':
        state = '2D'
    elif character == '¿':
        state = '2E'
    elif character == '$':
        state = '2F'
    elif character == '#':
        state = '30'
    elif character == '&':
        state = '31'
    elif character == '\\':
        state = '32'
    elif character == '~':
        state = '33'
    elif character == '<':
        state = '34'
    elif character == '>':
        state = '35'
    elif character == '!':
        state = '36'
    elif character == '_':
        state = '37'
    elif character == '°':
        state = '38' 
    elif character == '|':
        state = '39'  
    elif character == '¬':
        state = '3A'
    elif character == '^':
        state = '3B'
    elif character == '`':
        state = '3C'
    elif character == '¨':
        state = '3D'
    elif character == "'":
        state = '3E'
    elif character == 'Ø':
        state = '3F'
    elif character == '«':
        state = '40'
    elif character == '»':
        state = '41'
    elif character == '¦':
        state = '42'
    elif character == '©':
        state = '43'
    elif character == '¢':
        state = '44' 
    elif character == 'Ł':
        state = '45'
    elif character == 'Ω':
        state = '46'
    elif character == 'ß':
        state = '47' 
    elif character == 'æ':
        state = '48'
    elif character == 'Ð':
        state = '49'
    elif character == 'ŋ':
        state = '4A' 
    elif character == 'þ':
        state = '4B'
    elif character == ' ':
        state = '4C'
    elif character == '€':
        state = '4D' 
    elif character == '¥':
        state = '4E'
    elif character == '·':
        state = '4F' 
    elif character == 'Σ':
        state = '50'
    elif character == 'φ':
        state = '51' 
    elif character == 'ψ':
        state = '52'
    elif character == 'ᴨ':
        state = '53'
    elif character == 'Δ':
        state = '54'
    elif character == '¶':
        state = '55'
    elif character == '®':
        state = '56' 
    elif character == '¼':
        state = '57'  
    elif character == '½':
        state = '58'
    elif character == '♦':
        state = '59'
    elif character == '♣':
        state = '5A' 
    elif character == '♠':
        state = '5B'
    elif character == '♥': 
        state = '5C' 
    elif character == '♩':
        state = '5D'                                                                                                                                                                                                                                 
        
    return state

@app.route('/', methods = ['GET'])
def page() -> str:
    '''
        Use template for generate web
        form for define new delivery
        request.
    '''
    text: str = ''

    with open('templates/index.html', 'r') as content:
        for line in content.readlines():
            if text.__contains__('CODE'):
                # Generate different ticket code in each running
                inform_code = hex(hash('CODE').__abs__()).replace('0x', 'c')
                text += line.replace('CODE', inform_code)
            else:
                # Add HTML line to render web
                text += line    
    return text

@app.route('/delivery', methods = ['POST'])
def inform() -> str:
    '''
        Generate reports and save delivery data into
        database to send later.
    '''
    import sqlite3
    connector = sqlite3.connect('delivery.db')
    runner = connector.cursor()
    # Data to save in database
    file_name: str = ''

    data: list[str] =   [
                            request.cookies['grouper'],
                            request.form['copies'],
                            request.form['material']
                        ]
    
    # Load file binary content
    binary: list[bytes] = []

    for b in data[0]:
        # Add One Character that represent Byte
        binary.append(bytes(int(byte_translate(b), 16), 'utf-8'))
    # Write as binary file in models folder
    try:
        file_name = binary.__hash__()
        with open(f'models/user_{file_name}.3mf', 'wb') as writer:
            for bin in binary:
                writer.write(bin)
    except:
        pass
    # Save Into database
    try:
        runner.execute('CREATE TABLE delivery(Code varchar(20), File varchar(20), Copies int, Material varchar(4), Place varchar(20));')
        connector.commit()
        runner.execute(f'INSERT INTO delivery(Code, File, Copies, Material) VALUES ({inform_code}, {file_name}, {data[0]}, {data[1]});')                 
        connector.commit()
    except:
        pass
    # Render the form for view the loaded data
    return page()