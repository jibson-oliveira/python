from flask import Flask

app = Flask('app')

@app.route ('/command', methods = ['POST'])
def command():
    return 'Teste efetuado com sucesso'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='54321')

