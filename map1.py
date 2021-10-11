import folium

map = folium.Map(location=[35.70387918204649, 139.79352861911002], tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
map.add_child(folium.Marker(location=[35.70387918204649, 139.79352861911002], popup="Good Bar!", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")
