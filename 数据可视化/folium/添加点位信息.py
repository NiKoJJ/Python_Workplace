import folium
m = folium.Map(location=[39.917834, 116.397036], width='100%',height='100%', zoom_control='False',
               tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}&ltype=6',attr='AutoNavi')
tooltip ='请点击我查看该点信息'
folium.Marker([39.937282,116.403187], popup='南锣鼓巷',tooltip=tooltip).add_to(m)
folium.Marker([39.917834,116.397036], popup='故宫',tooltip=tooltip).add_to(m)
folium.Marker([39.928614,116.391746], popup='北海公园', tooltip=tooltip, icon=folium.Icon(color='red')).add_to(m)
folium.Marker([39.942143,116.382590], popup='后海公园', tooltip=tooltip, icon=folium.Icon(color='green', prefix='fa', icon='taxi')).add_to(m)
m.save("first.xml")