import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[35.70387918204649, 139.79352861911002], tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat,lon,elev):
	map.add_child(folium.Marker(location=[lt,ln], popup=str(el)+ " m", icon=folium.Icon(color="blue")))

map.add_child(folium.Marker(location=[35.70387918204649, 139.79352861911002], popup="Good Bar!", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")
