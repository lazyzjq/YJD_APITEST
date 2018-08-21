# coding=utf-8
import requests, unittest,pymysql, time, admin_sp
from defs import add_md5, get_password, jiekuan


# 主干测试
class sign_test(unittest.TestCase):
    def setUp(self):
        self.txt_path = 'D:/api_test_demo/txtfiles/'
        self.sign_url = 'http://api.yjdtest.cn/'
        # self.imagecodeuid='http://api.yijiedai.org/V_2_0/imageCode/index'
        # self.imgsavepath='D:/api_test_demo/yanzhengma/signin.png'
        # the_use=get_password.get_psw()
        # self.phonenum=the_use.get_psw()#获取手机号
        # self.inphonenum=int(self.phonenum)
        # 将目前手机号保存至文件
        # with open('D:/api_test_demo/txtfiles/current_phonenum.txt','w+') as ps:
        #    ps.write(self.phonenum)
        # self.now_time=int(time.time())
        # self.jiekuantime=time.time()
        # with open(self.txt_path+'now_username.txt','r+') as jk:
        #    self.username=jk.readline()
        # 连接短信验证码数据库
        self.conn = pymysql.connect(host='yijiedai-uat.mysql.rds.aliyuncs.com', user='yijiedai',
                                    password='@YiJieDai4006021788', database='www_yijiedai_com', port=3988)
        self.cur = self.conn.cursor()
        # sql1="INSERT INTO yjd_verify_sms (mobile,smscode,num,senttime,ip) VALUES (%d,'111111',1,%d,'192.168.100.219')"%(self.inphonenum,self.now_time)#插入注册所需的短信验证码
        # self.cur.execute(sql1)

        # 读取身份证(每次读取的身份证不一样，往下迭代),调用shenfenzheng方法获取新的身份证
        # get_sfzs=shenfenzheng.sfz()
        # self.sfz=get_sfzs.get_sfz().replace('\n','')
        # 密码加密
        # five = add_md5.add_md5()
        # self.password = five.am5('a123456789')
        # txt文件地址
        self.txtpath = 'D:/api_test_demo/txtfiles/'
        self.buyusername = 15889725416
        self.nomoney = 15848657321
        self.JKR = 15896302548
        self.zqbuyer = 18386249157

    def tearDown(self):
        self.conn.close()

    def runTest(self):
        pass

    def test_1(self):
        '''没钱的投资者投资'''
        pass

    @unittest.skip(u'无理由')
    def test_2(self):
        '''验证校验短信验证码与注册'''
        # 获取setup中写入的手机号
        print u'注册帐号'
        with open('D:/api_test_demo/txtfiles/current_phonenum.txt', 'r+') as pd:
            the_number0 = pd.readline()
            the_number = int(the_number0)
        r_check = requests.post(url=self.sign_url + 'V_2_0/reg/step/1',
                                data={'mpNumber': the_number, 'msgCode': '111111'})  # 传入手机号码，固定111111验证码
        vaild_token = r_check.json()['data']['valid_token']  # 获取签名
        message = r_check.json()['data']['message']
        self.assertEqual(message, u'验证通过')  # 验证返回的提示是否一致
        r_signin = requests.post(url=self.sign_url + 'V_2_0/reg/step/2',
                                 data={'mpNumber': the_number, 'password': self.password, 'device_no': '45211562',
                                       'mobile_type': 'android', 'valid_token': vaild_token})
        user_id = str(r_signin.json()['data']['user_id'])
        token = str(r_signin.json()['data']['access_token'])
        with open('D:/api_test_demo/txtfiles/user_id&access_token.txt', 'w+') as pr:
            pr.write(user_id + '\n' + token)
        self.assertEqual(the_number, r_signin.json()['data']['mobile'])  # 判断接口返回的电话号码和注册用的电话号码是否一致
        with open('D:/api_test_demo/txtfiles/now_username.txt', 'w+') as pd:  # 将这个case中获取的手机号存到now_username中，供以后的case用
            pd.write(the_number0)

    @unittest.skip(u'暂时跳过')
    def test_3(self):
        '''验证存管用户开户,绑卡'''
        print u'开户绑卡'
        # 将身份证保存到now_sfz,在读取出来
        with open(self.txt_path + 'now_sfz.txt', 'w+') as pk:
            sfz = pk.write(self.sfz)
        with open(self.txt_path + 'now_sfz.txt', 'r+') as po:
            the_sfz = po.readline()
        with open('D:/api_test_demo/txtfiles/now_username.txt', 'r+') as pp:  # 从now_username获取当前的手机号
            cur_num = pp.readline()
            cur_num = int(cur_num)
        with open('D:/api_test_demo/txtfiles/user_id&access_token.txt', 'r+') as re:
            user_id0 = re.readlines()[0]
            user_id = int(user_id0)  # 获取user_id
        # 读取银行卡
        cre = get_password.get_psw()
        credit_card = cre.get_credit()
        # 银行卡写入now_credit_card
        with open(self.txt_path + 'now_credit.txt', 'w+') as iu:
            iu.write(credit_card)
        # 调用登录接口
        log = add_md5.the_login()
        token = log.web_login(cur_num)[0]  # 获取登录后返回的token
        data = {'user_id': user_id, 'access_token': token, 'api_request_way': '1', 'name': '王存管', 'idcard': the_sfz,
                'user_type': '1', 'user_role': '1'}
        re1 = requests.post(url=self.sign_url + 'V_2_0/bankDepoAccount/openAccount', data=data)
        self.assertEqual(re1.json()['message'], u'操作成功')  # 判断存管开户返回的消息是否正确
        # 存管用户绑卡
        re2 = requests.post(url=self.sign_url + 'V_2_0/bankDepoAccount/bindCard',
                            data={'user_id': user_id, 'access_token': token, 'api_request_way': '1',
                                  'bank_card_no': credit_card, 'bank_card_mobile': cur_num, 'idname': '借鸡生蛋',
                                  'idcard': self.sfz, 'user_type': '1'})
        self.assertEqual(re2.json()['message'], u'操作成功!')

    def test_4(self):
        '''借款，投标'''
        print u'借款，投标'
        # 首先借款，并运用selenium操作后台审批
        # 获取借款人的金额，用于断言
        sql5 = "SELECT available FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % self.JKR
        self.cur.execute(sql5)
        jk1 = self.cur.fetchall()
        jkb = float(jk1[0][0])
        # 借款100
        bm = jiekuan.jie(10.5,12)
        bm1 = bm.jk1()
        self.assertEqual(bm1, u'提交成功!')
        bm2 = bm.jk2()
        self.assertEqual(bm2, u'提交成功!')
        bm3 = bm.jk3()
        self.assertEqual(bm3, u'提交成功!')
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

        # 没钞票的去投标
        lo = add_md5.the_login()
        no_money = lo.web_login(self.nomoney)
        no_token = no_money[0]
        no_user_id = no_money[1]
        no_data = {'borrow_id': borrow_id1,
                   'tbprice': 10000,
                   'channel': '2',
                   'access_token': no_token,
                   'user_id': no_user_id,
                   'api_request_way': '1'}
        no_r = requests.post(url=self.sign_url + 'V_2_0/invest/tb', data=no_data)
        self.assertEqual(u'账户可用余额不足!', no_r.json()['message'])

        # 正常投标，登录
        log = lo.web_login(self.buyusername)
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
        # 获取投标前的金额
        phone = self.buyusername
        # 获取存管金额
        sql = "SELECT available FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % phone
        self.cur.execute(sql)
        tol = self.cur.fetchall()
        totleb = float(tol[0][0])
        # 获取当前冻结金额
        sql2 = "SELECT frozen FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % phone
        self.cur.execute(sql2)
        fro = self.cur.fetchall()
        frozenb = float(fro[0][0])
        # 投标
        r1 = requests.post(url=self.sign_url + 'V_2_0/invest/tb', data=data)
        print r1.json()['message']
        self.assertEqual(r1.json()['message'], u'恭喜您投标成功!')
        # 获取投标后的金额
        sql3 = "SELECT available FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % phone
        self.cur.execute(sql3)
        tota = self.cur.fetchall()
        tltlea = float(tota[0][0])
        sql4 = "SELECT frozen FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % phone
        self.cur.execute(sql4)
        fraa = self.cur.fetchall()
        frozena = float(fraa[0][0])
        # 判断投资人投标前减投标资金后是否等于投标后的资金
        self.assertEqual(totleb - traprice, tltlea)
        # 判断投资人交易后的冻结资金
        self.assertEqual(frozenb + traprice, frozena)
        # 满标终审]
        print u'终审开始'
        time.sleep(10)
        thesp.maxsp()
        # 等待十秒，让数据库中的数据计算完毕，若不等待会因为数据库金额没更新好，断言失败
        print u'等待借款人金额数据更新20s'
        time.sleep(20)
        # 获取借款人借款后的金额，判断是否增加正确
        sql6 = "SELECT available FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % self.JKR
        self.cur.execute(sql6)
        jk2 = self.cur.fetchall()
        jka = float(jk2[0][0])
        print 'jkb=' + str(jkb)
        print 'jka=' + str(jka)
        # 判断借款人金额
        self.assertEqual(jka, jkb + traprice)

    def test_5(self):
        '''债权转让'''
        # 债转折让率改为0.3,0.8,1.0,1.5,2.0，3.0
        print u'债权转让'
        # 读取borrow_id,用于查询数据库中的creditor_id，转让1份
        with open(self.txt_path + 'borrow_id.txt', 'r+') as lp:
            bid = lp.readline()
        borrowid = int(bid)
        # 查询creditor_id
        sql = "SELECT creditor_id FROM yjd_creditor WHERE borrow_id=%d" % borrowid
        self.cur.execute(sql)
        cid = self.cur.fetchall()
        cid1 = cid[0][0]
        cid1 = str(cid1)
        creditor_id = int(cid1)
        # 将creditor_id写入文件，提供取消债转用
        with open(self.txt_path + 'creditorid.txt', 'w+') as pp:
            pp.write(cid1)
        # 登录
        l = add_md5.the_login()
        al = l.web_login(self.buyusername)
        token = al[0]
        user_id = al[1]
        data = {'creditorId': creditor_id,
                'transferNum': 1,
                'discApr': 0.3,
                'discount_per_partion': 2.0,
                'access_token': token,
                'user_id': user_id,
                'api_request_way': '1'}
        r = requests.post(url=self.sign_url + 'V_2_0/creditor/transferApply', data=data)
        print r.json()['message']
        self.assertEqual(r.json()['message'], u'转让申请成功！')

    def test_6(self):
        '''取消债权转让'''
        # 获取上一步保存的credit_id,取消转让，再转让出去
        with open(self.txt_path + 'creditorid.txt', 'r+') as fp:
            cid = fp.readline()
        cid = int(cid)
        # 登录
        log = add_md5.the_login()
        login = log.web_login(self.buyusername)
        token = login[0]
        userid = login[1]
        # 取消转让
        r = requests.post(url=self.sign_url + 'V_2_0/creditor/transfer_re',
                          data={'id': cid, 'access_token': token, 'user_id': userid, 'api_request_way': '1'})
        self.assertEqual(r.json()['message'], u'已取消！')
        # 转让
        data = {'creditorId': cid,
                'transferNum': 100,
                'discApr': 0.5,
                'discount_per_partion': 5,
                'access_token': token,
                'user_id': userid,
                'api_request_way': '1'}
        r2 = requests.post(url=self.sign_url + 'V_2_0/creditor/transferApply', data=data)
        self.assertEqual(r2.json()['message'], u'转让申请成功！')

    def test_7(self):
        '''购买债权'''
        print u'购买债权'
        # 获取债权转让记录id
        with open(self.txt_path + 'borrow_id.txt', 'r+') as po:
            bid = po.readline()
            bid = int(bid)
        sql = "SELECT id FROM yjd_creditor_transfer WHERE borrow_id=%d" % bid
        self.cur.execute(sql)
        x = self.cur.fetchall()
        zzid = x[0][0]
        # 获取转让人和购买人交易前的金额
        sql1 = "SELECT available FROM yjd_bank_depo_account WHERE  bank_card_mobile=%d" % self.buyusername
        self.cur.execute(sql1)
        buy = self.cur.fetchall()
        buycash = float(buy[0][0])  # 转让人的金额
        sql2 = "SELECT available FROM yjd_bank_depo_account WHERE  bank_card_mobile=%d" % 18386249157
        self.cur.execute(sql2)
        buyer = self.cur.fetchall()
        buyercash = float(buyer[0][0])  # 购买人的金额
        # 登录
        lo = add_md5.the_login()
        the_a = lo.web_login(18386249157)
        user_id = the_a[1]
        token = the_a[0]
        r2 = requests.post(url=self.sign_url + 'V_2_0/invest/buycreditor',
                           data={'id': zzid, 'channel': '2', 'user_id': user_id, 'access_token': token,
                                 'api_request_way': '1', 'noPwd': 1})
        print r2.json()['message']
        self.assertEqual(r2.json()['message'], u'恭喜您购买成功!')
        # 判断购买债权后，债转人和购买人的资金改变
        # 获取购买债权后的债转人,购买人账户金额
        print '购买成功后等待数据库更新数据，等待8s'
        time.sleep(8)
        self.cur.execute(sql1)
        zhuan = self.cur.fetchall()
        zhuancash = float(zhuan[0][0])  # 债转人购买后的金额
        # 获取购买人购买后的金额
        self.cur.execute(sql2)
        mai = self.cur.fetchall()
        maicash = float(mai[0][0])
        # 从crediter_tranfer中获取公允价值，转让折扣率，本金，管理费
        # 计算转让人到账金额和购买人付出金额  转让人到账金额=公允-本金*折让率  购买人应付金额=公允-本金*折让率+管理费
        sql3 = "SELECT `value` FROM yjd_creditor_transfer WHERE borrow_id=%d" % bid
        self.cur.execute(sql3)
        gy = self.cur.fetchall()
        gongyun = float(gy[0][0])  # 公允价值
        sql4 = "SELECT disc_apr FROM yjd_creditor_transfer WHERE borrow_id=%d" % bid
        self.cur.execute(sql4)
        zrl = self.cur.fetchall()
        zherl = float(zrl[0][0])
        zherl = zherl / 100  # 折让率,从数据库直接取出的值为0.5%，需要除100才能用来运算
        sql5 = "SELECT capital FROM yjd_creditor_transfer WHERE borrow_id=%d" % bid
        self.cur.execute(sql5)
        benjin = self.cur.fetchall()
        bj = float(benjin[0][0])  # 本金
        sql6 = "SELECT manage FROM yjd_creditor_transfer WHERE borrow_id=%d" % bid
        self.cur.execute(sql6)
        manage = self.cur.fetchall()
        gl = float(manage[0][0])  # 管理费
        sql7 = "SELECT discount_per_partion FROM yjd_creditor_transfer WHERE borrow_id=%d" % bid
        self.cur.execute(sql7)
        zhuanrj = self.cur.fetchall()
        zrj = float(zhuanrj[0][0])  # 转让金
        # 计算转让人应收益金额
        zrr = gongyun - round(bj * zherl, 2) - zrj
        # 计算购买人应付的金额
        gmr = gongyun - round(bj * zherl, 2) + gl
        # 判断转让人资金是否增加正确
        if buycash+zrr==zhuancash:
            print u'转让人资金增加正确'
        else:
            print u'转让人增加后的资金：'+str(buycash+zrr)
        # 判断购买人资金是否减少正确
        second_result = str(buyercash - gmr + 2)
        print second_result
        if second_result==maicash:
            print u'购买人资金减少正确'
        else:
            print u'购买人资金减少后的值：'+str(second_result)

    def test_8(self):
        '''正常还款'''
        print u'正常还款'
        # 获取还款前的余额
        sql2 = "SELECT available FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % self.JKR
        self.cur.execute(sql2)
        beforelist = self.cur.fetchall()
        returnb = float(beforelist[0][0])
        # 登录
        l = add_md5.the_login()
        log = l.web_login(self.JKR)
        token = log[0]
        user_id = log[1]
        # 获取borrow_id
        with open(self.txt_path + 'borrow_id.txt', 'r+')as p:
            borrow_id = p.readline()
            bid = int(borrow_id)
        sql = "SELECT id FROM yjd_arrears_form WHERE borrow_id=%d AND `limit`=1" % bid
        self.cur.execute(sql)
        tid = self.cur.fetchall()
        id = str(tid[0][0])
        r = requests.post(self.sign_url + 'V_2_0/borrow/repaysubmit/' + id,
                          data={'access_token': token, 'user_id': user_id, 'api_request_way': '1'})
        self.assertEqual(r.json()['message'], u'还款成功!')
        # 获取还款后的余额
        sql1 = "SELECT available FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % self.JKR
        self.cur.execute(sql1)
        afterlist = self.cur.fetchall()
        returna = float(afterlist[0][0])
        # 获取还款金额
        sql2 = "SELECT price FROM yjd_arrears_form WHERE borrow_id=%d AND `limit`=1" % bid
        self.cur.execute(sql2)
        rprice = self.cur.fetchall()
        reprice = float(rprice[0][0])
        # 判断还款后余额是否正确
        self.assertEqual(returnb - reprice, returna)

    def test_17(self):
        '''找回密码'''
        # 获取volid_token
        nt = time.time()
        nowt = int(nt)
        change_num = 15848657321
        sql = "INSERT INTO yjd_verify_sms (mobile,smscode,num,senttime,ip) VALUES (%d,111111,1,%d,'192.168.100.219')" % (change_num, nowt)
        self.cur.execute(sql)
        self.conn.commit()
        r = requests.post(url=self.sign_url + 'V_2_0/pwd/login/step/2',
                          data={'mpNumber': change_num, 'msgCode': '111111'})
        self.assertEqual(r.json()['data']['message'], u'验证通过')
        vt = r.json()['data']['valid_token']  # 获取到valid_token
        # 修改密码，密码加密
        pd = add_md5.add_md5()
        pwd = pd.am5('a123456')
        r2 = requests.post(url=self.sign_url + 'V_2_0/pwd/login/step/3',
                           data={'valid_token': vt, 'mpNumber': change_num, 'pwd': pwd})
        self.assertEqual(r2.json()['state'], '1')  # 由于没有任何返回信息，就对比state了
        sql2 = "DELETE FROM yjd_verify_sms WHERE mobile=%d" % change_num
        self.cur.execute(sql2)
        self.conn.commit()
    def test_10(self):
        '''判断是否认证银行卡'''
        log = add_md5.the_login()
        the_all = log.web_login('18386249157')
        token = the_all[0]
        userid = the_all[1]
        r = requests.post(url=self.sign_url + 'V_2_0/auth/isAuthBank',
                          data={'access_token': token, 'user_id': userid, 'api_request_way': '1'})
        self.assertEqual(r.json()['data']['isFlag'], False)

    def test_11(self):
        '''修改登录密码'''
        # 登录
        log = add_md5.the_login()
        the_all = log.web_login('18386249157')
        token = the_all[0]
        userid = the_all[1]
        # 加密
        pd = add_md5.add_md5()
        pwd = pd.am5('a123456')
        r = requests.post(url=self.sign_url + 'V_2_0/pwd/login/modify',
                          data={'old': pwd, 'pwd': pwd, 'access_token': token, 'user_id': userid,
                                'api_request_way': '1'})
        self.assertEqual(r.json()['data']['idname'], u'张兆志')  # 对比返回的用户名称

    def test_12(self):
        '''手机号变更'''
        now_time = time.time()
        nt = int(now_time)
        # 获取文件中最后一个帐号
        with open(self.txt_path + 'phonechange.txt', 'r+') as ko:
            pn = ko.readlines()
        phone_num = pn[-1].strip('\n')
        inpn = int(phone_num)
        # 登录
        log = add_md5.the_login()
        the_all = log.web_login(self.nomoney)
        token = the_all[0]
        userid = the_all[1]
        # 获取新手机号码
        with open(self.txt_path + 'phonechange.txt', 'r+') as fp:
            tf = fp.readlines()
        new_num = tf[0].strip('\n')
        innum = int(new_num)
        # 清空phonechange.txt
        with open(self.txt_path + 'phonechange.txt', 'w+') as f:
            f.write('')
        del tf[0]  # 删除号码列表中第一个号码，将列表写入文件，下次调用就可以再调用第一个号码，并且不重复,省掉了count文件
        # 将去掉第一个号码的列表写入文件
        for i in range(len(tf)):
            with open(self.txt_path + 'phonechange.txt', 'a+') as p:
                p.write(tf[i])
        sql = "INSERT INTO yjd_verify_sms (mobile,smscode,num,senttime,ip) VALUES (%d,'111111',1,%d,'192.168.100.219')" % (inpn, nt)
        self.cur.execute(sql)
        self.conn.commit()
        r = requests.post(url=self.sign_url + 'V_2_0/msg/compare/1',
                          data={'msgCode': '111111', 'access_token': token, 'user_id': userid, 'api_request_way': '1'})
        vt = r.json()['data']['valid_token']
        sql2 = "DELETE FROM yjd_verify_sms WHERE mobile=%d" % inpn
        self.cur.execute(sql2)
        self.conn.commit()
        r2 = requests.post(url=self.sign_url + 'V_2_0/safe/mpNumber/msg',
                           data={'mpNumber': new_num, 'valid_token': vt, 'access_token': token, 'user_id': userid,
                                 'api_request_way': '1'})
        self.assertEqual(u'短信已发送到您的150' + '****' + new_num[7:] + u'手机!', r2.json()['data']['message'])
        sql3 = "SELECT smscode FROM yjd_verify_sms WHERE mobile=%d" % innum
        self.cur.execute(sql3)
        sms = self.cur.fetchall()
        mes = sms[0][0]
        r3 = requests.post(url=self.sign_url + 'V_2_0/safe/mpNumber/modify',
                           data={'access_token': token, 'user_id': userid, 'api_request_way': '1', 'mpNumber': new_num,
                                 'msgCode': mes})
        self.assertEqual(r3.json()['message'], u'手机号已变更')
        with open(self.txt_path + 'phonechange.txt', 'a+') as lp:
            lp.write(new_num + '\n')

    def test_13(self):
        '''我的代金券详情'''
        # 登录
        log = add_md5.the_login()
        login = log.web_login('18386249157')
        token = login[0]
        userid = login[1]
        # 查询代金券
        r = requests.post(url=self.sign_url + 'V_2_0/my/fundsVolum',
                          data={'access_token': token, 'user_id': userid, 'api_request_way': '1'})
        self.assertEqual(r.json()['state'], '1')

    def test_14(self):
        '''我的加息券详情'''
        # 登录
        log = add_md5.the_login()
        login = log.web_login('18386249157')
        token = login[0]
        userid = login[1]
        # 查询加息券
        r = requests.post(self.sign_url + 'V_2_0/my/reiselist',
                          data={'access_token': token, 'user_id': userid, 'api_request_way': '1'})
        self.assertEqual(r.json()['state'], '1')

    def test_15(self):
        '''理财返现金详情，帐号用购买债权的'''
        # 登录
        log = add_md5.the_login()
        login = log.web_login(self.buyusername)
        token = login[0]
        userid = login[1]
        # 查询理财返现金
        r = requests.post(url=self.sign_url + 'V_2_0/my/volumeFinancial',
                          data={'access_token': token, 'user_id': userid, 'api_request_way': '1'})
        print r.json()['data']

    def test_16(self):
        '''企业法人注册'''
        # 将手机号的验证码插入到数据库中
        nt = time.time()
        nt = int(nt)
        sql1 = "INSERT INTO yjd_verify_sms (mobile,smscode,num,senttime,ip) VALUES (%d,'111111',1,%d,'192.168.100.219')" % (
        18956397182, nt)
        self.cur.execute(sql1)
        # 加密
        pw = add_md5.add_md5()
        pwd = pw.am5('a123456789')
        r = requests.post(url=self.sign_url + 'V_2_0/companyApply/submit', data={'protocol': '1',
                                                                                 'msgCode': 111111,
                                                                                 'userName': '陈边边',
                                                                                 'mobile': 18956397182,
                                                                                 'password': pwd,
                                                                                 'companyName': '上海市青浦区中中医院',
                                                                                 'companyCode': '545431231',
                                                                                 'idName': '渐渐全',
                                                                                 'idCard': '11010119500101013X',
                                                                                 'bank': '中国银行',
                                                                                 'bankAddress': '上海市嘉定区黄渡镇八路路分行',
                                                                                 'city': '上海上海市',
                                                                                 'bankCode': '6216611500001664560'})
        print r.json()['message']
        # 删除验证码
        sql2 = "DELETE FROM yjd_verify_sms WHERE mobile=%d" % 18956397182
        self.cur.execute(sql2)
        # 删除账号
        sql3 = "DELETE FROM yjd_user WHERE mobile=%d" % 18956397182
        self.cur.execute(sql3)

    def test_9(self):
        '''逾期还款'''
        print u'逾期还款'
        # 1、首先修改标的limit=2的交易id的还款时间 小于当前时间86400s，这里逾期2天
        # 2、获取arrears_form中的price,利息（intetest）,月利率0.0025，账户管理费0.25元，
        # 3、计算逾期利息+逾期账户管理费+逾期罚息+逾期罚账户管理费
        # 4、计算逾期1天后应还总额
        # 本期应还总额=应还本金+应还利息+账户管理费+逾期利息+逾期账户管理费+逾期罚息+逾期罚账户管理费
        #   a、逾期利息=本金*投资人利率（年化）/365*逾期天数 （开发代码调整计算：当月利息*12/365*205 ，因获取不到产品利息）
        #   b、逾期账户管理费=本金*管理费利率（月利率）/30*逾期天数
        #   c、逾期罚息=（本金+利息）*0.0005*逾期天数
        #   d、逾期罚账户管理费=账户管理费*0.0005*逾期天数'''
        with open(self.txt_path + 'borrow_id.txt', 'r+') as fp:
            bid = fp.readline()
        bid = int(bid)
        now_time = int(time.time())
        print u'当前时间:' + str(now_time)
        reday = now_time - 86440 * 3  # 还款逾期两天
        # 将arrears_form和profit_form数据库还款时间改成设置好的reday
        sql1 = "UPDATE yjd_arrears_form SET reday=%d WHERE borrow_id=%d AND `limit`=2" % (reday, bid)
        self.cur.execute(sql1)  # 借款人表修改完成
        self.conn.commit()
        sql2 = "UPDATE yjd_profit_form SET reday=%d WHERE borrow_id=%d AND `limit`=2" % (reday, bid)
        self.cur.execute(sql2)  # 投资人表修改完成
        self.conn.commit()
        #############################
        #                           #
        #        设置逾期完成
        #                           #
        #############################

        #借款人金额提现
        tx=admin_sp.sp()
        tx.tixian()
        #

        # 获取应还本金，应还利息，账户管理费由于脚本固定借款10000，所以为25
        zjk = 10000  # 总借款金额，由于系统改动，默认最低借款改为10000
        sql3 = "SELECT capital FROM yjd_arrears_form WHERE borrow_id=%d AND `limit`=2" % bid
        self.cur.execute(sql3)
        benjin = self.cur.fetchall()
        capital = benjin[0][0]
        capital = float(capital)
        sql4 = "SELECT interest FROM yjd_arrears_form WHERE borrow_id=%d AND `limit`=2" % bid
        self.cur.execute(sql4)
        lixi = self.cur.fetchall()
        interest = lixi[0][0]
        interest = float(interest)
        # 打印本期的本金和利息
        print u'当期本金' + str(capital)
        print u'当期利息' + str(interest)
        # 计算逾期利息,年华都设置为10.5%
        # 逾期利息=本金*投资人利率（年化）/365*逾期天数
        ylx = capital * 0.1 / 365 * 2
        ylx = round(ylx, 2)  # 精确到小数点后二位
        print u'逾期利息:' + str(ylx)
        # 计算逾期账户管理费
        # 逾期账户管理费=本金*管理费利率（月利率）/30*逾期天数
        ygl = capital * 0.0025 / 30 * 2
        ygl = round(ygl, 2)
        print u'逾期账户管理费:' + str(ygl)
        # 计算逾期罚息
        # 逾期罚息=（本金+利息）*0.0005*逾期天数，此处本金为本月应还本金
        yfx = (capital + interest) * 0.0005 * 2
        yfx = round(yfx, 2)
        print u'逾期罚息：' + str(yfx)
        # 计算逾期罚账户管理费
        # 逾期罚账户管理费=账户管理费*0.0005*逾期天数
        yfgl = 25 * 0.0005 * 2
        yfgl = round(yfgl, 2)
        print u'逾期罚账户管理费：' + str(yfgl)
        # 计算逾期还款总额
        total_repay = interest + 25+ylx+ygl+yfx+yfgl
        print '逾期还款总额：' + str(total_repay)
        '''调用还款接口还款，从数据库调出借款人还款前和还款后的金额，计算还款前减去total_repay是否等于还款后的金额'''
        # 获取还款前金额
        sql5 = "SELECT available FROM yjd_bank_depo_account WHERE bank_card_mobile=%d" % self.JKR
        cashb = 200
        sql6 = "SELECT id FROM yjd_arrears_form WHERE borrow_id=%d AND `limit`=2" % bid
        self.cur.execute(sql6)
        reid = self.cur.fetchall()
        reid = str(reid[0][0])  # 还款id

        #平台逾期垫付
        tx.dianfu()

        #借款人充值金额还款
        tx.chongzhi()

        # 登录
        log = add_md5.the_login()
        login = log.web_login(self.JKR)
        token = login[0]
        user_id = login[1]
        # 还款
        r = requests.post(url=self.sign_url + 'V_2_0/borrow/repaysubmit/' + reid,
                          data={'access_token': token, 'user_id': user_id, 'api_request_way': '1', 'noPwd': 1})
        print r.json()['message']
        # 获取逾期还款后的金额
        self.cur.execute(sql5)
        acash = self.cur.fetchall()
        casha = float(acash[0][0])
        # 判断金额
        self.assertEqual(cashb - total_repay, casha)

    def test_18(self):
        # 非借款人借款，非投资人投资
        print u'投资人借款'
        lo = add_md5.the_login()
        log = lo.web_login(15848657321)
        token = log[0]
        user_id = log[1]
        r1 = requests.post(url=self.sign_url + 'V_2_0/apply/step1submit', data={'is_hospital': 1,
                                                                                'class': 5,
                                                                                'title': '接口测试' + str(time.time()),
                                                                                'yongtu': 1,
                                                                                'price': 10000.00,
                                                                                'apr': 10.00,
                                                                                'limit': 12,
                                                                                'mode': 2,
                                                                                'content': '测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试',
                                                                                'access_token': token,
                                                                                'user_id': user_id,
                                                                                'api_request_way': '1'})
        self.assertEqual(u'您是出借人，不能借款。', r1.json()['message'])
        print u'借款人投资'
        log2 = lo.web_login(self.JKR)
        token2 = log2[0]
        user_id2 = log2[1]
        r2 = requests.post(url=self.sign_url + 'V_2_0/invest/tb', data={'borrow_id': 9397,
                                                                        'tbprice': 10000,
                                                                        'channel': '2',
                                                                        'access_token': token2,
                                                                        'user_id': user_id2,
                                                                        'api_request_way': '1'})
        self.assertEqual(u'您不能进行出借。', r2.json()['message'])

    def test_19(self):
        # 未开标时投标
        print u'未开标时投标'
        # 1、借款
        jie = jiekuan.jie(10.5,12)
        jie.jk1()
        jie.jk2()
        jie.jk3()
        # 2、审批
        spi = admin_sp.sp()
        spi.second_sp123()
        time.sleep(10)
        borrow_id = spi.borrow()
        log = add_md5.the_login()
        tok = log.web_login(self.buyusername)
        token = tok[0]
        user_id = tok[1]
        # 投标
        r = requests.post(url=self.sign_url + 'V_2_0/invest/tb', data={'borrow_id': borrow_id,
                                                                       'tbprice': 100,
                                                                       'channel': '2',
                                                                       'access_token': token,
                                                                       'user_id': user_id,
                                                                       'api_request_way': '1'})
        self.assertEqual(r.json()['message'], u'投标尚未开始!')

    def test_20(self):
        # 活动奖励发放
        print u'发放代金券'
        login = add_md5.the_login()
        userid = login.web_login(18386249157)
        userid = userid[1]
        hdtype = 'huodong'
        orderid = 5
        amount = 100
        ordertime = int(time.time())
        endtime = ordertime + 86400
        linkage_value = 96
        opttype = 1
        extend = 100
        sms = 0
        r = requests.post(url=self.sign_url + 'activityPrize/happy', data={'app_user': 1, 'app_type': hdtype,
                                                                           'app_msg': {'order_id': orderid,
                                                                                       'user_id': userid,
                                                                                       'amount': amount,
                                                                                       'order_time': ordertime,
                                                                                       'end_time': endtime,
                                                                                       'start_time': ordertime,
                                                                                       'linkage_value': linkage_value,
                                                                                       'opt_type': opttype,
                                                                                       'extend1': extend,
                                                                                       'is_sms_flag': sms}})
        print r.json()['message']

    def test_21(self):
        # 0.3,0.8,1.0,1.5,2.0，3.0，不同月份借款,债权折让率0.8
        # 借款3个月
        three_month = jiekuan.jie(8, 3)
        t31 = three_month.jk_m1()
        self.assertEqual(t31, u'提交成功!')
        t32 = three_month.jk_m2()
        self.assertEqual(t32, u'提交成功!')
        t33 = three_month.jk_m3()
        self.assertEqual(t33, u'提交成功!')
        # 审批
        snp = admin_sp.sp()
        snp.sp123()
        # 获取borrowid
        b_id = snp.borrow()
        b_id = str(b_id)
        # 投标-债转-购买债权，折让率0.8
        gogo=jiekuan.tb_buyzq(b_id,10000.00,0.8,1,2)
        re1=gogo.go()
        self.assertEqual(re1,u'恭喜您购买成功!')
    def test_22(self):
        #借6个月，折让率1.0
        six_month=jiekuan.jie(9.5,6)
        t61=six_month.jk_m1()
        self.assertEqual(t61,u'提交成功!')
        t62=six_month.jk_m2()
        self.assertEqual(t62,u'提交成功!')
        t63=six_month.jk_m3()
        self.assertEqual(t63,u'提交成功!')
        #审批
        snp=admin_sp.sp()
        snp.sp123()
        #获取borrowid
        b_id=snp.borrow()
        b_id=str(b_id)
        #投标-债转-购买债权，折让率1.0
        gogo=jiekuan.tb_buyzq(b_id,10000.00,1.0,1,2)
        re1=gogo.go()
        self.assertEqual(re1,u'恭喜您购买成功!')
    def test_23(self):
        #借款18个月，折让率1.5
        twelve_month=jiekuan.jie(11,18)
        t121=twelve_month.jk_m1()
        self.assertEqual(t121,u'提交成功!')
        t122=twelve_month.jk_m2()
        self.assertEqual(t122,u'提交成功!')
        t123=twelve_month.jk_m3()
        self.assertEqual(t123,u'提交成功!')
        #审批
        snp=admin_sp.sp()
        snp.sp123()
        #获取borrowid
        b_id=snp.borrow()
        b_id=str(b_id)
        #耶你懂的，折让率2.0
        gogo=jiekuan.tb_buyzq(b_id,10000.00,1.5,1,2)
        re1=gogo.go()
        self.assertEqual(re1,u'恭喜您购买成功!')
    def test_24(self):
        #借款12个月，折让率2.0
        twelve_month = jiekuan.jie(10.5, 12)
        t121 = twelve_month.jk_m1()
        self.assertEqual(t121, u'提交成功!')
        t122 = twelve_month.jk_m2()
        self.assertEqual(t122, u'提交成功!')
        t123 = twelve_month.jk_m3()
        self.assertEqual(t123, u'提交成功!')
        # 审批
        snp = admin_sp.sp()
        snp.sp123()
        # 获取borrowid
        b_id = snp.borrow()
        b_id = str(b_id)
        #折让率2.0
        gogo=jiekuan.tb_buyzq(b_id,10000.00,2.0,1,2)
        re1=gogo.go()
        self.assertEqual(re1,u'恭喜您购买成功!')
    def test_25(self):
        #借款12个月，折让率3.0
        twelve_month = jiekuan.jie(10.5, 12)
        t121 = twelve_month.jk_m1()
        self.assertEqual(t121, u'提交成功!')
        t122 = twelve_month.jk_m2()
        self.assertEqual(t122, u'提交成功!')
        t123 = twelve_month.jk_m3()
        self.assertEqual(t123, u'提交成功!')
        # 审批
        snp = admin_sp.sp()
        snp.sp123()
        # 获取borrowid
        b_id = snp.borrow()
        b_id = str(b_id)
        #折让率3.0
        gogo = jiekuan.tb_buyzq(b_id, 10000.00, 3.0, 1, 2)
        re1 = gogo.go()
        self.assertEqual(re1, u'恭喜您购买成功!')
    def test_26(self):
        #让利金为0
        twelve_month = jiekuan.jie(10.5, 12)
        t121 = twelve_month.jk_m1()
        self.assertEqual(t121, u'提交成功!')
        t122 = twelve_month.jk_m2()
        self.assertEqual(t122, u'提交成功!')
        t123 = twelve_month.jk_m3()
        self.assertEqual(t123, u'提交成功!')
        # 审批
        snp = admin_sp.sp()
        snp.sp123()
        # 获取borrowid
        b_id = snp.borrow()
        b_id = str(b_id)
        # 折让率3.0
        gogo = jiekuan.tb_buyzq(b_id, 10000.00, 3.0, 1, 0)
        re1 = gogo.go()
        self.assertEqual(re1, u'恭喜您购买成功!')

if __name__ == '__main__':
    unittest.main()
