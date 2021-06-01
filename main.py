import requests
import logging
import csv
import re
import time
import lxml
import pandas as pd
from bs4 import BeautifulSoup
from mechanize import Browser
import WFGSRCHPG as Ws
import WFGGLOBAL as Wg


"""
import mechanize as m
############ Change Log ###########
this pgm is used to open and query wells fargo website for testing purpose


Start_time = time.strftime('%X %x %Z')
print('start time is : ' + Start_time)

######## Mechanize Package Functions to open and query website #############

def process_file(Fullname,Pcode):

"""

#member = [['Tyler', 'Naki'], '89410-5207']
#member = [['Karlynn', 'Quist'], '82801-3904']

def process_file(member):

    Fullname = member[0]
    #print(Fullname)
    Pcode = member[1]

    #print(Pcode)


    br = Browser()  # Set Browser


    br.set_handle_robots(False)  # Ignore robots
    br.addheaders = [('User-agent', 'Firefox')]  # Set user Agent
    br.open('https://www.wellsfargo.com/locator/wellsfargoadvisors/search')  # Set the usr which ypu wish to Open
###
    br.form = list(br.forms())[0]
    br.form['chkFNet'] = False
    br.form['chkBIS'] = False

    br.form['zip5'] = str(Pcode).split('-')[0]
    #br.form['zip5'] = '75201'
    # br.form['zip5'] = '28202'


    search_zip = str(Pcode).split('-')[0]
    # search_zip = '28202'
    search_name = Fullname
    # search_name = ['Tonya','McMahon']


    br.submit()
    soup = BeautifulSoup(br.response().read(), "lxml")

    found_flag = 'N'


    #print(soup.find('div',attrs={'id':'alertBox'}))

    if soup.find('div',attrs={'id':'alertBox'}) != None:
        #print('came inside')
        pass
    else:
        table = soup.find_all('table', attrs={'class': 'generictext'})
        for td in table[0].find_all('td'):
            # print(td)
            # print(td.find('div').find('strong'))
            try:
                url = td.find('div').find('strong').find('a', href=True).get('href')
                # print(url)
                for links in td.find_all('br'):
                    zip = re.sub("(\n)|(\r)|(\t)|(\xa0)|(\n),", "", links.nextSibling)
                    # print(zip)
                    if search_zip in zip:
                        # print('came inside this ')
                        found_flag = Ws.search_page(url, search_name, Pcode)


            except AttributeError:
                pass
            except IndexError:
                pass

            finally:

                if found_flag == 'Y':
                    break


    if found_flag != 'Y':
        #print('member not found ' + search_name[0] + '  ' + search_name[1])

        Wg.Fname_not_found.append(search_name[0])
        Wg.Lname_not_found.append(search_name[1])
        Wg.Zip_not_found.append(Pcode)



# print(hrefs)

    br.close()

"""
df_list = pd.read_html(str(table[0])) # this parses all the tables in webpages to a list
#df = df_list[0]

#df = pd.DataFrame({df_list[0], {'Link' : hrefs[0:]}})



#data1 = {'detail': [df_list] , 'link': [hrefs]}
#df = pd.DataFrame(data1)
df = df_list[0]

#df['Href']=hrefs
df.insert(3,'hrefs',hrefs,False)
#df.insert('href',hrefs,hrefs,True)
df.to_csv('/Users/P7165881/Desktop/Brodridge/products199.csv', index=False, encoding='utf-8')

print('process ended successfully')

tb= time.strftime('%X %x %Z')
print('End time is : ' + tb)


########## this is a must to close the br object
br.close()

"""
#process_file(member)