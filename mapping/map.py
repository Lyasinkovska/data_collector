import folium
import json

data = open("mountains.json").read()
lat_list = list()
lon_list = list()
name_list = list()
height_list = list()

js = json.loads(data)
for item in js['features']:
    lat = item['properties']['latitude']
    lon = item['properties']['longitude']
    name = item['properties']['name']
    height = item['properties']['meters']
    lon_list.append(lon)
    lat_list.append(lat)
    name_list.append(name)
    height_list.append(height)

html = """
Mountain name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation <= 1000:
        return "blue"
    elif 1000<elevation<=2000:
        return "green"
    elif 2000<elevation<=3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[49.23, 13.02], zoom_start=4, tiles = "Mapbox Bright")


fgm = folium.FeatureGroup(name = "Mountains")

for lt, ln, nm, el in zip(lat_list, lon_list, name_list, height_list):
    iframe = folium.IFrame(html=html % (nm,nm, el), width=200, height=100)
    fgm.add_child(folium.CircleMarker(location = (lt, ln), radius = 5,popup = folium.Popup(iframe),
                                     color = color_producer(el),fill = True,
                                     fill_color = color_producer(el), fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding = "utf-8-sig").read(),
style_function=lambda x: {'fillColor': "green" if x['properties']['POP2005'] < 10000000
    else "orange" if 10000000 <= x['properties']['POP2005'] < 30000000
    else "pink" if 3000000 <= x['properties']['POP2005'] < 50000000
    else "red" if 50000000 <= x['properties']['POP2005'] < 100000000
    else "black"} ))

map.add_child(fgm)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
print("Map is ready for use")

