
"""
print(grp_name)
        print(grp_url)

        for links in grp_url:
            print('Searching for links ' + links)
            resp1 = requests.get(links)

            #print(resp1.status_code)

            soup1 = BeautifulSoup(resp1.text, 'lxml')
            found = 'N'
            #print(soup1.find('div', attrs={'class': 'groupFAs'}))

            for member1 in soup1.find('div', attrs={'id': 'groupFAs'}).find('ul').find_all('li'):
                names1 = member1.find('a', href=True).text.strip()
                print(names1)
                print('came in side ' + links)
                print(search_name[0].upper())
                print(search_name[1].upper())

                if search_name[0].upper() in names1 and search_name[1].upper() in names1:
                    print('Group found ')

"""