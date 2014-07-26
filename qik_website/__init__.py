from flask import Flask, session, g, render_template

app = Flask(__name__)
app.config.from_object('websiteconfig')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from flask_website import utils
from flask_website import filters
