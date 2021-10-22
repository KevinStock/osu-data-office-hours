from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/news')
def news():
    return render_template('news.html', title="News")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run(debug=True)