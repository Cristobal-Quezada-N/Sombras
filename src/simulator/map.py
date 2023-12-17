import folium
from jinja2 import Template
from branca import element as Elementos


def mapa_constructor(location=[-33.4477, -70.685585], zoom=16):
         # Mapa
        mapa_principal = folium.Map(
            location= location,
            zoom_start=zoom,
            height=600,
            width=1900,
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
                //history.replaceState({}, "", `?latlng=${marcador._latlng.lat},${marcador._latlng.lng}`)

            // Comunicar las coordenadas al Servidor
                $.ajax({
                    type : "POST",
                    data: JSON.stringify(marcador._latlng),
                    contentType: 'application/json',
                    success: function() {
                        console.log(marcador._latlng);
                        }
                });
            }
        {% endmacro %}
        """

        folium.ClickForMarker._template = Template(_templateClickForMarker)
        folium.ClickForMarker().add_to(mapa_principal)


        # Seoarar los componentes del mapa
        mapa_principal.get_root().render()
        header = mapa_principal.get_root().header.render()
        body   = mapa_principal.get_root().html.render()
        script = mapa_principal.get_root().script.render()


        return [header, body, script]
