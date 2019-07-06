import  requests



def getcode(address):
    parameters = {'address':address,'key':'CCYbQQuASeGazRVTZGSkPDANEbbwwXEF'}
    a = 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&address='+str(address)
    response = requests.get(a,parameters)
    info_site = response.json()
    lng = float(info_site['result']['location']['lng'])  # 经度 Longitude  简写Lng
    lat = float(info_site['result']['location']['lat'])

    return  lng,lat

if __name__ == '__main__':
    address = '上海'
    print(getcode(address))
    print(getcode("上海迪士尼"))

