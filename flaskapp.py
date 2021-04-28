from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Divya Rao',
        'title': 'Solo tripping in Coonoor is the best idea',
        'content': 'Tamil Nadu’s enchanting Coonoor is perhaps best experienced solo. Coonoor’s beautiful outdoors beckons travellers to experience all that it has to share. It is only 18 km away from Ooty, and 71 km from Coimbatore, and is a place that is known for its natural splendour.',
        'date_posted': 'April 29, 2021'
    },
    {
        'author': 'Jane Sloan',
        'title': 'Discovering Crete, The Biggest Island in Greece',
        'content': 'The beautiful island of Crete happens to also be the largest Greek island, located at the southernmost tip of Greece between the Cretan and Libyan seas.',
        'date_posted': 'April 20, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)