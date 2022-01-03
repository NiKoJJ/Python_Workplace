import pyecharts.options as opts
from pyecharts.charts import MapGlobe
from pyecharts.faker import POPULATION

data = [x for _, x in POPULATION[1:]]

Globe_World=(
    MapGlobe(init_opts=opts.InitOpts(
        width="1500px",height="900px",
        page_title="人口-world",bg_color="#00BFFF"))
    .add_schema()
    .add(
        maptype="world",
        series_name="世界人口地图",
        data_pair=POPULATION[1:],
        is_map_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
        is_roam=True,
        tooltip_opts=opts.TooltipOpts(
            is_show=True,trigger="item",
            trigger_on="mousemove|click"),

    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            type_="color",
            min_=min(data),
            max_=max(data),
            is_calculable=True,  # 显示拖拽的手柄
            # is_piecewise=True,  # 分段类型 不生效
            border_color="rgb(105,105,105)",
            range_color=["SeaGreen","Aquamarine","DarkRed"],
        )
    )
    .render('Globe_World.html')
)

