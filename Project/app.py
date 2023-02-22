import numpy as np
from flask import Flask, request, jsonify
from Core.utils import Utils

app = Flask(__name__)

# POSTMAN PARA PRUEBAS
@app.route('/predict', methods=['POST'])
def predict():
    # recogemos los datos
    args = request.get_json()
    data = np.array(args)
    data = data.reshape(1, -1)

    # Predecimos
    prediction = model.predict(data)

    # Devolvemos la predicción
    output = {'prediction': prediction.tolist()}
    return jsonify(output)

if __name__ == '__main__':
    # Cargamos el modelo
    model = Utils.load_model('Models/best_model_3.287.pkl')
    app.run(port=8080)
