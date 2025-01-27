from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'Faith Kamaraju',
        'title' : 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'January 26, 2025'
    },
    {
        'author': 'Maeve Guenette',
        'title' : 'Dnd stuff',
        'content': 'DND DND DND DND',
        'date_posted': 'January 25, 2025'
    }
]


#routes

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About Page')



if __name__ == "__main__":
    app.run(debug=True)