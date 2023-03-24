from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/work")
def work():
    return render_template('work.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    email = request.form['emailHead']
    message = request.form['msgBody']
    print(f'You have a message from {email}. It reads {message}')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
