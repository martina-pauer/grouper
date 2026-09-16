from flask import Flask, render_template
from flask import request

app = Flask(__name__)

inform_code: str = ''

def byte_translate(character) -> str:
    '''
        Decode character using table as byte 
        hexadecimal numeric text.
    '''
    # Turn Into character Unicode Decimal Number Code
    code = ord(character)
    # Decrease 100
    code = (code - 100)
    # Turn the Result to hexademial
    state = hex(code).replace('0x', '')
                                                                                                                                                                                                                                                                                   
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
                            request.form['address'],
                            request.form['copies'],
                            request.form['material'],
                            request.form['model']
                        ]
    # Use Pre-loaded piece
    file_name = data[3]
    # Save Into database
    try:
        runner.execute('CREATE TABLE delivery(Code varchar(20), File varchar(20), Copies int, Material varchar(4), Place varchar(20));')
        connector.commit()
    except:
        pass
    try:
        runner.execute(f'INSERT INTO delivery (Code, File, Copies, Material, Place) VALUES ("{inform_code}", "{file_name}", {data[1]}, "{data[2]}", "{data[0]}");')                 
        connector.commit()
    except:
        pass    
    # Render the form for view the loaded data
    return page()