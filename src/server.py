from flask import Flask, request, render_template_string, request 

from simulator.map import mapa_constructor
from simulator.sombra import info_sol

from flask_socketio import SocketIO
# from threading import Lock

template = """
        <!DOCTYPE html>
        <html>
            <head>
                {{ headers | safe }}
                <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.2/socket.io.min.js" integrity="sha384-mZLF4UVrpi/QTWPA7BjNPEnkIfRFn4ZEO3Qt/HFklTJBj/gBOV8G3HcKn4NfQblz" crossorigin="anonymous"></script>
                <script>
                    $(document).ready( function () {
                        console.log("SOCKET")
                        var socket = io.connect()
                        socket.on('info', function(msg){
                            //console.log("[i] Informacion recibida: " + msg.data)
                            document.getElementById("INFO").innerHTML = msg.data;
                        })
                    })
                </script>
            </head>
            <body>
                <h1>USACH INFORMACIÓN SOLAR</h1>
                {{ mapa | safe }}
                <div style="display: block;" id="INFO">Haz click en el mapa </div>
                {{ info | safe }}
               <script>
                    {{ scripts|safe }}
               </script>
            </body>
        </html>
"""

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
        print(f"[i] Coordenadas: {coordenadas}")
        info = info_sol(coordenadas)
        socketio.emit('info', { 'data': info })
    return pagina_template(mapa)


def pagina_template(mapa):
    return render_template_string(
        source  =template,
        # Elementos que se agregan al html
        headers =mapa['headers'],
        scripts =mapa['scripts'],
        mapa    =mapa['body'],
    )



# Manejar conexiones
@socketio.on('connect')
def conexion():
    # global thread
    print('[i] Cliente Conectado')
# [TODO]: gestionar ubicacion
#    with thread_detectado:
#        if thread is None:
#            thread = socketio.start_background_task(pedir_ubicacion)




def disconnect():
    print('[i] Client disconnected')

# Ejecutar el servidor si se ejecuta el archivo (server.py)
if __name__ == "__main__":
    app.run(debug=True)
