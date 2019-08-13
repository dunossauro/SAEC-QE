from flask import Flask

app = Flask('__name__')


@app.route('/')
def hello():
    return '''
        <div id=texto>Bem vindos a SAEC 2019</div>
    '''


app.run()
