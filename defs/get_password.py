class get_psw():
    def get_psw(self):
        with open('D:/api_test_demo/txtfiles/username_count.txt','r+') as fp:
            the_num=fp.readline()
            the_num=int(the_num)
            the_num+=1
        with open('D:/api_test_demo/txtfiles/username_count.txt','w+') as fc:
            the_num1=str(the_num)
            fc.write(the_num1)
        with open('D:/api_test_demo/txtfiles/usernames.txt','r+') as hh:
            the_psw=hh.readlines()[the_num]
        return the_psw
    def get_credit(self):
        with open('D:/api_test_demo/txtfiles/credit_count.txt','r+') as fp:
            the_num1=fp.readline()
            the_num1=int(the_num1)
            the_num1+=1
        with open('D:/api_test_demo/txtfiles/credit_count.txt','w+') as fc:
            the_num2=str(the_num1)
            fc.write(the_num2)
        with open('D:/api_test_demo/txtfiles/credit_card.txt','r+') as hh:
            the_psw=hh.readlines()[the_num1]
        return the_psw.replace('\n','')