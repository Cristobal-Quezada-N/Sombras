from flask import Flask, request
from simulator.map import mapa_inicializar
APP = Flask(__name__)


@APP.route("/")
def index():
    mapa = mapa_inicializar()
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    print(lat, lon)
    print("asdasdasd")
    return mapa.get_root().render()

if __name__ == "__main__":
    APP.run(debug=True)


