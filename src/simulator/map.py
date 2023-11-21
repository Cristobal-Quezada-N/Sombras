import folium
from jinja2 import Template
def mapa_inicializar():
         # Mapa
         mapa_principal = folium.Map(
             location=(-33.4400082,-70.6811497),
             zoom_start=1000
         )
         # Elementos del Mapa
         _templateClickForMarker = """{% macro script(this, kwargs) %}
             mapa = {{this._parent.get_name()}}
             mapa.on('click', onClick);
             function onClick(e){
                 if (typeof marcador != 'undefined'){
                     marcador.setLatLng(e.latlng)
                 }
                 else{
                     marcador = L.marker().setLatLng(e.latlng).addTo(mapa)
                 }
                 history.replaceState({}, "", `?lat=${marcador._latlng.lat}&lon=${marcador._latlng.lng}`)
             }
         {% endmacro %}"""
         
         folium.ClickForMarker._template = Template(_templateClickForMarker)
         folium.ClickForMarker().add_to(mapa_principal)

         return mapa_principal

