
class class1:
    def name(self):
        return 'class1'
    def head(self):
        return 'welcome to my head'
    def verify(self,str1,str2):
        if str1 in str2:
            print('yes, string '+ str1 + ' is present in ' + str2)


x = class1()

y= x.name()

print(y)

#x.verify('sagar','sagar kumthekar')

