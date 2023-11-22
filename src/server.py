from flask import Flask, request
from simulator.map import mapa_constructor
from folium.elements import JavascriptLink

# Instanciar el servidor APP
app = Flask(__name__)

# Instanciar el mapa
mapa = mapa_constructor()
## Incorporar la api de Shademap 
SHADEMAP_LIB = 'https://unpkg.com/leaflet-shadow-simulator/dist/leaflet-shadow-simulator.umd.min.js'
mapa.get_root().html.add_child(JavascriptLink(SHADEMAP_LIB))

# Crear ruta principal de la Pagina
# - GET para entregar el mapa
# - POST para recibir datos como coordenadas
@app.route("/", methods=['POST', 'GET'])
def index():
    coordenadas = str(request.get_data()) # coordenadas: b'LatLng(<float>, <float>)'
    coordenadas = coordenadas[9:-2].split(', ')
    print(f"[i] Coordenadas: {coordenadas}")
    # Servir al usuario el mapa en formato html
    return mapa.get_root().render()


# Ejecutar el servidor si se ejecuta el archivo (server.py)
if __name__ == "__main__":
    app.run(debug=True)
