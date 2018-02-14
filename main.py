import flask

from flask import render_template

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    dropdown_list = ["Snorkelling","Diving"]
    if request.method == 'POST':
        sport = request.form['sports']
    return render_template('index.html',dropdown_list=dropdown_list,sport = sport)

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