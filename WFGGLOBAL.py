"""
The purpose of this module is to
    1.Create variables which can be used across the application
"""

#Member Details are captured into following Arrays
Name_A=[]
Phone_A=[]
Url_A=[]
Email_A=[]
Des_A=[]
Group_A=[]
Primary_A=[]
Link_A=[]

"""
Members for whom no details are found are added into following Arrays
"""
Name_not_found=[]
Fname_not_found =[]
Lname_not_found=[]
Zip_not_found =[]

"""
Data Dictionary which contains the group and Member details. 
This is used to avoid multiple hits for the same group
"""
Group_and_Member_Dict = {}
All_groups=[]
All_members =[]

"""
CSV Files 
"""
File_Input = ''
File_output1 = ''
File_output2 =''

"""
Counters and Message Variables
"""
Counter_global = 0
Counter_max = 0
message = ''