import flask
from flask import *
import json
import  pymysql

app = Flask(__name__,static_folder="static",static_url_path="/static",template_folder="templates")

@app.errorhandler(404)
def page_not_found(e):
    return Response("<h1>404 Not Found</h1>"),404

@app.route('/')
def index():
    if request.cookies.get("u"):
        return flask.redirect("index_login")
    return flask.render_template("index.html")

@app.route('/index_login')
def index_login():
    name = request.cookies.get("u")
    return flask.render_template("index_login.html",name=name)

@app.route('/login')
def login():
    if request.cookies.get("u"):
        return flask.redirect("index_login")
    return flask.render_template("login.html")

@app.route('/login2',methods=['POST'])
def login2():
    username = request.form.get("username")
    response = make_response(flask.redirect("/"))
    response.set_cookie("u",username)
    return response

@app.route('/logout')
def logout():
    response = make_response(flask.redirect("/"))
    response.delete_cookie("u")
    response.delete_cookie("p")
    return response


def main():
    app.run(host='0.0.0.0',port=8888,debug=True)



if __name__ =='__main__':
    main()
