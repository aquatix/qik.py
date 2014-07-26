from flask import Flask, session, g, render_template

app = Flask(__name__)
app.config.from_object('websiteconfig')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from qik_website import utils
from qik_website import filters
