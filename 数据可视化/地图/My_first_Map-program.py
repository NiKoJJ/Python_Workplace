from pyecharts import options as opts
from pyecharts.charts import Map  # 地图
from pyecharts.faker import Faker
from pyecharts.charts import Geo  # 地理坐标系

geo=(
    Map()
    .add("商家",data_pair=[list(z) for z in zip(Faker.country,Faker.values(2,1000))],maptype="china")
    .set_global_opts(title_opts=opts.TitleOpts("版图"))
    .render("My_first_Map.html")
)
