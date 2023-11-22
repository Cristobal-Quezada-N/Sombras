import folium
from jinja2 import Template


def mapa_constructor(location=[-33.4477, -70.685585], zoom=16):
         # Mapa
        mapa_principal = folium.Map(
            location= location,
            zoom_start=zoom
        )
        # Extender la funcionalidad del Marcador de Mapa
        _templateClickForMarker = """
        {% macro script(this, kwargs) %}
            mapa = {{this._parent.get_name()}}
            mapa.on('click', onClick);
            function onClick(e){

            // Actualizar la posición del marcador

               if (typeof marcador != 'undefined'){
                   marcador.setLatLng(e.latlng)
               }
               else{
                   marcador = L.marker().setLatLng(e.latlng).addTo(mapa)
               }

               // Actualizar parametros en url
               history.replaceState({}, "", `?latlng=${marcador._latlng.lat},${marcador._latlng.lng}`)

               // Comunicar las coordenadas al Servidor
               fetch(
                  '/',
                  {
                      method: 'POST',
                      body: marcador._latlng
                  },
               )
            }
        {% endmacro %}
        """

        folium.ClickForMarker._template = Template(_templateClickForMarker)
        folium.ClickForMarker().add_to(mapa_principal)

        return mapa_principal
