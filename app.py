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

    if papy.errors:
        for i in range(len(papy.errors)):
            if papy.errors[i] == 'NO_MAPS':
                papy.errors.pop(i)

        if len(papy.errors) == 0:
            papy.errors = None

    dict = papy.get_response()

    return jsonify(
        question = dict['question'],
        place = dict['place'],
        location = dict['location'],
        maps = dict['maps'],
        wiki = dict['wiki'],
        wiki_link = dict['wiki_link'],
        hello = dict['hello'],
        introduction_maps = dict['introduction_maps'],
        introduction_wiki = dict['introduction_wiki'],
        bye = dict['bye'],
        errors = papy.errors,
    )


if __name__ == "__main__":
    app.run()
