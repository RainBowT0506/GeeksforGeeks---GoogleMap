# import gmplot package
import gmplot

from Constant import API_Key_Google_Map

latitude_list = [ 30.3358376, 30.307977, 30.3216419 ]
longitude_list = [ 77.8701919, 78.048457, 78.0413095 ]

gmap5 = gmplot.GoogleMapPlotter(30.3164945,
								78.03219179999999, 13,apikey=API_Key_Google_Map)

gmap5.scatter( latitude_list, longitude_list, '# FF0000',
								size = 40, marker = False)

# polygon method Draw a polygon with
# the help of coordinates
gmap5.polygon(latitude_list, longitude_list,
				color = 'cornflowerblue')

gmap5.draw( "map15.html" )
