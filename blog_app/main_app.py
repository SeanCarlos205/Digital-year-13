from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '292ecfd3114ae58cffef6b2febc720e5'

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

#Route for home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

#Route for about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

#Route for registration page
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

#Route for login page
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form='forms')

if __name__ =='__main__':
    app.run(debug=True)