from flask import Flask, render_template
from chess_engine import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/move/<path:fen>/')
def get_move(fen):
    print("Calculating...")
    engine = Engine(fen)
    move = engine.calculate_ab(4)
    # engine.print_best_sequence()
    # print("Move found!", move)
    print()
    return move


@app.route('/test/<string:tester>')
def test_get(tester):
    return tester


if __name__ == '__main__':
    app.run(debug=True)