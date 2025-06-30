from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    with open('data/items.json') as f:
        item_data = json.load(f)
    return render_template('items.html', items=item_data)

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)
