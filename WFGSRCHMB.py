import requests
from bs4 import BeautifulSoup
import re
import WFGGLOBAL as Wg

def search_member(Memurl):
    resp = requests.get(Memurl)

    if resp.ok:
        pass
    else:
        print('error from search member')

    soup = BeautifulSoup(resp.text,"lxml")

    try:
        name = soup.find('div',attrs:={'id':'nameTitle'}).find('h1').text.strip()
    except AttributeError:
        name = soup.find('div', attrs := {'id': 'nameTitle'}).find('script').contents[0].split('<h1>')[1].split('</h1>')[0]

    if ',' in name:
        name = name.split(',')[0]

    Wg.Name_A.append(name)
    #designation = soup.find('div', attrs := {'id': 'nameTitle'}).find('h2').text.strip()
    #print(soup.find('div', attrs := {'id': 'nameTitle'}).find_all('h2').text.strip())

    try:
        designation = soup.find('div',attrs:={'id':'nameTitle'}).find_all('h2')[1].text.strip()
    except IndexError:
        try:
            designation = soup.find('div', attrs := {'id': 'nameTitle'}).find_all('h2')[0].text.strip()
        except AttributeError:
            designation = ' '

    Wg.Des_A.append(designation)
    Wg.Link_A.append('')
    #Wg.Group_A.append('')
    Address_tag = soup.find('div',attrs:={'id': 'address'})

    ph2=''
    for lines in Address_tag.select('strong'):
    #print(lines.text)
    #print(lines.nextSibling)
        if 'Phone' in lines.text:
            ph=lines.nextSibling.strip()
            ph1 = re.sub("(\n)|(\r)|(\t)|(\xa0)|(\n),", "", ph)
            ph2 = ph1.replace('|', ',').replace('                                                ', '').replace(
                '               ', '')


    if ph2 != '':
        Wg.Phone_A.append(ph2)
    else:
        Wg.Phone_A.append(' ')

    try:
        email = Address_tag.find('a',href=True).get('href').split(':')[1]
    except AttributeError:
        email = ''

    Wg.Email_A.append(email)






