# Cartografia

# Se iportan las librerias necesarias
import folium, json
import pandas as pd

# Se hace la lectura del archivo que contiene el mapa geografico
prov_geo = r'colombia.geo.json'

# Se le asigna una localizacion inicial y zoom en el mapa
m = folium.Map(location = [0,-80], zoom_start = 5)

folium.Choropleth(
    geo_data=prov_geo,     # Mapa geografico
    data=None,             # Data
    columns=None,          # Columnas de la Data
    key_on=None,           # Key ON
    fill_color='YlGn',     # Color
    fill_opacity=0.7,      # Opacidad del color
    line_opacity=0.2,      # Opacidad entre lineas
    legend_name='Colombia' # Nombre
).add_to(m)                # Se añade al mapa

m.save('map.html') # Se guarda el mapa en un archivo.html