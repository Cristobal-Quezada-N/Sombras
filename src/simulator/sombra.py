from pysolar.solar import get_altitude
from pysolar.radiation import get_radiation_direct

import pytz
import datetime

def info_sol(coordenadas):
    info = []
    latitude_deg = float(coordenadas[0])
    longitude_deg = float(coordenadas[1])

    fecha = datetime.date.today()
    
    dia = fecha.day
    mes = fecha.month
    año = fecha.year
    #STEP=3600
    STEP=3600 # Obtener para cada hora
    
    for i in range(0,3600*24, STEP):
        hora = int(i / 3600)
        segundo = i - hora*3600
        minuto = int(segundo/60)
        segundo = segundo - minuto*60
        # asignar dia en el cual se sacan los datos
        date = datetime.datetime(año, mes, dia, hora, minuto, segundo, tzinfo=pytz.timezone('America/Santiago'))
        
        # altitud sol
        altitude_deg = get_altitude(latitude_deg, longitude_deg, date)
        # Radicion directa

        result = get_radiation_direct(date, altitude_deg)

        # Formatear los datos para devolverlos en [<float> radiacion, <str> fecha, <str> tiempo]
        date = str(date).split()
        result = [result]
        result.extend(date)
        info.append(result)
    return info
