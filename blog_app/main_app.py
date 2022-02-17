from flask import Flask, render_template
app = Flask(__name__)

posts = [
    
    {
        'author': 'Sean Carlos',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 15, 2022'        
    },
    
    {
        'author': 'Joem Ama',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 17, 2022'        
    },
    
    {
        'author': 'Jenna Tolls',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'February 18, 2022'        
    }
    
]

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ =='__main__':
    app.run(debug=True)