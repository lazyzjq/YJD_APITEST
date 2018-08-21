#coding=utf-8
import requests,hashlib,unittest,urllib,pymysql,time,random,json,configparser,admin_sp,BSTestRunner
from defs import shenfenzheng,add_md5,get_password,jiekuan
#线上测试
class online(unittest.TestCase):
    def setUp(self):
        self.sign_url='http://api.yijiedai.com/'
        self.url='http://api.yijiedai.org/'
        self.username='18016349627'
        m = hashlib.md5()
        m.update('dayangquanfei')
        self.password = m.hexdigest()
        s = hashlib.md5()
        s.update('854518')
        self.pwd = s.hexdigest()
        self.r = requests.post(url=self.sign_url + 'V_2_0/login/handle',
                          data={'username': self.username, 'password': self.password, 'api_request_way': '1'})
        self.token = self.r.json()['data']['access_token']
        self.user_id = self.r.json()['data']['user_id']
    def tearDown(self):
        pass

    def test_1(self):
       
        print u'注册'
        print u'第一步'
        r1=requests.post(url=self.sign_url+'V_2_0/reg/msg1',data={'mpNumber':self.username,'imageCodeUid':'afsadsd','imageCode':'dfgt'})
        print r1.json()['message']
        print u'第二步'
        r2=requests.post(url=self.sign_url+'V_2_0/reg/step/1',data={'mpNumber':self.username,'msgCode':'5455asd'})
        print r2.json()['message']
        print u'第三步'
        r3=requests.post(url=self.sign_url+'V_2_0/reg/step/2',data={'mpNumber':self.username,'password':self.password,'device_no':'dasdasd','mobile_type':'ios','valid_token':'asdsasafsa'})
        print r3.json()['message']
    def test_2(self):
        
        print u'登录'
        r=requests.post(url=self.sign_url+'V_2_0/login/handle',data={'username':self.username,'password':self.password,'api_request_way':'1'})
        print r.json()
        print r.json()['message']


    def test_3(self):
        
        print u'投标'
        r = requests.post(url=self.sign_url + 'V_2_0/login/handle',
                          data={'username': self.username, 'password': self.password, 'api_request_way': '1'})
        token = r.json()['data']['access_token']
        user_id = r.json()['data']['user_id']
        r1=requests.post(url=self.sign_url+'V_2_0/invest/tb',data={'borrow_id':9743,'tbprice':100,'channel':'2','access_token':token,'user_id':user_id,'api_request_way':'1'})
        print r1.json()['message']
    #@unittest.skip(u'绅士道')
    def test_4(self):
        
        print u'购买债权'
        r = requests.post(url=self.sign_url + 'V_2_0/login/handle',data={'username': self.username, 'password': self.password, 'api_request_way': 2})
        token = r.json()['data']['access_token']
        user_id = r.json()['data']['user_id']
        r1=requests.post(url=self.sign_url+'V_2_0/invest/buycreditor',data={'access_token':token,'user_id':user_id,'api_request_way':2,'id':165464,'channel':2})
        print r1.json()['message']
    def test_5(self):
        
        print u'债转'
        r = requests.post(url=self.sign_url + 'V_2_0/login/handle',data={'username': self.username, 'password': self.password, 'api_request_way': 1})
        token = r.json()['data']['access_token']
        user_id = r.json()['data']['user_id']
        r1=requests.post(url=self.sign_url+'V_2_0/creditor/transferApply',data={'access_token':token,'user_id':user_id,'api_request_way':1,'creditorId':'544545','transferNum':2,'discApr':0.5,'discount_per_partion':1})
        print r1.json()['message']
    def test_6(self):
        print u'借款第一步'
        r = requests.post(url=self.sign_url + 'V_2_0/login/handle',
                          data={'username': self.username, 'password': self.password, 'api_request_way': '1'})
        token = r.json()['data']['access_token']
        user_id = r.json()['data']['user_id']
        r1=requests.post(url=self.sign_url+'V_2_0/apply/step1submit',data={'is_hospital':1,
                                                                                        'class':5,
                                                                                        'title':'接口测试',
                                                                                        'yongtu':1,
                                                                                        'price':100.00,
                                                                                        'apr':10.00,
                                                                                        'limit':12,
                                                                                        'mode':2,
                                                                                        'content':'测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试',
                                                                                        'access_token':token,
                                                                                        'user_id':user_id,
                                                                                        'api_request_way':'1'})
        print r1.json()['message']
    def test_7(self):
        print u'借款第二步'
        r = requests.post(url=self.sign_url + 'V_2_0/login/handle',
                          data={'username': self.username, 'password': self.password, 'api_request_way': '1'})
        token = r.json()['data']['access_token']
        user_id = r.json()['data']['user_id']
        r1=requests.post(url=self.sign_url+'V_2_0/apply/step2submit',data={'xueli':1,
                                                                                       'hukou':1,
                                                                                       'city':1,
                                                                                       'address':'上受到了卡萨帝',
                                                                                       'tel':'18655469874',
                                                                                       'zip':1,
                                                                                       'hunyin':1,
                                                                                       'iszinv':1,
                                                                                       'z_name':'绅士道',
                                                                                       'z_type':1,
                                                                                       'z_mobile':18699959878,
                                                                                       'o_name':'来咯是',
                                                                                       'o_type':1,
                                                                                       'o_mobile':18611122233,
                                                                                       'work_class':1,
                                                                                       'work_city':1,
                                                                                       'work_shouru':8000,
                                                                                       'work_guimo':100,
                                                                                       'work_nianxian':1,
                                                                                       'work_tel':'18955442266',
                                                                                       'work_address':'撒大师傅萨芬大事',
                                                                                       'work_zhiwei':'大老板',
                                                                                       'h_name':'十点多睡的',
                                                                                       'h_xingzhi':1,
                                                                                       'h_leibie':1,
                                                                                       'h_dengji':1,
                                                                                       'c_name':'说是道非萨芬',
                                                                                       'c_xingzhi':1,
                                                                                       'c_hangye':1,
                                                                                       'isfang':1,
                                                                                       'isfangdai':1,
                                                                                       'ische':1,
                                                                                       'ischedai':1,
                                                                                       'access_token': token,
                                                                                       'user_id': user_id,
                                                                                       'api_request_way': '1'
                                                                                       })
        print r1.json()['message']
    def test_8(self):
        print u'借款第三步'
        r = requests.post(url=self.sign_url + 'V_2_0/login/handle',
                          data={'username': self.username, 'password': self.password, 'api_request_way': '1'})
        token = r.json()['data']['access_token']
        user_id = r.json()['data']['user_id']
        r1=requests.post(url='http://api.yijiedai.com/V_2_0/apply/step4submit',data={'access_token': token,
                                                                                       'user_id': user_id,
                                                                                       'api_request_way': '1'})
        print r1.json()['message']
    def test_9(self):
        print u'标的还款信息'
        r = requests.post(url=self.sign_url + 'V_2_0/borrow/arrearsforms/9001')
        print r.json()
    def test_a(self):
        print u'定期投标-标的详情'
        r = requests.post(url=self.sign_url + 'V_2_0/borrow/detail/9000')
        print r.json()
    def test_b(self):
        print u'我要投标页面信息'
        r=requests.post(url=self.sign_url+'V_2_0/invest/getMyBid/9000',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_c(self):
        print u'定期投标-获取可全部投入的金额'
        r=requests.post(url=self.sign_url+'V_2_0/invest/getUserCanInvestPriceByBorrowId/9000',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_d(self):
        print u'图片验证码'
        r=requests.post(url=self.sign_url+'V_2_0/imageCode/index')
        print r.json()
    def test_e(self):
        print u'代金券详情'
        r=requests.post(url=self.sign_url+'V_2_0/my/fundsVolum',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_f(self):
        print u'加息券详情'
        r=requests.post(url=self.sign_url+'V_2_0/my/raiseInterest',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_g(self):
        print u'交易记录'
        r=requests.post(url=self.sign_url+'V_2_0/funds/detail',data={'queryType':2,'queryStatus':-1,'queryRange':6,'rows':10,'page':'1','access_token':self.token,'user_id':self.user_id,'api_request_way':1})
        print r.json()
    def test_h(self):
        print u'投资详情'
        r=requests.post(url=self.sign_url+'V_2_0/financecalendar/detail',data={'borrow_id':1000,'creditor_id':1000,'access_token':self.token,'user_id':self.user_id})
        print r.json()
    def test_i(self):
        print u'预约券详情'
        r=requests.post(url=self.sign_url+'V_2_0/my/subVolum',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_j(self):
        print u'企业法人注册'
        r=requests.post(url=self.sign_url+'V_2_0/companyApply/submit',data={'protocol':1,'msgCode':'asd451','userName':'sadsd12','mobile':1122511220,'password':'4sdadas44a2',
                                                                            'companyName':u'但是放到沙发上','companyCode':'asdsad','idName':'sadsadd','idCard':'asdsad',
                                                                            'bank':'asdsad','bankAddress':'sadfsdfsa','city':'sadsa','bankCode':'asdsadsa'})
        print r.json()['message']
    def test_k(self):
        print u'修改银行卡接口'
        r=requests.post(url=self.sign_url+'V_2_0/cash/updateMyBankCard',data={'bankcode':'asdsadsad','city':'sdada','bankaddress':'sadsadsad'})
        print r.json()
    def test_l(self):
        print u'还款页面接口详情'
        r=requests.post(url=self.sign_url+'V_2_0/borrow/repayment/1000',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_m(self):
        print u'更新企业联络人信息'
        r=requests.post(url=self.sign_url+'V_2_0/info/update/enterprise/contacts',data={'cfo_name':'fdgdfg','cfo_mobile':'hfghfgh',
                                                                                        'actual_name':'gfhfgh',
                                                                                        'actual_mobile':'hgfhgfhfgh',
                                                                                        'opt_name':'ghgfhgfh',
                                                                                        'opt_mobile':'fgdfgfgd','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()['message']
    def test_n(self):
        print u'更新企业基本情况信息'
        r=requests.post(url=self.sign_url+'V_2_0/info/update/enterprise/basic',data={'hukou':'sadas','work_class':'dsadsa','work_address':'sadsaasd',
                                                                                     'h_mianji':'sadsa','c_cap_type':'sadasd','c_rent':'asdsad',
                                                                                     'c_cap_ex':'adssad','c_major':'sadsad','h_dengji':'sadsad',
                                                                                     'h_yibao':'asdsa','h_nonhe':'sadsad','work_guimo':'sadsad',
                                                                                     'ex_shouru':'asdsad','ex_profit':'sadasd','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()['message']
    def test_o(self):
        print u'存管用户分组'
        r=requests.post(url=self.sign_url+'V_2_0/depo/user/status',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_p(self):
        print u'快捷登录第一步校验短信验证码'
        r=requests.post(self.sign_url+'V_2_0/login/quicklogin/handle',data={'mobile':'18016931582','sms':'asdsad',})
        print r.json()
    def test_q(self):
        print u'银行卡卡bin查询接口'
        r=requests.post(url=self.sign_url+'V_2_0/auth/validator',data={'bankCode':'211211212112'})
        print r.json()
    def test_r(self):
        print u'提现认证银行卡PC端'
        r=requests.post(url=self.sign_url+'V_2_0/auth/authBankCard',data={'idname':'sad','idcard':'sadasd','bankCode':'asdasd','mobile':'sadas','city':'sadasd','bankAddress':'1511233213'})
        print r.json()
    def test_s(self):
        print u'PC四要素认证支持银行卡列表'
        r=requests.post(url=self.sign_url+'V_2_0/auth/fourBankList')
        print r.json()
    def test_t(self):
        print u'官网2.0未绑卡充值'
        r=requests.post(url=self.sign_url+'V_2_0/recharge/generatorOrder',data={'orderAmount':100,'certNo':'310229195652120202','realName':u'爱仕达',
                                                                                'bankCardNo':'51651a1sd51sa515','mpNumber':'5456sad4','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_u(self):
        print u'官网2.0提现接口'
        r=requests.post(url=self.sign_url+'V_2_0/cashOut/apply',data={'price':111,'bankid':'asdsad','paypassword':'sdasd111','mobile':'123132561','city':'sadsad','bankaddress':'sadsadsad',
                                                                      'access_token': self.token,
                                                                      'user_id': self.user_id, 'api_request_way': '1'})
        print r.json()
    def test_v(self):
        print u'将普通账户资金全部转到存管账户'
        r=requests.post(url=self.sign_url+'V_2_0/bankDepoAccount/transfer')
        print r.json()
    def test_w(self):
        print u'存管账户--提现申请'
        r=requests.post(url=self.sign_url+'V_2_0/bankDepo/cashOut',data={'price':100,'channel':1,'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_x(self):
        print u'将理财卡账户资金转到存管账户'
        r=requests.post(url=self.sign_url+'V_2_0/bankDepoAccount/lckTransfer',data={'price':100,'card_id':'1512001223221','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_y(self):
        print u'存管账户银行卡信息'
        r=requests.post(url=self.sign_url+'V_2_0/bankDepoAccount/bank',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_z(self):
        print u'登录用户添加自身到白名单'
        r=requests.post(url=self.sign_url+'V_2_0/depository/whitelists/submit/self')
        print r.json()
    def test_A(self):
        print u'存管用户开户'
        r=requests.post(url=self.sign_url+'V_2_0/bankDepoAccount/openAccount',data={'name':'sadsa','idcard':'sadsa54das4da','user_type':1,'user_role':1})
        print r.json()
    def test_B(self):
        print u'存管用户绑卡'
        r=requests.post(url=self.sign_url+'V_2_0/bankDepoAccount/bindCard',data={'bank_card_no':'sadasd5as5asd','bank_card_mobile':'234654156132','idname':'sadasd',
                                                                            'idcard':'sadsad','user_type':2})
        print r.json()
    def test_C(self):
        print u'APPV2.1.9发现'
        r=requests.post(url=self.sign_url+'V_2_0/union/discovery')
        print r.json()
    def test_D(self):
        print u'预约标预约'
        r=requests.post(url=self.sign_url+'V_2_0/reservation/submit',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_E(self):
        print u'取消预约记录'
        r=requests.post(url=self.sign_url+'V_2_0/reservation/cancel',data={'reservation_id':'54153','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_F(self):
        print u'预约标-提交人工筛选'
        r=requests.post(url=self.sign_url+'V_2_0/reservation/filter',data={'borrow_id':'100000','user_ids':'dfdsf','prices':11111,'sign':'sadasd'})
        print r.json()
    def test_G(self):
        print u'预约标-筛选数据测试校验接口'
        r=requests.post(url=self.sign_url+'V_2_0/reservation/filterTest',data={'borrow_id':'100000','user_ids':'dfdsf','prices':11111,'sign':'sadasd'})
        print r.json()
    def test_H(self):
        print u'申请电子签证-个人'
        r=requests.post(url=self.sign_url+'V_2_0/evidence/apply/signature/personal',data={'msgCode':'dsad','realname':'dasdsa','idcard':'dadsd','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_I(self):
        print u'申请电子签章-企业'
        r=requests.post(url=self.sign_url+'V_2_0/evidence/apply/signature/enterprise',data={'msgCode':'sadasd','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_J(self):
        print u'下载电子签章图片'
        r=requests.post(url=self.sign_url+'V_2_0/evidence/signature/stamp/download',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_K(self):
        print u'下载合同文件PDF'
        r=requests.post(url=self.sign_url+'V_2_0/evidence/signature/file/content',data={'local_file_id':'111','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_L(self):
        print u'签章第一步'
        r=requests.post(url=self.sign_url+'V_2_0/evidence/signature/stamp/verify',data={'local_file_id':'111','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_M(self):
        print u'签章第二步'
        r=requests.post(url=self.sign_url+'V_2_0/evidence/signature/stamp/create',data={'local_file_id':'111','access_token':self.token,'user_id':self.user_id,'api_request_way':'1','msgCode':'sadasd'})
        print r.json()
    def test_N(self):
        print u'获取图片验证码信息'
        r=requests.post(url=self.sign_url+'V_2_0/imageCode/index',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_O(self):
        print u'新版人人推广-获取当前推广人的一些信息'
        r=requests.post(url=self.sign_url+'V_2_0/spread/spreadInfo',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_P(self):
        print u'调api推送app消息'
        r=requests.post(url=self.sign_url+'V_2_0/push/message',data={'app_user':'sadsad','app_msg':'dsadas'})
        print r.json()
    def test_Q(self):
        print u'添加自动白名单提醒'
        r=requests.post(url=self.sign_url+'V_2_0/userAutoInvest/reminder',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_R(self):
        print u'用户手机解绑申请'
        r=requests.post(url=self.sign_url+'V_2_0/userInfoChanage/mobileApply',data={'remark':'dasd','tel':'sadsa','channel':1,'Filedata':'sadsad','filePaths':'asdsad'})
        print r.json()
    def test_S(self):
        print u'用户银行卡解绑申请'
        r=requests.post(url=self.sign_url+'V_2_0/userInfoChanage/bankApply',data={'remark':'dasd','tel':'sadsa','channel':1,'filePaths':'asdsad'})
        print r.json()
    def test_T(self):
        print u'用户触达'
        r=requests.post(url=self.sign_url+'recommend/informList',data={'msgType':1,'page':1})
        print r.json()
    def test_U(self):
        print u'风险评测信息'
        r=requests.post(url=self.sign_url+'V_2_0/evaluate/info',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_V(self):
        print u'过期债权列表'
        r=requests.post(url=self.sign_url+'V_2_0/creditor/expired',data={'page':1,'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_W(self):
        print u'过期债权收益列表'
        r=requests.post(url=self.sign_url+'V_2_0/creditor/expired/ProfitList',data={'creditor_id':1,'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_X(self):
        print u'提额券详情'
        r=requests.post(url=self.sign_url+'V_2_0/my/raiseLimit/detail',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_Y(self):
        print u'债转让利金信息后台配置'
        r=requests.post(url=self.sign_url+'V_2_0/creditor/discount/info',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_Z(self):
        print u'银行存管充值接口'
        r=requests.post(url=self.sign_url+'V_2_0/rech/bankDepo/pay',data={'orderAmount':100,'type':'bank_pc_auth','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_a1(self):
        print u'活动预约券领取接口'
        r=requests.post(url=self.sign_url+'V_2_0/subscribe/get',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_a2(self):
        print u'网银充值（普通用户）'
        r=requests.post(url=self.sign_url+'V_2_0/pay/netbank',data={'price':'100','idbank':'1441','access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_a3(self):
        print u'快捷网银充值接口（银行存管用户）'
        r=requests.post(url=self.sign_url+'V_2_0/pay/bankDepo',data={'price':100,'type':'bank_pc'})
        print r.json()
    def test_a4(self):
        print u'充值完成页面需要新增接口'
        r=requests.post(url=self.sign_url+'V_2_0/recommend/after/recharge')
        print r.json()
    def test_a5(self):
        print u'列表弹窗接口'
        r=requests.post(url=self.sign_url+'V_2_0/invest/prompt')
        print r.json()
    def test_a6(self):
        print u'获取借款人待还金额信息'
        r=requests.post(url=self.sign_url+'V_2_0/borrow/repayFunds',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_a7(self):
        r=requests.post(url=self.sign_url+'V_2_0/my/newRaiseInterest',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':'1'})
        print r.json()
    def test_a8(self):
        print u'根据债权id，份数，折让率计算预计到账金额'
        r=requests.post(url=self.sign_url+'V_2_0/creditor/getCreditorTransferCounter',data={'creditor_id':2060,'transferNum':'1','disc_apr':0.3,'discount_per_partion':2,
                                                                                            'access_token':self.token,'user_id':self.user_id,'api_request_way':1})
        print r.json()['message']
    def test_a9(self):
        print u'获取银行卡历史列表'
        r=requests.post(url=self.sign_url+'V_2_0/auth/bankCodeHistory',data={'access_token':self.token,'user_id':self.user_id,'api_request_way':1})
        print r.json()['data']
    def test_a10(self):
        print u'认证银行列表'
        r=requests.post(url=self.sign_url+'V_2_0/auth/authBankList')
        print r.json()['data']
    def test_a11(self):
        print u'获取所有省份'
        r=requests.post(url=self.sign_url+'V_2_0/getProvince')
        print r.json()['data']
    def test_a12(self):
        print u'提现记录'
        r=requests.post(url=self.sign_url+'V_2_0/cash/applyRecord',data={'rows':1,'page':1,'access_token':self.token,'user_id':self.user_id,'api_request_way':1})
        print r.json()['data']['page']
if __name__=='__main__':
    unittest.main()

