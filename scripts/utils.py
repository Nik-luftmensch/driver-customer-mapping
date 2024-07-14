import h3
import requests
import polyline

def index_positions(positions, resolution=9):
    for pos in positions:
        pos['h3_index'] = h3.geo_to_h3(pos['lat'], pos['lon'], resolution)
    return positions

def find_nearest_driver(customer, drivers):
    min_distance = float('inf')
    nearest_driver = None
    
    for driver in drivers:
        distance = h3.h3_distance(customer['h3_index'], driver['h3_index'])
        if distance < min_distance:
            min_distance = distance
            nearest_driver = driver
            
    return nearest_driver, min_distance

def get_route(start, end):
    url = f"http://router.project-osrm.org/route/v1/driving/{start[1]},{start[0]};{end[1]},{end[0]}?overview=full"
    response = requests.get(url)
    data = response.json()
    route = data['routes'][0]['geometry']
    return polyline.decode(route)
