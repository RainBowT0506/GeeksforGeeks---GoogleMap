# import gmplot package
import gmplot

from Constant import API_Key_Google_Map

# from_geocode method return the
# latitude and longitude of given location .
gmap2 = gmplot.GoogleMapPlotter.from_geocode("Dehradun, India", apikey=API_Key_Google_Map)
gmap2.draw("map12.html")
