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
import WFGFILEWRT as Ww
"""
The purpose of this program is to read list of financial advisors and call the submodules to extract the advisor information


"""

def Start_Process(input_file):
    #Start_time = time.strftime('%X %x %Z')
    #print('start time is : ' + Start_time)

    #File = '/Users/P7165881/Desktop/Brodridge/input_file_extracts.xlsx'
    #File = '/Users/P7165881/Desktop/Brodridge/Reps for Web Research Input3.xlsx'
    members=[]

    File = input_file
    #print(File)

    try:
        #with open('/Users/P7165881/Desktop/Brodridge/20210429 MDR_FOP URLs.xlsx', mode='r') as csv_file:
        Excl = pd.read_excel(File)
        df = pd.DataFrame(Excl,columns=['mfo_per_first_name','mfo_per_last_name','mfo_ofl_postal_code','mfo_fir_name'])
        print('Total # records in Excel : ' + str(df.__len__()))
        #df1 = df.iloc[:, lambda df: df.columns.str.contains('wellsfargoadvisors.com', case=False)].head()

        #df1 = df.filter(like='wellsfargoadvisors.com')
        df1 = df[df['mfo_fir_name'].str.contains('WELLS FARGO CLEARING SERVICES, LLC')]
        #df1 = df
        line_count = 0
        #print('Filtered Excel : '+ str(df1.count()))
        print( '#of records in Filtered from Excel : -------------> '+ str(df1.__len__()))


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

        End_time = time.strftime('%X %x %Z')
        Wg.Counter_max = members.__len__()
        print(Wg.Counter_max)
        print('End time of url process is : ' + End_time)


    with ThreadPoolExecutor(max_workers=10) as executor:
        start = time.time()
        futures = {executor.submit(main.process_file,member): member for member in members}
        for future in as_completed(futures):
            Wg.Counter_global = Wg.Counter_global + 1
            #print(str(counter1))
            url = futures[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
                exc_type, exc_value, exc_tb = sys.exc_info()
                tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
                print(''.join(tb.format_exception_only()))

        end = time.time()
        print("Time Taken: {:.6f}s".format(end - start))
        print('End time of url process is xz : ' + End_time)



    Ww.Write_To_Csv()



