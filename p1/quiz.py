from flask import Flask,session,redirect,url_for
from db_script import *

def index():
    return "<h1>HELLO NEW ZEALAND"

def test():
    return 0
def result():
    return 0

app = Flask(__name__)
app.add_url_rule("/","index",index)
app.add_url_rule("/test","test",test)
app.add_url_rule("/result","result",result)
app.secret_key = "niggers" 

if __name__ == "__main__":
    app.run()