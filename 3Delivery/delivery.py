from flask import Flask
from flask import Request

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

    form = Request()
    data: list[str] =   [
                            form.form['model'],
                            form.form['copies'],
                            form.form['material']
                        ]
    return page()