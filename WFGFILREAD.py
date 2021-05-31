########### Import all the packages needed for the processing ##############
import time
import pandas as pd
import main as main
from concurrent.futures import ProcessPoolExecutor , as_completed
import time


Start_time = time.strftime('%X %x %Z')
print('start time is : ' + Start_time)

File = '/Users/P7165881/Desktop/Brodridge/input_file_extracts.xlsx'


try:
    #with open('/Users/P7165881/Desktop/Brodridge/20210429 MDR_FOP URLs.xlsx', mode='r') as csv_file:
    Excl = pd.read_excel(File)
    df = pd.DataFrame(Excl,columns=['mfo_per_first_name','mfo_per_last_name','mfo_ofl_postal_code','mfo_fir_name'])
    print('Total Excel : ' + str(df.count()))
    #df1 = df.iloc[:, lambda df: df.columns.str.contains('wellsfargoadvisors.com', case=False)].head()

    #df1 = df.filter(like='wellsfargoadvisors.com')
    #df1 = df[df['mfo_fir_name'].str.contains('WELLS FARGO CLEARING SERVICES, LLC')]
    df1 = df
    line_count = 0
    print('Filtered Excel : '+ str(df1.count()))


    for index, row in df1.iterrows():
        #print(row['MFO_PER_DIRECT_URL'])
        #Wa.Process_Urls(row['MFO_PER_DIRECT_URL'])

        Fname = row['mfo_per_first_name']
        Lname = row['mfo_per_last_name']
        Pcode = str(row['mfo_ofl_postal_code'])


        Fullname=[Fname,Lname]
        print(Fullname)
        #print(Pcode)
        #Wg.sleep(Wg.np.random.randint(1, 10))
        #Wg.sleep(Wg.np.random.randint(1, 3))
        main.process_file(Fullname,Pcode)


        line_count = line_count + 1
        #print('Completed for '+ str(line_count) + ' ' + Fullname[0] + ' ' + Fullname[1])


        #if line_count  == 10:
            #break
        """
        with ProcessPoolExecutor(max_workers=4) as executor:
            start = time.time()
            futures = [executor.submit(main.process_file,Fullname, Pcode)]
            #futures = []
            results = []
            for result in as_completed(futures):
                results.append(result)
            end = time.time()
            print("Time Taken: {:.6f}s".format(end - start))
        """

except FileNotFoundError:
    print('Invalid or Empty Input File')
    message = 'Invalid or Empty Input File'

except UnicodeDecodeError:
    print('File is corrupted or incorrect, Please check the file contents')
    message = 'File is corrupted Or Incorrect,Please check the file contents'


finally:
    #print('came out')
    End_time = time.strftime('%X %x %Z')
    print('End time of url process is : ' + End_time)

"""
    try:
        Wg.df = Wg.pd.DataFrame({'Name': Wg.Name, 'Designation': Wg.Designation, 'Phone': Wg.Phone, 'Email': Wg.Email,
                             'Primary Person': Wg.Primary_Sw, 'Group': Wg.Group, 'Url': Wg.Url,
                             'Linked In Url': Wg.Linkedin_Url})
        Wg.df.to_csv('/Users/P7165881/Desktop/Brodridge/WFARG8O7.csv', index=False, encoding='utf-8')
    except ValueError:
        print('Name :')
        print(Wg.Name.__len__())
        print('Designation :')
        print(Wg.Designation.__len__())
        print('Phone :')
        print(Wg.Phone.__len__())
        print('Email :')
        print(Wg.Email.__len__())
        print('Primary_Sw :')
        print(Wg.Primary_Sw.__len__())
        print('Group :')
        print(Wg.Group.__len__())
        print('Url :')
        print(Wg.Url.__len__())
        Wg.df = Wg.pd.DataFrame({'Url': Wg.Url,'Name': Wg.Name})
        Wg.df.to_csv('/Users/P7165881/Desktop/Brodridge/Error_urls7.csv', index=False, encoding='utf-8')


    Wg.df = Wg.pd.DataFrame({'List of invalid Urls': Wg.Error_Msg})
    Wg.df.to_csv('/Users/P7165881/Desktop/Brodridge/Error7.csv', index=False, encoding='utf-8')

    print('Process Completed Successfully')
    End_time = time.strftime('%X %x %Z')
    print('Final End time is : ' + End_time)

"""