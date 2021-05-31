import logging
import  WFGSRCHMB as Wb
import requests
from bs4 import BeautifulSoup
import WFGGLOBAL as Wg
import WFGSRCFRGP as Wf
import WFGSRCMB2 as W2

grp_found = 'N'

def search_page(url,search_name,Pcode):

    print(Pcode)
    group_exists = 'N'
    resp = requests.get(url)

    #print('this is my url : '+ url +  '  '+ search_name[0] + '  ' + search_name[1])
    if resp.ok:
        pass
    else:
        print('error occurred')

    soup = BeautifulSoup(resp.text, "lxml")

    grp_name = ' '

    if Wg.Group_and_Member_Dict.__len__() > 0:
        #print('checking group')
        for x,y in Wg.Group_and_Member_Dict.items():
            #print('Search the member here')
            #print(x,y)
            mem_name = search_name[0].upper() +' ' + search_name[1].upper()
            #print(mem_name)

            if y.count(mem_name) > 0:
                grp_name =x
                group_exists ='Y'

    if soup.find('div', attrs={'id': 'ourTeams'}) != None and group_exists != 'Y':

        for groups in soup.find('div', attrs={'id': 'ourTeams'}).find('ul').find_all('li'):
            grp_url = groups.find('a', href=True).get('href')
            Wg.All_groups.append(groups.find('a', href=True).text.strip())

            #print('Before call : ' + grp_found )
            Wg.All_members = []
            grp_found = Wf.Search_for_Group(grp_url, search_name)

            Wg.Group_and_Member_Dict[groups.find('a', href=True).text.strip()] = Wg.All_members

            #print('Dcitionary is :----------------------->')
            #print(Wg.Group_and_Member_Dict)
            #print('After call : ' + grp_found)
            if grp_found == 'Y':
                print('group found ' + grp_name + ' for ' + search_name[0] + '  ' + search_name[1] )
                grp_name = groups.find('a', href=True).text.strip()
                #Wg.Group_A.append(grp_name)



    counter = 0
    for members in soup.find('div',attrs={'id':'ourFAs'}).find('ul').find_all('li'):
        Memurl = members.find('a',href=True).get('href')
        names  = members.find('a',href=True).text.strip()
        names.capitalize()
        counter = counter + 1


        #print(search_name)
        if (search_name[0].upper() in names and search_name[1].upper() in names) or \
                (search_name[1].upper() in names and search_name[0][0:3].upper() in names) :

            if counter == 1:
                Wg.Primary_A.append('Y')
            else:
                Wg.Primary_A.append('N')

            #print("found desired member " + names + ' Url is : ' + Memurl )
            mem_found ='Y'
            Wb.search_member(Memurl)
            Wg.Url_A.append(Memurl)
            #if grp_found =='Y' or group_exists =='Y':
            Wg.Group_A.append(grp_name)

            return 'Y'


        """
        if search_name[1].upper() in names and search_name[0][0:4].upper() in names :
            print('inside search 2---------------------------------> ' + search_name[0][0:4] +'  ' + search_name[1] )

            
            
            

            if W2.search_member(Memurl,Pcode)== 'Y':
                if counter == 1:
                    Wg.Primary_A.append('Y')
                else:
                    Wg.Primary_A.append('N')

                Wg.Url_A.append(Memurl)
                Wg.Group_A.append(grp_name)

            return 'Y'

        """



