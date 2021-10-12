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


fg = folium.FeatureGroup(name = "My Map")
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
	fg.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=folium.Popup(iframe), fill_color=colr, color= 'grey', fill_opacity=.7))

map.add_child(fg)
map.save("Map_html_popup_advanced.html")
