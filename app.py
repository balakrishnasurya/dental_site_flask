from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Construct the path to the JSON file
    json_path = os.path.join(app.root_path, 'data.json')
    
    # Read the JSON file
    with open(json_path, 'r', encoding='utf-8') as file:
        site_data = json.load(file)
        
    # Pass the data to the template
    return render_template('index.html', data=site_data)

if __name__ == '__main__':
    app.run(debug=True)