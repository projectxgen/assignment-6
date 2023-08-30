from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    context={'tip': '0.00', 'total': '0.00'}
    return render_template("index.html", context=context)

@app.route('/', methods=['POST'])
def calculate_tips():
    tip = 0
    total = 0
    amount = 0
    people = 0

    # Your code here

    context={'tip': '0.00', 'amount': '', 'total': '0.00', 'people': ''}

    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.run(debug=True)