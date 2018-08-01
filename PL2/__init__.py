from flask import Flask
#from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-a-trial'
from PL2 import routes