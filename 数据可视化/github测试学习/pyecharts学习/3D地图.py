from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType

China_base=(
    Map3D(init_opts=opts.InitOpts(width="1080px",height="900px",page_title="三维中国地图"))
    .add_schema(
        maptype='world',
        name='中国',
        box_width=100,  # 组件宽度
        box_depth=None,  # 组件深度，组件深度默认自动，保证三维组件的显示比例跟输入的 GeoJSON 的比例相同。
        box_height=10,  # 组件深度
        region_height=3,  # 模型高度<boxheight, boxheight-regionheight 这片区域被用于柱状图散点图的展示
        is_show_ground=True,  # 是否显示地面
        ground_color="#aaa",  # 地面颜色
        environment='#BEBEBE',  # 环境贴图
        map3d_label=opts.Map3DLabelOpts(is_show=True),  # 标签
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(0,139,139)",
            border_color="rgb(192,255,62)",  # 描边颜色
            border_width=0.8,  # 描边宽度
            opacity=0.8  # 图形透明度
        ),
        # 光照设置 合理的光照设置能够让整个场景的明暗变得更丰富，更有层次。
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            is_main_shadow=True,
            main_alpha=55,
            main_beta=10,
            main_intensity=1.2,
            ambient_intensity=0.3,
        )

    )
    .add(
        "china",
        "",
        maptype=ChartType.MAP3D,
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="China/World-3D地图绘制",title_link="https://www.nikojj.top"),
        visualmap_opts=opts.VisualMapOpts(is_show=True), # 视觉映射
        tooltip_opts=opts.TooltipOpts(
            is_show=True,trigger='item',trigger_on='mousemove|click') # 提示框配置
    )
    .render("3DMap-China.html")
)
