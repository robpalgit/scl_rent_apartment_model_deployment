from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import os
import utils

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', **{'SERVICE_URL': os.environ['SERVICE_URL']})

@app.route('/get_comunas')
def get_comunas():
    response = jsonify({
        'comunas': utils.get_comunas()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price', methods=['GET', 'POST'])
def predict_price():
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    total_area_m2 = float(request.form['total_area_m2'])
    balcony_area_m2 = float(request.form['balcony_area_m2'])
    comuna = request.form['comuna']

    response = jsonify({
        'predicted_price': utils.predict_property_price(bedrooms, bathrooms, total_area_m2, balcony_area_m2, comuna)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)
