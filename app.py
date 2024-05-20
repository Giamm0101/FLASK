from flask import Flask, render_template
import csv
import requests

app = Flask(__name__)
titol = 'ciao sito'


@app.route('/')  # route di default con slash
def hello_world():
    bottoni = {
        'b1': 'movies',
        'b2': 'music',
        'b3': 'book',
        'b4': 'Videogiochi'
    }
    # per richiamare il diz in html si usa la sintassi 'bottoni.b1'
    return render_template("home2.html", titolo='Benvenuti nel nostro sito'.upper(), bottoni=bottoni)


@app.route('/data')  # route di default con slash
def data():
    return 'Ciao, data!'


@app.route('/movies')  # route di default con slash
def movies():
    return render_template('movies.html')
#movies lavora lato server


@app.route('/book')
def book():
    return render_template('book.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/datisito/titolo')
def tornatitolo():
    return titol


@app.route('/api/generi')
def tornageneri():
    return ['Horror', 'Fantasy', 'Comedy', 'Sci-Fi']


@app.route('/movies2')  # route di default con slash
def movies2():
    response = requests.get('https://api.chucknorris.io/jokes/categories')
    print(response)
    dati = response.json()
    print(dati)
    return render_template('movies2.html', dati=dati)
# movies2 avviene lato server
# response è un oggetto di type response


# tutte rotte in modalita GET (quando non viene specificato nulla)
# quando si compila un post di solito è di modalita POST

if __name__ == '__main__':
    app.run(debug=True)
