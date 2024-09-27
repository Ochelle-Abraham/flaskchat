from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'AB',
        'Title' : 'First',
        'content' : 'first post content',
        'date_posted' : 'April 21, 2018'
    }, 
    {
        'author': 'Simieyaa',
        'Title' : 'Second',
        'content' : 'second post content',
        'date_posted' : 'April 21, 2018'
    }
]

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html')
#still working on video 
if __name__=='__main__':
    app.run(debug=True)