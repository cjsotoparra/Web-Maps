import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


map = folium.Map(location=[35.70387918204649, 139.79352861911002], tiles="Stamen Terrain")


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""


fgv = folium.FeatureGroup(name = "Volcanoes")
colr = " "

for lt, ln, el, name in zip(lat, lon, elev, name):

	if el <= 1000:
		colr = "red"
	elif el > 1000 and el <= 2000:
		colr = "blue"
	elif el > 2000 and el <= 3000:
		colr = "green"
	else:
		colr = "orange"

	iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
	fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=folium.Popup(iframe), fill_color=colr, color= 'grey', fill_opacity=.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(), 
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'yellow'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map_html_popup_advanced.html")
