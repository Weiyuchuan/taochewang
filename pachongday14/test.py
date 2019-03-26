import re
import requests
from lxml import etree


url="https://beijing.taoche.com/all/"

all = requests.get(url=url).text
tree = etree.HTML(all)

CITY_CODE=[]
CAR_CODE_LIST=[]

CAR_CODE_list =tree.xpath('//div[@class="header-city-province-mian"]/ul/li')

for i in CAR_CODE_list:
   all = i.xpath('.//div[@class="header-city-province-text"]/a/@href')

   for j in all:
       city = re.findall(r'//(.*?)\.taoche.com',j)

       CITY_CODE.append(city[0])
print(CITY_CODE)

CAR_CODE_list1 =tree.xpath('//div[@id="brandMoreDiv"]/ul')[2:-1]

for q in CAR_CODE_list1:
    all = q.xpath('./li/a/@href')
    for w in all:
        car = re.findall(r'/(.*?)/',w)
        CAR_CODE_LIST.append(car[0])
print(CAR_CODE_LIST)

with open("city.py",'a')as fp:
    fp.write('CITY_CODE'+'='+str(CITY_CODE)+'\n')
    fp.write('CAR_CODE_LIST'+'='+str(CAR_CODE_LIST))


