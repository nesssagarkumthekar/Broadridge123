import requests
from bs4 import BeautifulSoup
import WFGGLOBAL as Wg

def Search_for_Group(Grpurl,search_name):
    #print('came in side 1 ' + Grpurl)
    resp1 = requests.get(Grpurl)

    if resp1.ok:
        pass
    else:
        print('bad search in group '+ Grpurl)

    soup1 = BeautifulSoup(resp1.text,'lxml')
    found = 'N'

    for member1 in soup1.find('div',attrs={'id':'groupFAs'}).find('ul').find_all('li'):
        names1 = member1.find('a', href=True).text.strip()
        #print(names1)
        #print('came in side '+ Grpurl)
        Wg.All_members.append(names1)


        if search_name[0].upper() in names1 and search_name[1].upper() in names1:
            #print('Group found')
            found = 'Y'

        resp1.close()
        requests.session().close()

    return found










