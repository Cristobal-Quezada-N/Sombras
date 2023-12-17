from flask import Flask, render_template, request, render_template_string, request, redirect, url_for
from simulator.map import mapa_constructor
from simulator.sombra import info_sol

import random

template = """
        <!DOCTYPE html>
        <html>
            <head>
                {{ headers | safe }}
            </head>
            <body>
                <h1>USACH INFORMACIÓN SOLAR</h1>
                {{ mapa | safe }}
                <div style="display: block;" id="INFO">Haz click en el mapa </div>
                {{ info | safe }}
               <script>
                    {{ scripts|safe }}
                </script>

                <script>
                    function update(){
                        $.get("/info", function(data){
                            if (data != "None"){
                                $("#INFO").html(data)
                            }
                        });
                    }
                        update()
                    }, 1000);
                   window.onClick(e){
                    console.log("eeee")
                   } 
                </script>
            </body>
        </html>
"""

# Instanciar el servidor APP
app = Flask(__name__)

# Instanciar el mapa
mapa = mapa_constructor()

# Crear ruta principal de la Pagina
# - GET para entregar el mapa
# - POST para recibir datos como coordenadas
@app.route("/")
def index():
    return pagina_template(mapa)

@app.route("/", methods=['POST'])
def index_post():
    coordenadas = request.get_json() # coordenadas: b'LatLng(<float>, <float>)'
    print(f"[i] Coordenadas: {coordenadas}")
    info = info_sol(coordenadas)
    return render_template_string(source=template, info=info)

def pagina_template(mapa, info=[]):
    a = random.random()
    print(info)

    return render_template_string(
        source  =template,
        # Elementos que se agregan al html
        info = info,
        headers =mapa[0],
        mapa    =mapa[1],
        scripts =mapa[2],
    )

@app.route('/info')
def info():
    info = str(request.args.get('data'))
    if info == None:
        print('aaaaa')
        print(info)
    return str(info)


# Ejecutar el servidor si se ejecuta el archivo (server.py)
if __name__ == "__main__":
    app.run(debug=True)
