########### Import all the packages needed for the processing ##############
import time
import pandas as pd
import traceback2

import main as main
from concurrent.futures import ThreadPoolExecutor , as_completed
import time
import WFGGLOBAL as Wg
import traceback
import traceback2
import sys
"""
The purpose of this program is to read list of financial advisors and call the submodules to extract the advisor information


"""
Start_time = time.strftime('%X %x %Z')
print('start time is : ' + Start_time)

#File = '/Users/P7165881/Desktop/Brodridge/input_file_extracts.xlsx'
File = '/Users/P7165881/Desktop/Brodridge/Reps for Web Research Input3.xlsx'
members=[]

try:
    #with open('/Users/P7165881/Desktop/Brodridge/20210429 MDR_FOP URLs.xlsx', mode='r') as csv_file:
    Excl = pd.read_excel(File)
    df = pd.DataFrame(Excl,columns=['mfo_per_first_name','mfo_per_last_name','mfo_ofl_postal_code','mfo_fir_name'])
    print('Total Excel : ' + str(df.count()))
    #df1 = df.iloc[:, lambda df: df.columns.str.contains('wellsfargoadvisors.com', case=False)].head()

    #df1 = df.filter(like='wellsfargoadvisors.com')
    df1 = df[df['mfo_fir_name'].str.contains('WELLS FARGO CLEARING SERVICES, LLC')]
    #df1 = df
    line_count = 0
    print('Filtered Excel : '+ str(df1.count()))


    for index, row in df1.iterrows():
        #print(row['MFO_PER_DIRECT_URL'])
        #Wa.Process_Urls(row['MFO_PER_DIRECT_URL'])

        Fname = row['mfo_per_first_name']
        Lname = row['mfo_per_last_name']
        #Pcode = str(row['mfo_ofl_postal_code']).split('-')[0]
        #Pcode = str(row['mfo_ofl_postal_code'])
        Pcode = row['mfo_ofl_postal_code']
        Fullname=[Fname,Lname]
        #print(Fullname)
        #print(Pcode)
        #Wg.sleep(Wg.np.random.randint(1, 10))
        #Wg.sleep(Wg.np.random.randint(1, 3))
        #main.process_file(Fullname,Pcode)
        member=[Fullname,Pcode]

        members.append(member)

        line_count = line_count + 1
        #print('Completed for '+ str(line_count) + ' ' + Fullname[0] + ' ' + Fullname[1])
        #print('Completed for :' + str(line_count))


        #if line_count  == 1000:
            #break




except FileNotFoundError:
    print('Invalid or Empty Input File')
    message = 'Invalid or Empty Input File'

except UnicodeDecodeError:
    print('File is corrupted or incorrect, Please check the file contents')
    message = 'File is corrupted Or Incorrect,Please check the file contents'


finally:
    print('came out')
    End_time = time.strftime('%X %x %Z')
    print('End time of url process is : ' + End_time)

    counter1 = 0
with ThreadPoolExecutor(max_workers=10) as executor:
    start = time.time()
    futures = {executor.submit(main.process_file,member): member for member in members}
    for future in as_completed(futures):
        counter1 = counter1 + 1
        print(str(counter1))
        url = futures[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
            exc_type, exc_value, exc_tb = sys.exc_info()
            tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
            print(''.join(tb.format_exception_only()))
        #else:
            #print('%r page is  bytes' % (member))
        #futures = []
        """
    results = []
    for result in as_completed(futures):
        results.append(result)
        end = time.time()
    """
    end = time.time()
    print("Time Taken: {:.6f}s".format(end - start))
    print('End time of url process is xz : ' + End_time)




try:
    df = pd.DataFrame({'Name': Wg.Name_A, 'Designation': Wg.Des_A, 'Phone': Wg.Phone_A, 'Email': Wg.Email_A,
                             'Primary Person': Wg.Primary_A, 'Group': Wg.Group_A, 'Url': Wg.Url_A,
                             'Linked In Url': Wg.Link_A})
    df.to_csv('/Users/P7165881/Desktop/Brodridge/WellsFargo/WFARG_Found_009.csv', index=False, encoding='utf-8')

    df = pd.DataFrame({'First Name': Wg.Fname_not_found, 'Last Name': Wg.Lname_not_found, 'Zip': Wg.Zip_not_found})

    df.to_csv('/Users/P7165881/Desktop/Brodridge/WellsFargo/WFARG_Error_009.csv', index=False, encoding='utf-8')


except ValueError:
    print('Name :')
    print(Wg.Name_A.__len__())
    print('Designation :')
    print(Wg.Des_A.__len__())
    print('Phone :')
    print(Wg.Phone_A.__len__())
    print('Email :')
    print(Wg.Email_A.__len__())
    print('Primary_Sw :')
    print(Wg.Primary_A.__len__())
    print('Group :')
    print(Wg.Group_A.__len__())
    print('Url :')
    print(Wg.Url_A.__len__())
    df = pd.DataFrame({'Url': Wg.Url_A, 'Name': Wg.Name_A})
    df.to_csv('/Users/P7165881/Desktop/Brodridge/WellsFargo/WFGERR0018.csv', index=False, encoding='utf-8')

    """
    df = Wg.pd.DataFrame({'List of invalid Urls': Wg.Error_Msg})
    df.to_csv('/Users/P7165881/Desktop/Brodridge/WellsFargo/Error7.csv', index=False, encoding='utf-8')
    """
finally:
    print('Process Completed Successfully')
    End_time = time.strftime('%X %x %Z')
    print('Final End time is : ' + End_time)

