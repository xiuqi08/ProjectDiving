import flask

from flask import render_template
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def index(sport=0):
    return render_template('index.html',selection = ["Snorkelling","Diving"], sport = sport)

@app.route('/price', methods = ['GET','POST'])
def price(sport=0):
    sport = request.form['sports']
    return render_template('index.html',selection = ["Snorkelling","Diving"], sport = sport)

class PrizeCalculating():
    #Initialize as 0, 
    __sport = 0
    
    def setSport(self, sport):
        self.__sport = sport
    
    def calculate(self):
        if self.__sport == 'Diving':
            return 7500
        elif self.__sport == 'Snorkelling':
            return 5000
        else:
            return 0

if __name__ == '__main__':
    app.run(debug=True)
