# import gmplot package
import gmplot

from Constant import API_Key_Google_Map

# GoogleMapPlotter return Map object
# Pass the center latitude and
# center longitude
gmap1 = gmplot.GoogleMapPlotter(30.3164945,
								78.03219179999999, 13 ,apikey=API_Key_Google_Map)

# Pass the absolute path
gmap1.draw("map11.html")
