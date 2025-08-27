from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    print("Home route accessed")  # Debug print
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, port=5000)
