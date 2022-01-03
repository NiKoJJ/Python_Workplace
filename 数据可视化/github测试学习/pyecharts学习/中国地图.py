from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType

# --------------------------------------迁徙地图-------------------------------------#
provience_dis = {"广州": (113.27, 23.13), "北京": (116.40, 39.90), "新疆": (87.62, 43.82),
                 "安徽": (117.25, 31.83), "成都": (104.07, 30.67)}
list_key = list(provience_dis.keys())
list_value = list(provience_dis.values())
# 利用zip()函数生成由 <元组> 组成的 <列表>,list(z)为一个个元组，最后注意要加上[]成为列表
data_pro = [list(z) for z in zip(list_key, list_value)]
print(data_pro)

migrate = (
    Geo(init_opts=opts.InitOpts(width="1500px", height='1200px', page_title="成都人口流向图"))  # 初始化配置
        # 基本框架设置 参考 pyecharts-document-Geo
        .add_schema(maptype="china",
                    is_roam=True,  # 开启鼠标缩放
                    zoom=1,  # 当前视角比例缩放
                    center=[104.06, 30.67],  # 当前视角的中心点 经纬度表示
                    layout_size=500,
                    itemstyle_opts=opts.ItemStyleOpts(color="#FFFFCC", border_color="#800000"))
        # 为地图添加配置
        # 标注散点
        .add(
        "",  # series name
        # 添加数据项（坐标点名称，坐标点值）
        # data_pro,
        [("广州", (113.27, 23.13)), ("北京", (116.40, 39.90)), ("安徽", (117.25, 31.83)),
         ("新疆", (87.62, 43.82)), ("成都", (104.07, 30.67))],
        type_=ChartType.EFFECT_SCATTER,  # 添加图类型
        color="black"
    )
        # 标记流向线条
        .add(
        'Geo',  # series_name
        [("成都", "新疆"), ("成都", "北京"), ("成都", "安徽"), ("成都", "广州")],
        type_=ChartType.LINES,
        is_selected=True,  # 图例
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=6, color="blue"),  # 添加效果 箭头arrow
        linestyle_opts=opts.LineStyleOpts(curve=0.2)
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))  # 系列配置项
        .set_global_opts(title_opts=opts.TitleOpts(title="成都人口流向图"))  # 全局配置项
        .render('migrate.html')
)

# --------------------------------------世界地图-------------------------------------#
world = (
    Map(init_opts=opts.InitOpts(width="1500px", height="900px", page_title="世界地图——NiKOJJ"))  # 初始化配置
        .add(
        "世界地图",
        data_pair=[("China", 95.1), ("Canada", 23.2),
                   ("Brazil", 43.3), ("Russia", 66.4), ("Britain", 11.0),
                   ("United States", 88.5), ("Greenland", 60.0), ("Germany", 10.27,),
                   ("Australia", 150.53), ("South Africa", 17.33), ("Italy", 41.54)],
        maptype="world",
        is_roam=True,
        is_selected=True,
        is_map_symbol_show=True,  # 是否显示标记图形
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="MAP-世界地图"),
        visualmap_opts=opts.VisualMapOpts(is_show=True),  # 视觉映射配置项
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))  # 是否显示标签
        .render('MAP-WORLD.html')

)

# --------------------------------------中国地图-------------------------------------#
China = (
    Map(init_opts=opts.InitOpts(width="1500px", height="900px", page_title="中国地图—NiKoJJ"))
        .add(
        "中国地图",
        [("广东", (113.27, 23.13)), ("北京", (116.40, 39.90)), ("安徽", (117.25, 31.83)),
         ("新疆", (87.62, 43.82)), ("四川", (104.07, 30.67)), ('江苏', (180.12, 30.67))],
        maptype="china",
        is_roam=True,  # 鼠标缩放
        is_selected=True,  # 图例

    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-中国地图"),
        visualmap_opts=opts.VisualMapOpts(is_show=True, max_=200)
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .render('Map-China.html')
)

# --------------------------------绘制省市地图----------------------------- #
city1 = ['宿州市', '合肥市', '芜湖市', '六安市', '安庆市', '马鞍山市', '宣城市', '黄山市',
         '淮南市', '蚌埠市', '滁州市', '亳州市', '阜阳市', '淮北市', '池州市', '铜陵市']
city2 = ['南京市', '扬州市', '苏州市', '南京市', '徐州市', '南通市', '泰州市', '无锡市', '镇江市',
         '常州市', '淮安市', '连云港市', '宿迁市', '张家港市', '昆山市', '高邮市', '靖江市', '常熟市', '盐城市']
values1 = [10, 40, 45, 50, 67, 80, 100, 115, 130, 140, 155, 165, 175, 30, 90, 190]
value2 = [5, 10, 18, 25, 32, 39, 41, 49, 53, 62, 67, 70, 76, 83, 89, 91, 94, 99]
data_anhui = [list(z) for z in zip(city1, values1)]
data_jiangsu = [list(z) for z in zip(city2, value2)]

anhui_flink = "https://baike.baidu.com/item/%E5%AE%89%E5%BE%BD/37014"  # 副标题
anhui_zlink = "https://zh.wikipedia.org/wiki/%E5%AE%89%E5%BE%BD%E7%9C%81"  # 主标题

provience_anhui = (
    Map(init_opts=opts.InitOpts(width="1500px", height="900px", page_title='安徽省地图-NiKoJJ'))
        .add(
        '安徽',
        data_anhui,
        maptype='安徽',
        is_roam=True,
        is_selected=True,
        is_map_symbol_show=True  # 是否标记图形
    )
        #####
        # 注：这里添加两个省份的地图的话，会相互覆盖一部分，所以这里将江苏省的注释掉了
        ####
        # .add(
        #     '江苏',
        #     data_jiangsu,
        #     maptype='江苏',
        #     is_roam=True,
        #     is_selected=Truef
        # )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-安徽省地图",
                                  title_link=anhui_zlink,  # 主标题跳转链接
                                  title_target="blank",  # 新窗口打开
                                  subtitle="安徽省市地图",  # 副标题
                                  subtitle_link=anhui_flink,
                                  subtitle_target="self"),  # 当前窗口打开

        visualmap_opts=opts.VisualMapOpts(is_show=True,  # 视觉映射配置
                                          max_=200,
                                          is_calculable=True,  # 是否显示拖拽用的手柄
                                          is_piecewise=True,  # 是否为分段型
                                          range_text=["High", "Low"],
                                          border_color="#000"),  # 两端文本

        tooltip_opts=opts.TooltipOpts(trigger="item",  # 触发类型
                                      trigger_on="mousemove|click",  # 提示框的触发条件
                                      formatter="{b}:{c} (权重)")  # 标签内容格式，这里采用的字符串模板
    )
        .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True)
    )
        .render('provience_安徽.html')
)
