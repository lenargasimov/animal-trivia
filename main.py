from flask import Flask, render_template, abort
from model import db

app = Flask(__name__)


@app.route('/questions/<int:index>')
def questions_view(index):
    try:
        questions_db = db[index]
        return render_template('quiz.html', 
                                question=questions_db,
                                index=index,
                                max_index=len(db) - 1)

    except IndexError:
        abort(404)



if __name__ == '__main__':
    app.run(debug=True)