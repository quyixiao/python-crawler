import requests
from bs4 import BeautifulSoup
from lxml.doctestcompare import strip

url = 'https://my.oschina.net/'
headers = {
    'Host': "www.oschina.net",
    'Connection': "keep-alive",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'X-DevTools-Emulate-Network-Conditions-Client-Id': "a638e770-f2be-4986-8ddb-2b40d75f5abd",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon / 5.0 Chrome / 55.0.2883.75 Safari / 537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'DNT': "1",
    'Referer': "https://www.oschina.net/home/login",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN",
    'Cookie': "_user_behavior_=e82d45a4-6ffe-4777-ae78-97a28fd6ba4c; __gads=ID=0fe160476b5f3f41:T=1582644586:S=ALNI_MY9q1Pl7C4wofG_JQf3TuEf5Nh-7A; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1582644586,1582687514; _reg_key_=UN65J2Sftyb5P5csJHPx; oscid=lvanICoCqxw3F1O6YJRgC%2F0fPtfGsGzERFnV3rf5WXfJyAeTPvGMAtBOhANYc%2FXQc%2FVm492r%2FpQ7OumToptvB%2B%2FLlXxyGyDLTg8v7TdXBqt1wJ2REFT1Y4uhUr3k4%2BeCs5jYwOcuTlFpSIvsYn4Mw2%2FKGX%2BBVpaT6wjL1FTgO0c%3D; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1582687620",
}


response = requests.request("GET", url, headers=headers)
text = response.text
soup = BeautifulSoup(text, 'lxml')
ele = soup.find(id="userSidebar")

a = ele.img.get('src')
print(a)

with response:
    with open('profile.html', 'w', encoding='utf-8') as f:
        text = response.text
        f.write(text)
        #print(text)  # 搜索 user-inf
        #print(response.status_code, '~~~~~~~~~~~~~~~~~~~~')
