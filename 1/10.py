main_url = 'https://sgulyano.github.io/eval/'
html_url = ['90151389.html',
            '63740399.html']
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
    
def alphabet ():
    classs = []
    point = []
    for j in range(len(html_url)):
        classs.append(data[0][j][0][1])
        point.append([data[0][j][0][1], j])

    test = []
    results = []
    for check in list(dict.fromkeys(classs)):
        for num, checker in enumerate(classs):
            if check == checker:
                test.append(point[num])
        results.append(test) ; test = []
    return results


b = alphabet()
    
w1 = []
w2 = []
w3 = []
w4 = []

for i in b:
    for j in i:

        w1.append(data[0] [j[1]] [1][1])
        w2.append(float(data[1] [j[1]] [12][2]))
        w3.append(float(data[1] [j[1]] [23][2]))
        w4.append(float(data[1] [j[1]] [30][2]))

fig, axes = plt.subplots(nrows=1,ncols=3,figsize=(20,5))


axes[0].set_title("tqkcxncfqb (2563) \n PART 1", color='#000066', fontsize = 14)
bary = axes[0].bar(w1, w2, color='#ADD8E6', width = 0.5)
axes[0].set_xlabel('Section', color = '#4682B4', fontsize = 12)
axes[0].set_ylabel('Percentage of Assessment Level 5', color = '#4682B4', fontsize = 12)

axes[1].set_title("tqkcxncfqb (2563) \n PART 2", color='#000066', fontsize = 14)
axes[1].bar(w1, w3, color='#ADD8E6', width = 0.5)
axes[1].set_xlabel('Section', color = '#4682B4', fontsize = 12)
axes[1].set_ylabel('Percentage of Assessment Level 5', color = '#4682B4', fontsize = 12)

axes[2].set_title("tqkcxncfqb (2563) \n PART 3", color='#000066', fontsize = 14)
axes[2].bar(w1, w4, color='#ADD8E6', width = 0.5)
axes[2].set_xlabel('Section', color = '#4682B4', fontsize = 12)
axes[2].set_ylabel('Percentage of Assessment Level 5', color = '#4682B4', fontsize = 12)

for bar in bary:
  height = bar.get_height()
  label_x_pos = bar.get_x() + bar.get_width() / 2
  ax.text(label_x_pos, height, s=f'{height}', ha='center',va='bottom')

plt.tight_layout()