import folium
from jinja2 import Template

def mapa_constructor(location=[-33.4477, -70.685585], zoom=16):
    # Mapa a devolver
    mapa = {
        'headers': '',
        'scripts': '',
        'body': '',
    }
    # Mapa
    mapa_constructor = folium.Map(
        location= location,
        zoom_start=zoom,
        height=600,
        width=1900,
    )
    # Extender la funcionalidad del Marcador de Mapa
    with open('./src/templates/Ext-ClickForMarker.html.jinja2', 'r') as template_marker:
        folium.ClickForMarker._template = Template(template_marker.read())
        folium.ClickForMarker().add_to(mapa_constructor)


    # Seoarar los componentes del mapa
    mapa_constructor.get_root().render()
    mapa['headers'] = mapa_constructor.get_root().header.render()
    mapa['scripts'] = mapa_constructor.get_root().script.render()
    mapa['body']   = mapa_constructor.get_root().html.render()

    return mapa
