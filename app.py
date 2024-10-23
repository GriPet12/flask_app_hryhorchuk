from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route('/')
def home():
    return render_template('base.html', title="Home")

@app.route('/resume')
def resume():
    return render_template('resume.html', title="My Resume")

if __name__ == '__main__':
    app.run()
