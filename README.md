實作了文章 [GeeksforGeeks - Python | Plotting Google Map using gmplot package](https://www.geeksforgeeks.org/python-plotting-google-map-using-gmplot-package/)

Github：[GeeksforGeeks-GoogleMap](https://github.com/RainBowT0506/GeeksforGeeks-GoogleMap)

使用 `gmplot` 套件在 Python 中繪製 Google 地圖的功能。
`gmplot` 提供了一個類似於 Matplotlib 的介面，用於生成在 Google 地圖上顯示所有數據所需的 HTML 和 JavaScript。

### 程式碼 #1: 創建基本地圖
創建一個基本地圖，設定中心點的緯度、經度，並將地圖保存為 HTML 文件。
![map11](https://github.com/RainBowT0506/GeeksforGeeks-GoogleMap/assets/109667537/9779999c-9f16-466a-85ef-9b6bbb1d32bf)

### 程式碼 #2: 另一種創建基本地圖的方法
使用地理編碼的方式來創建基本地圖。
![map12](https://github.com/RainBowT0506/GeeksforGeeks-GoogleMap/assets/109667537/5a06428a-2835-4c85-8634-410c36ef0604)

### 程式碼 #3: 在 Google 地圖上繪製散點和連線
在 Google 地圖上繪製了散點並連線。
![map13](https://github.com/RainBowT0506/GeeksforGeeks-GoogleMap/assets/109667537/b8a279ed-724d-425e-a796-79a233b9328f)

### 程式碼 #4: 顯示熱度圖
創建了一個顯示熱度圖的地圖。
![map14](https://github.com/RainBowT0506/GeeksforGeeks-GoogleMap/assets/109667537/f8250d15-c966-47c0-b29a-c0842e8df9a3)

### 程式碼 #5: 在 Google 地圖上繪製多邊形
在 Google 地圖上繪製了多邊形。
![map15](https://github.com/RainBowT0506/GeeksforGeeks-GoogleMap/assets/109667537/3c9d7218-9a9c-4e07-aaa0-f2e6d2bd9e2e)

### 專業術語
1. `gmplot` 包：提供了類似於 Matplotlib 的介面，用於生成在 Google 地圖上顯示數據所需的 HTML 和 JavaScript。
2. `GoogleMapPlotter`：`gmplot` 包中的類，用於創建 Google 地圖的基本繪圖對象。
3. `scatter` 方法：在 Google 地圖上散點表示的方法，可用於標記特定的地理位置。
4. `plot` 方法：用於在 Google 地圖上繪製連線（線段）的方法。
5. `heatmap` 方法：繪製 Google 地圖上的熱度圖，顯示數據點的熱度分佈。
6. `polygon` 方法：在 Google 地圖上繪製多邊形的方法，通常用於標記區域或邊界。
7. `draw` 方法：將生成的地圖保存為 HTML 文件的方法。
8. `latitude_list` 和 `longitude_list`：包含緯度和經度數據的列表，表示地理位置的坐標點。
9. `from_geocode` 方法：從地名或位置名稱獲取其緯度和經度坐標的方法。
10. `edge_width`：在地圖上繪製線條時的線寬。
11. `size`：在地圖上散點表示時的點的大小。
12. `marker`：控制是否在地圖上的散點處繪製標記點。
13. HTML 文件：通過 `draw` 方法生成的文件，其中包含了在 Google 地圖上顯示數據所需的 HTML 和 JavaScript 代碼。


----

實作了文章　[Python Bokeh – Plot for all Types of Google Maps ( roadmap, satellite, hybrid, terrain)](https://www.geeksforgeeks.org/python-bokeh-plot-for-all-types-of-google-maps-roadmap-satellite-hybrid-terrain/)

Github：[GeeksforGeeks-GoogleMap](https://github.com/RainBowT0506/GeeksforGeeks-GoogleMap)

使用 Bokeh 庫在 Python 中創建顯示不同類型 Google 地圖（道路地圖、衛星、混合、地形）的程式碼片段。這對於希望將 Google 地圖整合到 Bokeh 可視化中的人來說是一個有用的指南。

以下是每種地圖類型的簡要摘要：
### 道路地圖（Roadmap）：
使用 Bokeh 創建一個顯示 Google 地圖路線圖的互動式視覺化。路線圖是一種適合在車輛中導航區域的地圖，地形被平滑，道路被突顯。預設地圖類型。
![Roadmap](https://hackmd.io/_uploads/Hy5SQzguT.png)

### 衛星（Satellite）：
使用 Bokeh 創建顯示 Google 地球衛星圖的互動式視覺化。衛星圖是一種鳥瞰圖，不包含任何圖形。
![Satellite](https://hackmd.io/_uploads/Hkd9mflup.png)

### 混合（Hybrid）：
使用 Bokeh 中創建顯示 Google 地圖混合視圖的互動式視覺化。混合圖將衛星圖與道路圖形結合在一起。
![Hybrid](https://hackmd.io/_uploads/SJN3XGeOa.png)

### 地形（Terrain）：
使用　Bokeh 中創建顯示 Google 地圖地形信息的互動式視覺化。
![Terrain](https://hackmd.io/_uploads/SJ8J4Gl_p.png)

## 專業術語
1. **Bokeh:** Bokeh 是一個用於製作交互式資料視覺化的 Python 函式庫，它使用 HTML 和 JavaScript 在現代瀏覽器中呈現圖表。
2. **gmap():** `gmap` 是 Bokeh 中的一個函數，用於顯示 Google 地圖。
3. **GMapOptions:** `GMapOptions` 是 Bokeh 中的一個模型，用於配置 Google 地圖的選項，例如地圖類型、座標和縮放級別。
4. **output_file:** `output_file` 函數用於指定將 Bokeh 圖表保存到的 HTML 文件的名稱。
5. **show():** `show` 函數用於顯示 Bokeh 圖表。
6. **Google Maps API Key:** Google 地圖 API 金鑰是一個用於訪問 Google 地圖 API 服務的安全金鑰。
7. **地圖類型 (map_type):** 地圖類型表示 Google 地圖的不同視圖，包括 "roadmap"（路線圖）、"satellite"（衛星圖）、"hybrid"（混合圖）和 "terrain"（地形圖）。
8. **座標 (lat, lng):** 緯度（latitude）和經度（longitude）是用來指定地圖中心點的座標。
9. **縮放級別 (zoom):** 縮放級別表示地圖的縮放程度，可以根據需要調整。
10. **HTML 文件輸出 (output_file):** `output_file` 函數用於指定 Bokeh 圖表的 HTML 文件輸出位置。
