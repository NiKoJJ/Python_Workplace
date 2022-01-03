from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

c = (
    Map()
    .add("商家B", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    .render("map_base.html")
)

# d=(
#     Map()
#     .add("Animal",[list(z) for z in zip(Faker.provinces,Faker.animal)],"china")
#     .set_global_opts(title_opts=opts.TitleOpts("中国省份动物概要"))
#     .render("My_first_test.html")
# )