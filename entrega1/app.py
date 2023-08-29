from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)

app.run(host="0.0.0.0", port=8000, debug=True)