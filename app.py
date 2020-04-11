from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

from papy import Papy


# App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d443f27567d441f2b6176a'


@app.route("/")
def home():
    return render_template('home.html.django')


#ajax
@app.route("/ask/", methods=['GET', 'POST'])
def ajax():

    question = request.form['question']

    papy = Papy(question)

    papy.cogitation()

    dict = papy.get_response()

    return jsonify(
        question = dict['question'],
        place = dict['place'],
        location = dict['location'],
        maps = dict['maps'],
        wiki = dict['wiki'],
        hello = dict['hello'],
        introduction_maps = dict['introduction_maps'],
        introduction_wiki = dict['introduction_wiki'],
        bye = dict['bye'],
        errors = papy.errors,
    )


if __name__ == "__main__":
    app.run()
