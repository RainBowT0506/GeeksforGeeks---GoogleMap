# importing the required modules
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.io import output_file, show

from Constant import API_Key_Google_Map

# file to save the model
output_file("Satellite.html")

# configuring the Google map
lat = 30.3165
lng = 78.0322
map_type = "satellite"
zoom = 12
google_map_options = GMapOptions(lat = lat,
								lng = lng,
								map_type = map_type,
								zoom = zoom)

title = "Dehradun"
google_map = gmap(API_Key_Google_Map,
				google_map_options,
				title = title)

# displaying the model
show(google_map)
