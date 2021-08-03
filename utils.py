#import pickle
import json
import numpy as np
import joblib

__comunas = None
__data_columns = None
__model = None

def predict_property_price(bedrooms, bathrooms, total_area_m2, balcony_area_m2, comuna):
    if __model is None:
        load_saved_artifacts()
    try:
        loc_index = __data_columns.index(comuna.lower())
    except:
        loc_index = -1

    X = np.zeros(len(__data_columns))
    X[0] = bedrooms
    X[1] = bathrooms
    X[2] = total_area_m2
    X[3] = balcony_area_m2
    if loc_index >= 0:
        X[loc_index] = 1

    return round(__model.predict([X])[0], 0)


def load_saved_artifacts():
    global __data_columns
    global __comunas

    with open("data_columns.json", "r") as file:
        __data_columns = json.load(file)['data_columns']
        __comunas = __data_columns[4:]

    global __model

    if __model is None:
        #with open('rf_model.pkl', 'rb') as file:
            #__model = pickle.load(file)
        __model = joblib.load('rf_model.pkl')
        #__model = joblib.load('rf_model.sav')


def get_comunas():
    return __comunas

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    