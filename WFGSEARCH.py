import requests
import csv
import re
import time
import lxml

from bs4 import BeautifulSoup
from mechanize import Browser
import WFGSRCHPG as Ws




def process_file(member):

    Fullname = member[0]
    print(Fullname)
    Pcode = member[1]
    print(Pcode)

    br = Browser()  # Set Browser

    br.set_handle_robots(False)  # Ignore robots
    br.addheaders = [('User-agent', 'Firefox')]  # Set user Agent
    br.open('https://www.wellsfargo.com/locator/wellsfargoadvisors/search')  # Set the usr which ypu wish to Open
###
    br.form = list(br.forms())[0]
    br.form['chkFNet'] = False
    br.form['chkBIS'] = False

    br.form['zip5'] = Pcode
    #br.form['zip5'] = '75201'
    # br.form['zip5'] = '28202'

    search_zip = Pcode
    # search_zip = '28202'
    search_name = Fullname
    # search_name = ['Tonya','McMahon']

    br.submit()
    soup = BeautifulSoup(br.response().read(), "lxml")
    table = soup.find_all('table', attrs={'class': 'generictext'})

    found_flag = 'N'
    for td in table[0].find_all('td'):
        # print(td)
        # print(td.find('div').find('strong'))
        try:
            url = td.find('div').find('strong').find('a', href=True).get('href')

            for links in td.find_all('br'):
                zip = re.sub("(\n)|(\r)|(\t)|(\xa0)|(\n),", "", links.nextSibling)
                if search_zip in zip:
                    found_flag = Ws.search_page(url, search_name)


        except AttributeError:
            pass

        finally:

            if found_flag == 'Y':
                break

    if found_flag != 'Y':
        print('member not found')



    br.close()


