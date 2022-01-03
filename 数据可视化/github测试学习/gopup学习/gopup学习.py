import gopup as gp
covid_163_df = gp.covid_163(indicator="全球所有国家及地区累计数据")
covid_163_df.to_csv('cov_data.csv',encoding='GBK')

# import gopup as gp
# covid_163_df = gp.covid_163(indicator="中国实时数据")
# print(covid_163_df)

# import folium
# m=folium.Map(location=[104.07,30.67],width=600,height=600,zoom_start=12)
