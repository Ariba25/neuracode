from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to fetch data from Overpass API
def fetch_overpass_data():
    overpass_url = "http://overpass-api.de/api/interpreter"
    
    overpass_query = """
    [out:json];
    node(around:1000, 40.748817, -73.985428);  # Query for nodes within 1km of a specific lat, lon
    out;
    """
    
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    return data

@app.route('/')
def home():
    overpass_data = fetch_overpass_data()

    locations = []
    for element in overpass_data['elements']:
        if 'lat' in element and 'lon' in element:
            locations.append({
                'lat': element['lat'],
                'lon': element['lon'],
            })

    return render_template('index.html', locations=locations)

if __name__ == '__main__':
    app.run(debug=True)
