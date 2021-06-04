import re
from bs4 import BeautifulSoup
from mechanize import Browser
import WFGSRCHPG as Ws
import WFGGLOBAL as Wg


"""
############ Change Log ###########
This pgm is used to open and query wells fargo website for testing purpose




"""

#member = [['Tyler', 'Naki'], '89410-5207']
#member = [['Matthew', 'Noble'], '43017-2950']
#member = [['Matthew','Lowe'],'75225-6330']
#member = [['Richard','Barry'],'95403-5738']

def process_file(member):

    Fullname = member[0]
    #print(Fullname)
    Pcode = member[1]

    #print(Pcode)


    br = Browser()  # Set Browser


    br.set_handle_robots(False)  # Ignore robots
    br.addheaders = [('User-agent', 'Firefox')]  # Set user Agent
    br.open('https://www.wellsfargo.com/locator/wellsfargoadvisors/search')
###
    br.form = list(br.forms())[0]
    br.form['chkFNet'] = False
    br.form['chkBIS'] = False

    br.form['zip5'] = str(Pcode).split('-')[0]
    search_zip = str(Pcode).split('-')[0]
    search_name = Fullname



    br.submit()
    soup = BeautifulSoup(br.response().read(), "lxml")

    found_flag = 'N'

    if soup.find('div',attrs={'id':'alertBox'}) != None:
        pass
    else:
        table = soup.find_all('table', attrs={'class': 'generictext'})
        for td in table[0].find_all('td'):
            try:
                url = td.find('div').find('strong').find('a', href=True).get('href')
                for links in td.find_all('br'):
                    zip = re.sub("(\n)|(\r)|(\t)|(\xa0)|(\n),", "", links.nextSibling)

                    if search_zip in zip:
                        found_flag = Ws.search_page(url, search_name, Pcode)


            except AttributeError:
                pass
            except IndexError:
                pass

            finally:

                if found_flag == 'Y':
                    break

    if found_flag != 'Y':

        Wg.Fname_not_found.append(search_name[0])
        Wg.Lname_not_found.append(search_name[1])
        Wg.Zip_not_found.append(Pcode)





    br.close()



"""
process_file(member)

print('--------------------')
print(Wg.Group_A)
print(Wg.Name_A)
print(Wg.Link_A)
print(Wg.Url_A)

"""