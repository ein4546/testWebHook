from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form.get('name')
    return f'Welcome {name}!'

if __name__ == '__main__':
    app.run(debug=True)
