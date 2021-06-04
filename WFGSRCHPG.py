import logging
import  WFGSRCHMB as Wb
import requests
from bs4 import BeautifulSoup
import WFGGLOBAL as Wg
import WFGSRCFRGP as Wf

grp_found = 'N'


def search_page(url,search_name,Pcode):

    #print(Pcode)
    group_exists = 'N'
    grp_found ='N'
    resp = requests.get(url)


    if resp.ok:
        pass
    else:
        print('error occurred')

    soup = BeautifulSoup(resp.text, "lxml")

    grp_name = ' '

    if Wg.Group_and_Member_Dict.__len__() > 0:

        for x,y in Wg.Group_and_Member_Dict.items():

            mem_name = search_name[0].upper() +' ' + search_name[1].upper()


            if y.count(mem_name) > 0:

                if y.count(mem_name)==1 :
                    grp_name = x
                else:
                    grp_name = x + ',' + grp_name

                group_exists ='Y'

    if soup.find('div', attrs={'id': 'ourTeams'}) != None and group_exists != 'Y':

        for groups in soup.find('div', attrs={'id': 'ourTeams'}).find('ul').find_all('li'):
            grp_url = groups.find('a', href=True).get('href')
            Wg.All_groups.append(groups.find('a', href=True).text.strip())

            Wg.All_members = []
            grp_found = Wf.Search_for_Group(grp_url, search_name)
            gname = groups.find('a', href=True).text.strip()
            #print('group found  ' + grp_found)


            if 'of Wells Fargo Advisors' in gname:
                grp_name = gname.split('of Wells Fargo Advisors')[0]
            else:
                grp_name = gname

            if grp_found == 'Y':
                gname1 = grp_name

            Wg.Group_and_Member_Dict[grp_name] = Wg.All_members
            #print(grp_name)
            #print(Wg.All_members)



    counter = 0
    for members in soup.find('div',attrs={'id':'ourFAs'}).find('ul').find_all('li'):
        Memurl = members.find('a',href=True).get('href')
        names  = members.find('a',href=True).text.strip()
        names.capitalize()
        counter = counter + 1

        if (search_name[0].upper() in names and search_name[1].upper() in names) or \
                (search_name[1].upper() in names and search_name[0][0:3].upper() in names) :

            if counter == 1:
                Wg.Primary_A.append('Y')
            else:
                Wg.Primary_A.append('N')

            mem_found ='Y'
            Wb.search_member(Memurl)
            Wg.Url_A.append(Memurl)
            if grp_found =='Y':
                Wg.Group_A.append(gname1)
            elif group_exists =='Y':
                Wg.Group_A.append(grp_name)
            else:
                Wg.Group_A.append('')


            return 'Y'






