from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route('/')
@app.route('/'home)
def home():
    return "<h1>hello world"

@app.route('/about')
def about():
    return "<h1>About page"

if __name__=='__main__':
    app.run(debug=True)