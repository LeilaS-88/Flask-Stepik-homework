from flask import  Flask, render_template
from game_of_life import GameOfLife

app =  Flask(__name__)

game_of_life = None

@app.route('/')
def index():
    GameOfLife(20, 20)
    return render_template('index.html')

@app.route('/live')
def live():
    life = GameOfLife()
    if life.counter > 0:
            life.form_new_generation()
    life.bump()
    generation = life.world
    return render_template('live.html', generation=generation, life=life)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

