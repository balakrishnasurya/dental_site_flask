from flask import Flask, render_template

app = Flask(__name__)

# This route tells Flask what to load when someone visits the main URL (/)
@app.route('/')
def home():
    # Flask automatically looks in the "templates" folder for this file
    return render_template('index.html')

if __name__ == '__main__':
    # debug=True allows the server to auto-reload if you make changes to your code
    app.run(debug=True)