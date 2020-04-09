from flask import Flask, render_template, url_for, request, redirect, flash


# App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d443f27567d441f2b6176a'


@app.route("/")
def home():
    return render_template('home.html.django')


#ajax
#jsonify
def ajax():
    return render_template('home.html.django')


if __name__ == "__main__":
    app.run()
