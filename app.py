from flask import flask
app = flask(_name_)

@app.route('/')
def index():
    return '<h1> News Highlight </h1>'


if __name__ == '__main__':
 app.run(debug = True)