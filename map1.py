import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[35.70387918204649, 139.79352861911002], tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat,lon):
	map.add_child(folium.Marker(location=[lt,ln], popup="Hi, I'm a Marker", icon=folium.Icon(color="blue")))

for coordinates in [[35.70387918204649, 139.79352861911002]]:
	map.add_child(folium.Marker(location=coordinates, popup="Good Bar!", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")
