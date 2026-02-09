import requests
def getweather(latitude,longitude):
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,  
        "timezone": "auto"       
    }
    response = requests.get(url,params=params,timeout=10)
    data = response.json()
    current_weather = data.get("current_weather",{})
    weacode = current_weather.get("weathercode")
    tem = current_weather.get("temperature")
    day = current_weather.get("is_day")
    return weacode,tem,day

#这个函数借助API获取天气码以及温度，昼夜
#返回天气码，就是weathercode，其他的返回值我抛掉了
def weathercode(weathercode):
    weathercodedz = {
        0 : '晴',
        1 : '多云',
        2 : '少云',
        3 : '阴',
        45 : '雾',
        48 : '冻雾',
        51 : '轻毛毛雨',
        53 : '中毛毛雨',
        55 : '重毛毛雨',
        56 : '轻冻毛毛雨',
        57 : '重冻毛毛雨',
        61 : '小雨',
        63 : '中雨',
        65 : '大雨',
        66 : '轻冻雨',
        67 : '重冻雨',
        71 : '小雪',
        73 : '中雪',
        75 : '大雪',
        77 : '雪粒',
        80 : '小阵雨',
        81 : '阵雨',
        82 : '强阵雨',
        85 : '小阵雪',
        86 : '阵雪',
        95 : '雷雨',
        96 : '轻度雷雨伴有冰雹',
        99 : '重度雷雨伴有冰雹'
    }
    return weathercodedz.get(weathercode,"未知天气")
#解析传来的天气码
#(敲这个字典给我累死了你知道吗)
if __name__ == "__main__":
    latitude1 = float(input("纬度="))
    longitude1 = float(input("经度="))
    cur,temp,dayn = getweather(latitude1,longitude1)
    curdz = weathercode(cur)
    print("当前天气为",curdz,"\n温度大约在",temp,"摄氏度")
    if dayn == 1:
        print("出去看看吧，现在正是美好的白天")
    else:
        print("天黑了，时候已经不早，早点睡觉吧\n晚安")
