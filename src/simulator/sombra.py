from pysolar.solar import get_altitude
from pysolar.radiation import get_radiation_direct

import pytz
import datetime

def generara_rangos_sol(coordenadas):
    info = []
    lat = coordenadas['lat']
    lng = coordenadas['lng']

    fecha = datetime.date.today()
    #STEP=3600
    STEP=3600 # Obtener para cada hora
    
    for i in range(0,3600*24, STEP):
        hora = int(i / 3600)
        segundo = i - hora*3600
        minuto = int(segundo/60)
        segundo = segundo - minuto*60

        # asignar dia en el cual se sacan los datos
        date = datetime.datetime(
                fecha.year,
                fecha.month,
                fecha.day,

                hora,
                minuto,
                segundo,
                tzinfo=pytz.timezone('America/Santiago')
        )
        
        # altitud sol
        altitude_deg = get_altitude(lat, lng, date)
        # Radicion directa

        radiacion = get_radiation_direct(date, altitude_deg)

        # Formatear los datos para devolverlos en <float> radiacion, <str> fecha, <str> tiempo]
        # La radiacion es medida en wattss por metro cuadrado
        date = str(date).split()
        Radicion_Hora = dict(
                radiacion   = radiacion,
                fecha       = date[0],
                hora        = date[1]
        )
        info.append(Radicion_Hora)
    return info
 

# Aqui se demuestra la necesidad de class o structs
def info_sol(coordenadas):
    info = []
    mayor = dict(radiacion = 0.0, fecha = '', hora = '')
    intervalos_sol = generara_rangos_sol(coordenadas)
    for intervalo in intervalos_sol:
        # Agregar valores en formato list
        info.append(list(intervalo.values()))
        # Encontrar el mayor intervalo de radiacion.
        if intervalo['radiacion'] > mayor['radiacion']:
            mayor = intervalo
    mayor = list(mayor.values())
    return [mayor ,info]
