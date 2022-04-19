import requests
from bs4 import BeautifulSoup
import pickle
import matplotlib.pyplot as plt

main_url = 'https://sgulyano.github.io/eval/'
html_url = ['87385371.html',
            '87545994.html',
            '57138607.html',
            '98742007.html',
            '33737452.html',
            '58806234.html',
            '90151389.html']
eval_url = [main_url + url for url in html_url]

def get_table_data(item):
    data = []
    table_body = item.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

all_info = []
all_ratings = []

for url in eval_url:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tables = soup.find_all("table")

    all_info.append(get_table_data(tables[0]))
    all_ratings.append(get_table_data(tables[2]))
data = (all_info, all_ratings)


def timeline ():
    time = []
    for i in range(len(html_url)):
        time.append([data[0][i][2][1], i])
    return time

test = timeline()
timelines = (sorted(test ,key=lambda x: x[0].split("/")[::-1]))


def classtify (datas, html_point):
    classs = []
    point = []
    for j in datas:
        ht = j[1]
        classs.append(data[0][ht][html_point][1])
        point.append([data[0][ht][html_point][1], ht])

    result = []
    results = []
    for check in list(dict.fromkeys(classs)):
        for num, checker in enumerate(classs):
            if check == checker:
                result.append(point[num])
        results.append(result) ; result = []
    return results






def sec_class (inp):
    classs = []
    point = []
    result = []
    mem = []
    for ia in inp:
        for sec in ia:
            html_point = sec[1]
            classs.append(data[0][html_point][1][1])
            point.append([data[0][html_point][1][1], sec[1]])
        
        for checker in list(dict.fromkeys(classs)):
            for num ,check in enumerate(classs):
                if checker == check:
                    mem.append(point[num])

        result.append(mem) ; mem = []
        classs = []
        point = []
    return(result)
    

b = classtify(timelines, 0)
a = (sec_class(b))



in1 = []
in2 = []
for i in a:
    for j in i:
      in1.append(data[0] [j[1]] [0] [1])
      in2.append(data[0] [j[1]] [2] [1])
print(in1)
print(in2)

plt.plot(in2,in1,'--ro')
plt.show()





