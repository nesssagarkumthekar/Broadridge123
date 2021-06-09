import WFGGLOBAL as Wg
import WFGPRCMEM as Wp
import requests
import WFGSRCHMB as Wb

def Alt_Search_Method(search_name):

    Base_Url= 'https://home.wellsfargoadvisors.com/'
    Fin_Url= Base_Url + search_name[0] + '.' + search_name[1]

    myses= requests.session()

    resp = myses.get(Fin_Url)

    if resp.status_code ==404:
        return 'N'
    elif resp.status_code == 200:
        Wb.search_member(Fin_Url)



