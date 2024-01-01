# importing the required modules
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.io import output_file, show

from geopy.geocoders import GoogleV3  # 新增 geopy
from Constant import API_Key_Google_Map

# file to save the model
output_file("RoadmapTaichung.html")

# 使用 geopy 進行地址轉換
geolocator = GoogleV3(api_key=API_Key_Google_Map)
location_address = '台中市'
location = geolocator.geocode(location_address)

# 檢查結果
if location:
    lat = location.latitude
    lng = location.longitude
else:
    print("找不到該地址的經緯度坐標。")
    lat, lng = 0, 0  # 若找不到，設定一個預設值或提醒使用者

# configuring the Google map
map_type = "roadmap"
zoom = 12
google_map_options = GMapOptions(lat=lat, lng=lng, map_type=map_type, zoom=zoom)

title = "Taichung"
google_map = gmap(API_Key_Google_Map, google_map_options, title=title)

# displaying the model
show(google_map)
