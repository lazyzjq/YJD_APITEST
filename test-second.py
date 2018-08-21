#coding=utf-8
import requests,unittest,urllib,pymysql,time,random,json
from defs import shenfenzheng,add_md5,get_password

class test_signin(unittest.TestCase):
    def setUp(self):
        self.sign_url='http://test1117-api.yijiedai.org/'
        self.imagecodeuid='http://api.yijiedai.org/V_2_0/imageCode/index'
        self.imgsavepath='D:/api_test_demo/yanzhengma/signin.png'
        the_use=get_password.get_psw()
        self.phonenum=the_use.get_psw()#获取手机号
        self.inphonenum=int(self.phonenum)
        #将目前手机号保存至文件
        with open('D:/api_test_demo/txtfiles/current_phonenum.txt','w+') as ps:
            ps.write(self.phonenum)
        self.now_time=int(time.time())
        #连接短信验证码数据库
        self.conn=pymysql.connect(host='192.168.10.140',user='www_yijiedai_com ',password='@YiJieDai4006021788',database='www_yijiedai_com',port=3306)
        self.cur=self.conn.cursor()
        sql1="INSERT INTO yjd_verify_sms (mobile,smscode,num,senttime,ip) VALUES (%d,'111111',1,%d,'192.168.100.219')"%(self.inphonenum,self.now_time)#插入注册所需的短信验证码
        self.cur.execute(sql1)
        self.conn.commit()
        # 读取身份证(每次读取的身份证不一样，往下迭代),调用shenfenzheng方法获取新的身份证
        get_sfzs=shenfenzheng.sfz()
        self.sfz=get_sfzs.get_sfz().replace('\n','')
        #密码加密
        five = add_md5.add_md5()
        self.password = five.am5('a123456789')
        #txt文件地址
        self.txtpath='D:/api_test_demo/txtfiles/'
    def tearDown(self):
        sql2="DELETE FROM yjd_verify_sms WHERE mobile=%d"%self.inphonenum
        self.cur.execute(sql2)
        self.conn.commit()
        self.conn.close()
    def test_2(self):
        '''验证校验短信验证码与注册'''
        #获取setup中写入的手机号
        with open('D:/api_test_demo/txtfiles/current_phonenum.txt','r+') as pd:
            the_number0=pd.readline()
            the_number=int(the_number0)
        r_check=requests.post(url=self.sign_url+'V_2_0/reg/step/1',data={'mpNumber':the_number,'msgCode':'111111'})#传入手机号码，固定111111验证码
        vaild_token=r_check.json()['data']['valid_token']#获取签名
        message=r_check.json()['data']['message']
        self.assertEqual(message,u'验证通过')#验证返回的提示是否一致
        r_signin=requests.post(url=self.sign_url+'V_2_0/reg/step/2',data={'mpNumber':the_number,'password':self.password,'device_no':'45211562','mobile_type':'android','valid_token':vaild_token})
        user_id=str(r_signin.json()['data']['user_id'])
        token=str(r_signin.json()['data']['access_token'])
        with open('D:/api_test_demo/txtfiles/user_id&access_token.txt','w+') as pr:
            pr.write(user_id+'\n'+token)
        self.assertEqual(the_number,r_signin.json()['data']['mobile'])#判断接口返回的电话号码和注册用的电话号码是否一致
        with open('D:/api_test_demo/txtfiles/now_username.txt','w+') as pd:#将这个case中获取的手机号存到now_username中，供以后的case用
            pd.write(the_number0)

    def test_3(self):
        '''验证存管用户开户'''
        with open('D:/api_test_demo/txtfiles/now_username.txt','r+') as pp:#从now_username获取当前的手机号
            cur_num=pp.readline()
        with open('D:/api_test_demo/txtfiles/user_id&access_token.txt','r+') as re:#获取userid，token
            the_all=re.readlines()
            user_id=the_all[0]
        #登录
        r_login=add_md5.the_login()
        token=r_login.login(cur_num)
        #存管用户绑卡
        re1=requests.post(url=self.sign_url+'V_2_0/bankDepoAccount/bindCard',data={'user_id':user_id,'access_token':token,'api_request_way':'1','bank_card_no':'6228480402564890018','bank_card_mobile':cur_num,'idname':'借鸡生蛋','idcard':self.sfz,'user_type':'1'})
        print re1.json()['message']

if __name__=='__main__':
    unittest.main()





