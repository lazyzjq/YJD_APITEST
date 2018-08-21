#coding=utf-8
import requests,unittest,urllib,pymysql,time,admin_sp
from defs import add_md5,jiekuan

timee=time.time()
timee=str(timee)
@unittest.skip('asd')
class terribal1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test1(self):
        # 借款时输入price字段输入9999.99
        a=jiekuan.jie()
        a.t_jk1(9999.99)
        a.t_jk2()
        a.t_jk3()
@unittest.skip('asd')
class terribal2(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test1(self):
        # 借款时输入price字段输入1000000.01
        a=jiekuan.jie()
        a.t_jk1(10000000)
@unittest.skip('asd')
class terribal3(unittest.TestCase):
    def setUp(self):
        self.txt_path = 'D:/api_test_demo/txtfiles/'
        self.sign_url = 'http://api.yijiedai.org/'
    def test1(self):
        a=jiekuan.jie()
        #借款
        a.jk1()
        a.jk2()
        a.jk3()
        # ui自动审批发标
        thesp = admin_sp.sp()
        thesp.sp123()
        # 审批完毕，睡眠三秒再运行webdriver
        time.sleep(10)
        # 获取borrow_id
        print u'开始提取borrow_id'
        borrow_id = thesp.borrow()
        borrow_id1 = str(borrow_id)
        # 将获取的borrow_id保存到borrow_id.txt中
        with open(self.txt_path + 'borrow_id.txt', 'w+') as fp:
            fp.write(borrow_id1)
        # 登录
        lo = add_md5.the_login()
        log = lo.web_login(18965738912)
        token = log[0]
        user_id = log[1]
        traprice = 10001
        data = {'borrow_id': borrow_id1,
                'tbprice': traprice,
                'channel': '2',
                'access_token': token,
                'user_id': user_id,
                'api_request_way': '1'
                }
        r1 = requests.post(url=self.sign_url + 'V_2_0/invest/tb', data=data)
        self.assertEqual(r1.json()['message'],u'哎呀，手慢了！该项目仅剩10,000元可投！')
class terribal4(unittest.TestCase):
    def setUp(self):
        self.txt_path = 'D:/api_test_demo/txtfiles/'
        self.sign_url = 'http://api.yijiedai.org/'
        self.conn = pymysql.connect(host='yijiedai-uat.mysql.rds.aliyuncs.com', user='yijiedai',
                                    password='@YiJieDai4006021788', database='www_yijiedai_com', port=3988)
        self.cur = self.conn.cursor()
    def test1(self):
        a=jiekuan.jie()
        #借款
        a.jk1()
        a.jk2()
        a.jk3()
        # ui自动审批发标
        thesp = admin_sp.sp()
        thesp.sp123()
        # 审批完毕，睡眠三秒再运行webdriver
        time.sleep(10)
        # 获取borrow_id
        print u'开始提取borrow_id'
        borrow_id = thesp.borrow()
        borrow_id1 = str(borrow_id)
        # 将获取的borrow_id保存到borrow_id.txt中
        with open(self.txt_path + 'borrow_id.txt', 'w+') as fp:
            fp.write(borrow_id1)
        # 登录
        lo = add_md5.the_login()
        log = lo.web_login(18965738912)
        token = log[0]
        user_id = log[1]
        traprice = 10000
        data = {'borrow_id': borrow_id1,
                'tbprice': traprice,
                'channel': '2',
                'access_token': token,
                'user_id': user_id,
                'api_request_way': '1'
                }
        r1 = requests.post(url=self.sign_url + 'V_2_0/invest/tb', data=data)
        print r1.json()['message']
        thesp.maxsp()
        print u'债权转让'
        # 读取borrow_id,用于查询数据库中的creditor_id，转让1份
        with open(self.txt_path + 'borrow_id.txt', 'r+') as lp:
            bid = lp.readline()
        borrowid = int(bid)
        print u'等待数据库更新'
        time.sleep(8)
        # 查询creditor_id
        sql = "SELECT creditor_id FROM yjd_creditor WHERE borrow_id=%d" % borrowid
        self.cur.execute(sql)
        self.conn.commit()
        cid = self.cur.fetchall()
        cid1 = cid[0][0]
        cid1 = str(cid1)
        creditor_id = int(cid1)
        # 将creditor_id写入文件，提供取消债转用
        with open(self.txt_path + 'creditorid.txt', 'w+') as pp:
            pp.write(cid1)
        # 登录
        l = add_md5.the_login()
        al = l.web_login(18965738912)
        token = al[0]
        user_id = al[1]
        data = {'creditorId': creditor_id,
                'transferNum': 101,
                'discApr': 0.5,
                'discount_per_partion': 2.0,
                'access_token': token,
                'user_id': user_id,
                'api_request_way': '1'}
        r = requests.post(url=self.sign_url + 'V_2_0/creditor/transferApply', data=data)
        self.assertEqual(r.json()['message'],u'参数有误!')
if __name__ == '__main__':
    unittest.main()