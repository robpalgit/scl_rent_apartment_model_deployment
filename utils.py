import json
import numpy as np
import joblib

__data_columns = None
__comunas = None
__neighborhoods = None
__model = None

neighborhood_dict = {
    # Huechuraba
    'Pedro Fontova': 'Huechuraba',
    'Ciudad Empresarial': 'Huechuraba',
    'Huechuraba': 'Huechuraba',
    'Ciudad Empresarial': 'Ciudad Empresarial',
    # La Reina
    'Metro Príncipe De Gales - Country Club': 'La Reina',
    'Carlos Ossandón': 'La Reina',
    'La Reina - Metro Simón Bolivar': 'La Reina',
    'La Reina': 'La Reina',
    'Blest Gana': 'Blest Gana',
    # San Joaquín
    'Rodrigo De Araya': 'San Joaquín',
    'Carlos Valdovinos': 'San Joaquín',
    'Metro San Joaquín': 'San Joaquín',
    'San Joaquín': 'San Joaquín',
    # La Cisterna
    'Lo Ovalle': 'La Cisterna',
    'Metro La Cisterna': 'La Cisterna',
    'La Cisterna': 'La Cisterna',
    'El Parrón': 'El Parrón',
    # Quinta Normal
    'Quinta Normal': 'Quinta Normal - Grupo 1',
    'Gruta De Lourdes': 'Quinta Normal - Grupo 1',
    'Blanqueado': 'Quinta Normal - Grupo 1',
    'Parque Padre Renato Poblete': 'Quinta Normal - Grupo 2',
    'Salvador Gutiérrez': 'Quinta Normal - Grupo 2',
    # Recoleta
    'Cementerios': 'Recoleta - Grupo 1',
    'Recoleta': 'Recoleta - Grupo 1',
    'Cerro Blanco': 'Recoleta - Grupo 2',
    'Patronato': 'Recoleta - Grupo 2',
    'Recoleta - Bellavista': 'Recoleta - Bellavista',
    # La Florida
    'La Florida': 'La Florida - Grupo 1',
    'Plaza Vespucio': 'La Florida - Grupo 1',
    'Metro Mirador': 'La Florida - Grupo 1',
    'Vicente Valdés': 'La Florida - Grupo 2',
    'La Florida Alto': 'La Florida - Grupo 2',
    'Rojas Magallanes': 'La Florida - Grupo 2',
    # Macul
    'Metro Las Torres': 'Macul - Grupo 1',
    'Metro Quilín': 'Macul - Grupo 1',
    'Metro Los Presidentes': 'Macul - Grupo 1',
    'Escuela Agrícola': 'Macul - Grupo 1',
    'Metro Macul': 'Macul - Grupo 1',
    'Villa Macul': 'Macul - Grupo 2',
    'Las Dalias': 'Macul - Grupo 2',
    'Santa Julia De Macul': 'Macul - Grupo 2',
    'Metro Camino Agrícola': 'Macul - Grupo 3',
    'Metro Carlos Valdovinos': 'Macul - Grupo 3',
    'Macul': 'Macul',
    # Lo Barnechea
    'Los Trapenses': 'Lo Barnechea - Grupo 1',
    'El Huinganal': 'Lo Barnechea - Grupo 1',
    'Valle Escondido': 'Lo Barnechea - Grupo 1',
    'La Dehesa': 'La Dehesa',
    'Lo Barnechea': 'Lo Barnechea',
    'Puente Nuevo': 'Puente Nuevo',
    'Plaza San Enrique': 'Plaza San Enrique',
    # Independencia
    'Plaza Chacabuco': 'Independencia - Grupo 1',
    'Juan Antonio Ríos': 'Independencia - Grupo 1',
    'Independencia': 'Independencia - Grupo 2',
    'Metro Cal Y Canto': 'Independencia - Grupo 2',
    'Hospitales': 'Hospitales',
    # San Miguel
    'Lo Vial': 'San Miguel',
    'Ciudad Del Niño': 'San Miguel',
    'El Llano': 'El Llano',
    'San Miguel': 'San Miguel',
    # Estación Central
    'San Alberto Hurtado': 'Estación Central',
    'Metro Ecuador': 'Estación Central',
    'Metro Las Rejas': 'Estación Central',
    'Universidad De Santiago': 'Universidad De Santiago',
    # Vitacura
    'Tabancura': 'Vitacura - Grupo 1',
    'Estadio Croata': 'Vitacura - Grupo 1',
    'Pío Xi': 'Vitacura - Grupo 1',
    'Parque Bicentenario': 'Vitacura - Grupo 2',
    'Estadio Manquehue': 'Vitacura - Grupo 2',
    'Nuestra Señora Del Rosario': 'Vitacura - Grupo 2',
    'Jardín Del Este': 'Vitacura - Grupo 3',
    'Borde Río - Casa Piedra': 'Vitacura - Grupo 3',
    'Juan Xxiii': 'Vitacura - Grupo 4',
    'Villa El Dorado': 'Vitacura - Grupo 4',
    'La Llavería': 'La Llavería',
    'Vitacura': 'Vitacura',
    # Ñuñoa
    'Plaza Egaña': 'Ñuñoa - Grupo 1',
    'Ñuñoa - Metro Simón Bolivar': 'Ñuñoa - Grupo 1',
    'Diagonal Oriente': 'Ñuñoa - Grupo 1',
    'Amapolas': 'Ñuñoa - Grupo 1',
    'Metro Irarrázaval': 'Ñuñoa - Grupo 2',
    'Villa Frei': 'Ñuñoa - Grupo 2',
    'Estadio Nacional': 'Ñuñoa - Grupo 2',
    'Juan Gómez Millas': 'Ñuñoa - Grupo 2',
    'Parque San Eugenio - Metro Ñuble': 'Ñuñoa - Grupo 2',
    'Plaza Ñuñoa': 'Ñuñoa - Grupo 3',
    'Metro Monseñor Eyzaguirre': 'Ñuñoa - Grupo 3',
    'Metro Ñuñoa': 'Ñuñoa - Grupo 3',
    'Diego De Almagro': 'Ñuñoa - Grupo 4',
    'Parque Botánico': 'Ñuñoa - Grupo 4',
    'Parque Juan Xxiii': 'Parque Juan Xxiii',
    # Providencia
    'Metro Tobalaba - Mall Costanera': 'Providencia - Grupo 1',
    'Barrio Italia': 'Providencia - Grupo 1',
    'Inés De Suárez': 'Providencia - Grupo 2',
    'Metro Bilbao': 'Providencia - Grupo 2',
    'Pedro De Valdivia': 'Providencia - Grupo 3',
    'Salvador': 'Providencia - Grupo 3',
    'Las Lilas': 'Providencia - Grupo 4',
    'Pedro De Valdivia Norte': 'Providencia - Grupo 4',
    'Los Leones': 'Los Leones',
    'Manuel Montt': 'Manuel Montt',
    'Campus Oriente': 'Campus Oriente',
    'Plaza Italia': 'Plaza Italia',
    'Providencia - Bellavista': 'Providencia - Bellavista',
    # Las Condes
    'Alto Las Condes': 'Las Condes - Grupo 1',
    'Mall Sport': 'Las Condes - Grupo 1',
    'Nueva Las Condes': 'Las Condes - Grupo 1',
    'Metro Hernando De Magallanes': 'Las Condes - Grupo 2',
    'Estoril': 'Las Condes - Grupo 2',
    'Barrio El Golf': 'Las Condes - Grupo 3',
    'San Carlos De Apoquindo': 'Las Condes - Grupo 3',
    'Vaticano': 'Las Condes - Grupo 4',
    'Parque Padre Alberto Hurtado': 'Las Condes - Grupo 4',
    'Metro Escuela Militar': 'Metro Escuela Militar',
    'Metro Manquehue - Apumanque': 'Metro Manquehue - Apumanque',
    'Parque Arauco': 'Parque Arauco',
    'Centro Financiero': 'Centro Financiero',
    'Sebastián Elcano': 'Sebastián Elcano',
    'Rotonda Atenas': 'Rotonda Atenas',
    'Los Dominicos': 'Los Dominicos',
    'Colón Oriente - Vital Apoquindo': 'Colón Oriente - Vital Apoquindo',
    # Santiago
    'San Diego': 'Santiago - Grupo 1',
    'Bogotá - Sierra Bella': 'Santiago - Grupo 1',
    'Barrio Diez De Julio': 'Santiago - Grupo 1',
    'Ejército - Toesca': 'Santiago - Grupo 2',
    'Barrio República': 'Santiago - Grupo 2',
    'Parque Los Reyes': 'Santiago - Grupo 2',
    'Centro Histórico De Santiago': 'Santiago - Grupo 3',
    'Barrio Brasil': 'Santiago - Grupo 3',
    'Barrio Yungay': 'Santiago - Grupo 4',
    'Franklin - Biobío': 'Santiago - Grupo 4',
    'Santa Isabel': 'Santiago - Grupo 5',
    'Parque Almagro': 'Santiago - Grupo 5',
    'Bulnes': 'Bulnes',
    "Parque O'Higgins": "Parque O'Higgins",
    'Barrio Lastarria': 'Barrio Lastarria',
    'Barrio San Borja': 'Barrio San Borja'
}

def predict_property_price(bedrooms, bathrooms, covered_area_m2, balcony_area_m2, comuna, neighborhood):
    if __model is None:
        load_saved_artifacts()
    try:
        comuna_index = __comunas.index(comuna.lower()) + 4
    except:
        comuna_index = -1
    try:
        neighborhood_index = __neighborhoods.index(neighborhood.lower()) + 21
    except:
        neighborhood_index = -1

    X = np.zeros(len(__data_columns))
    X[0] = bedrooms
    X[1] = bathrooms
    X[2] = covered_area_m2
    X[3] = balcony_area_m2
    if comuna_index >= 0:
        X[comuna_index] = 1
    if neighborhood_index >= 0:
        X[neighborhood_index] = 1

    return round(__model.predict([X])[0], 0)


def load_saved_artifacts():
    global __data_columns
    global __comunas
    global __neighborhoods

    with open("data_columns.json", "r") as file:
        __data_columns = json.load(file)['data_columns']
        __comunas = [x.replace("comuna_", "") for x in __data_columns[4:21]]
        __neighborhoods = [x.replace("neighborhood_", "") for x in __data_columns[21:]]

    global __model

    if __model is None:
        __model = joblib.load('rf_model_win.pkl')


def get_data_columns():
    return __data_columns

def get_comunas():
    return __comunas

if __name__ == '__main__':
    load_saved_artifacts()
    