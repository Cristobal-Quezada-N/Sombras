from flask import Flask, request, jsonify
from simulator.map import mapa_inicializar
APP = Flask(__name__)


@APP.route("/", methods=['POST', 'GET'])
def index():
    mapa = mapa_inicializar()
    coordenadas = str(request.get_data())
    coordenadas = coordenadas[9:-2].split(', ')
    print(f"[i] Coordenadas: {coordenadas}")
    return mapa.get_root().render()


if __name__ == "__main__":
    APP.run(debug=True)


