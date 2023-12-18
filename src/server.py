from flask import Flask, request, render_template, request 

from simulator.map import mapa_constructor
from simulator.sombra import info_sol

from flask_socketio import SocketIO

# from threading import Lock

# Instanciar el servidor y manejar hilos para conexiones
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
#thread = None
#thread_detectado = Lock()

# Instanciar el mapa
# - Solo se ejecuta una vez
mapa = mapa_constructor()

# Crear ruta principal de la Pagina
# - GET para entregar el mapa
# - POST para recibir datos como coordenadas
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        coordenadas = request.get_json() # coordenadas: { 'lat' : <float>, 'lng': <float> }
        print('\n----------------------------------------------------------------------\n')
        print(f"[i] Coordenadas: {coordenadas}")
        print('\n----------------------------------------------------------------------\n')
        info = info_sol(coordenadas)
        # Se envian datos al Cliente
        socketio.emit('info', { 'mayor': info[0], 'intervalos': info[1:] })
    return pagina_template(mapa)


def pagina_template(mapa):
    return render_template('index.html',
                           # Elementos que se agregan al html
                           headers =mapa['headers'],
                           scripts =mapa['scripts'],
                           mapa    =mapa['body']
                           )
# Manejar conexiones
@socketio.on('connect')
def conexion():
    # global thread
    print('\n----------------------------------------------------------------------\n')
    print('[i] Cliente Conectado')
    print('\n----------------------------------------------------------------------\n')
# [TODO]: gestionar ubicacion
#    with thread_detectado:
#        if thread is None:
#            thread = socketio.start_background_task(pedir_ubicacion)

def disconnect():
    print('\n----------------------------------------------------------------------\n')
    print('[i] Client disconnected')
    print('\n----------------------------------------------------------------------\n')


# Ejecutar el servidor si se ejecuta el archivo (server.py)
if __name__ == "__main__":
    app.run(debug=True)
