class sfz():
    def get_sfz(self):
        with open('D:/api_test_demo/txtfiles/count.txt','r+') as fp:
            the_num=fp.readline()
            the_num=int(the_num)
            the_num+=1
        with open('D:/api_test_demo/txtfiles/count.txt','w+') as fc:
            the_num1=str(the_num)
            fc.write(the_num1)
        with open('D:/api_test_demo/txtfiles/shenfenzheng.txt','r+') as lp:
            the_sfz=lp.readlines()[the_num]
        return the_sfz
