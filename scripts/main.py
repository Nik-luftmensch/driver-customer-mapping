import h3
import folium
from geopy.distance import geodesic
from folium.plugins import MarkerCluster
import requests
import polyline
from utils import index_positions, find_nearest_driver, get_route  # Adjusted import to use relative path
import json

# Load drivers and customer data
drivers = [
    {"name": "Driver 1", "lat": 40.712776, "lon": -74.005974},
    {"name": "Driver 2", "lat": 40.706446, "lon": -74.009443},
    {"name": "Driver 3", "lat": 40.730610, "lon": -73.935242},
    {"name": "Driver 4", "lat": 40.758896, "lon": -73.985130},
    {"name": "Driver 5", "lat": 40.741895, "lon": -73.989308}
]

customer = {"name": "Customer", "lat": 40.748817, "lon": -73.985428}

# Index positions with H3
drivers = index_positions(drivers)
customer = index_positions([customer])[0]

# Find the nearest driver
nearest_driver, h3_distance = find_nearest_driver(customer, drivers)

# Calculate geodesic distance
customer_location = (customer['lat'], customer['lon'])
nearest_driver_location = (nearest_driver['lat'], nearest_driver['lon'])
geodesic_distance = geodesic(customer_location, nearest_driver_location).kilometers

print(f"The nearest driver is {nearest_driver['name']}")
print(f"H3 Distance: {h3_distance}")
print(f"Geodesic Distance: {geodesic_distance:.2f} km")

# Get route coordinates
route_coords = get_route(customer_location, nearest_driver_location)

# Visualize on map
m = folium.Map(location=[customer['lat'], customer['lon']], zoom_start=14, tiles='OpenStreetMap')

# Add customer marker
folium.Marker([customer['lat'], customer['lon']], popup=customer['name'], icon=folium.Icon(color='red', icon='user')).add_to(m)

# Add driver markers with clustering
marker_cluster = MarkerCluster().add_to(m)
for driver in drivers:
    icon_color = 'green' if driver == nearest_driver else 'blue'
    folium.Marker([driver['lat'], driver['lon']], popup=f"{driver['name']}<br>Lat: {driver['lat']}<br>Lon: {driver['lon']}", icon=folium.Icon(color=icon_color, icon='car')).add_to(marker_cluster)

# Add route between the customer and the nearest driver
folium.PolyLine(route_coords, color='blue', weight=5, opacity=0.7).add_to(m)

# Add distance information
folium.Marker(
    [(customer['lat'] + nearest_driver['lat']) / 2, (customer['lon'] + nearest_driver['lon']) / 2],
    popup=f"Distance: {geodesic_distance:.2f} km",
    icon=folium.DivIcon(html=f"<div style='font-size: 12pt; color: black; background-color: white; padding: 5px;'>{geodesic_distance:.2f} km</div>")
).add_to(m)

# Add legend
legend_html = '''
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 150px; height: 120px; 
            border:2px solid grey; z-index:9999; font-size:14px;
            background-color: white; padding: 10px;">
&emsp;<b>Legend</b><br>
&emsp;<i class="fa fa-user" style="color:red"></i>&emsp;Customer<br>
&emsp;<i class="fa fa-car" style="color:green"></i>&emsp;Nearest Driver<br>
&emsp;<i class="fa fa-car" style="color:blue"></i>&emsp;Driver<br>
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
m.save('map_advanced.html')
