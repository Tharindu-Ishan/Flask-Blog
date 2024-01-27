from flask import Flask, render_template, url_for

app=Flask(__name__)

posts=[
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'March 19, 2019'
    },
    {
        'author':'Jhon Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'Aug 09, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)