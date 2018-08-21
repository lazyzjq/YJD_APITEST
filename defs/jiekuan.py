#coding=utf-8
import requests,add_md5,time,pymysql,admin_sp

timee=time.time()
timee=str(timee)
url='http://api.yjdtest.cn/'
class jie():
    def __init__(self,apr,limit,price=10000.00):
        self.apr=apr
        self.limit=limit
        self.price=price
    def jk1(self):
        lo=add_md5.the_login()
        log=lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r1=requests.post(url=url+'V_2_0/apply/step1submit',data={   'is_hospital':1,
                                                                                        'class':5,
                                                                                        'title':'接口测试'+timee,
                                                                                        'yongtu':1,
                                                                                        'price':self.price,
                                                                                        'apr':self.apr,
                                                                                        'limit':self.limit,
                                                                                        'mode':2,
                                                                                        'content':'测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试',
                                                                                        'access_token':token,
                                                                                        'user_id':user_id,
                                                                                        'api_request_way':'1'})
        return r1.json()['message']
    def jk2(self):
        lo = add_md5.the_login()
        log = lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r2=requests.post(url=url+'V_2_0/apply/step2submit',data={'user_id':user_id,
                                                                                       'access_token':token,
                                                                                       'api_request_way':'1',
                                                                                       'xueli':1,
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
                                                                                       'ischedai':1
                                                                                       })
        return r2.json()['message']

    def jk3(self):
        lo = add_md5.the_login()
        log = lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r3=requests.post(url=url+'V_2_0/apply/step4submit',data={'user_id':user_id,'access_token':token,'api_request_way':'1'})
        return r3.json()['message']

    def t_jk1(self,price=10000.00,apr=10.00,limit=12):
        lo = add_md5.the_login()
        log = lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r1 = requests.post(url='http://api.yijiedai.org/V_2_0/apply/step1submit', data={'is_hospital': 1,
                                                                                        'class': 5,
                                                                                        'title': '接口测试' + timee,
                                                                                        'yongtu': 1,
                                                                                        'price': price,
                                                                                        'apr': apr,
                                                                                        'limit': limit,
                                                                                        'mode': 2,
                                                                                        'content': '测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试',
                                                                                        'access_token': token,
                                                                                        'user_id': user_id,
                                                                                        'api_request_way': '1'})
        print r1.json()['message']
    def t_jk2(self):
        lo = add_md5.the_login()
        log = lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r2 = requests.post(url='http://api.yijiedai.org/V_2_0/apply/step2submit', data={'user_id': user_id,
                                                                                        'access_token': token,
                                                                                        'api_request_way': '1',
                                                                                        'xueli': 1,
                                                                                        'hukou': 1,
                                                                                        'city': 1,
                                                                                        'address': '上受到了卡萨帝',
                                                                                        'tel': '18655469874',
                                                                                        'zip': 1,
                                                                                        'hunyin': 1,
                                                                                        'iszinv': 1,
                                                                                        'z_name': '绅士道',
                                                                                        'z_type': 1,
                                                                                        'z_mobile': 18699959878,
                                                                                        'o_name': '来咯是',
                                                                                        'o_type': 1,
                                                                                        'o_mobile': 18611122233,
                                                                                        'work_class': 1,
                                                                                        'work_city': 1,
                                                                                        'work_shouru': 8000,
                                                                                        'work_guimo': 100,
                                                                                        'work_nianxian': 1,
                                                                                        'work_tel': '18955442266',
                                                                                        'work_address': '撒大师傅萨芬大事',
                                                                                        'work_zhiwei': '大老板',
                                                                                        'h_name': '十点多睡的',
                                                                                        'h_xingzhi': 1,
                                                                                        'h_leibie': 1,
                                                                                        'h_dengji': 1,
                                                                                        'c_name': '说是道非萨芬',
                                                                                        'c_xingzhi': 1,
                                                                                        'c_hangye': 1,
                                                                                        'isfang': 1,
                                                                                        'isfangdai': 1,
                                                                                        'ische': 1,
                                                                                        'ischedai': 1
                                                                                        })
        print r2.json()['message']
    def t_jk3(self):
        lo = add_md5.the_login()
        log = lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r3 = requests.post(url='http://api.yijiedai.org/V_2_0/apply/step4submit',
                           data={'user_id': user_id, 'access_token': token, 'api_request_way': '1'})
        print r3.json()['message']
    def jk_m1(self):
        lo = add_md5.the_login()
        log = lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r1 = requests.post(url=url + 'V_2_0/apply/step1submit', data={'is_hospital': 1,
                                                                      'class': 5,
                                                                      'title': '接口测试' + timee,
                                                                      'yongtu': 1,
                                                                      'price': self.price,
                                                                      'apr': self.apr,
                                                                      'limit': self.limit,
                                                                      'mode': 2,
                                                                      'content': '测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试',
                                                                      'access_token': token,
                                                                      'user_id': user_id,
                                                                      'api_request_way': '1'})
        return r1.json()['message']
    def jk_m2(self):
        lo = add_md5.the_login()
        log = lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r2 = requests.post(url=url + 'V_2_0/apply/step2submit', data={'user_id': user_id,
                                                                      'access_token': token,
                                                                      'api_request_way': '1',
                                                                      'xueli': 1,
                                                                      'hukou': 1,
                                                                      'city': 1,
                                                                      'address': '上受到了卡萨帝',
                                                                      'tel': '18655469874',
                                                                      'zip': 1,
                                                                      'hunyin': 1,
                                                                      'iszinv': 1,
                                                                      'z_name': '绅士道',
                                                                      'z_type': 1,
                                                                      'z_mobile': 18699959878,
                                                                      'o_name': '来咯是',
                                                                      'o_type': 1,
                                                                      'o_mobile': 18611122233,
                                                                      'work_class': 1,
                                                                      'work_city': 1,
                                                                      'work_shouru': 8000,
                                                                      'work_guimo': 100,
                                                                      'work_nianxian': 1,
                                                                      'work_tel': '18955442266',
                                                                      'work_address': '撒大师傅萨芬大事',
                                                                      'work_zhiwei': '大老板',
                                                                      'h_name': '十点多睡的',
                                                                      'h_xingzhi': 1,
                                                                      'h_leibie': 1,
                                                                      'h_dengji': 1,
                                                                      'c_name': '说是道非萨芬',
                                                                      'c_xingzhi': 1,
                                                                      'c_hangye': 1,
                                                                      'isfang': 1,
                                                                      'isfangdai': 1,
                                                                      'ische': 1,
                                                                      'ischedai': 1
                                                                      })
        return r2.json()['message']
    def jk_m3(self):
        lo = add_md5.the_login()
        log = lo.web_login(15896302548)
        token = log[0]
        user_id = log[1]
        r3 = requests.post(url=url + 'V_2_0/apply/step4submit',
                           data={'user_id': user_id, 'access_token': token, 'api_request_way': '1'})
        return r3.json()['message']
class tb_buyzq():
    def __init__(self,bid,tbprice,disapr,transNum,discount):
        self.bid=bid
        self.tbprice=tbprice
        self.disapr=disapr
        self.trannum=transNum
        self.discount=discount

    def go(self):
        conn = pymysql.connect(host='yijiedai-uat.mysql.rds.aliyuncs.com', user='yijiedai',
                                    password='@YiJieDai4006021788', database='www_yijiedai_com', port=3988)
        cur = conn.cursor()
        login = add_md5.the_login()
        log = login.web_login(15889725416)
        token = log[0]
        user_id = log[1]
        data = {'borrow_id': self.bid,
                'tbprice': self.tbprice,
                'channel': '2',
                'access_token': token,
                'user_id': user_id,
                'api_request_way': '1'}
        r = requests.post(url=url + 'V_2_0/invest/tb', data=data)
        #终审
        zs=admin_sp.sp()
        zs.maxsp()
        # 债权转出
        time.sleep(20)
        sql = "SELECT creditor_id FROM yjd_creditor WHERE borrow_id=%s" % self.bid
        cur.execute(sql)
        cid = cur.fetchall()
        cid = cid[0][0]
        zz_data = {'creditorId': cid,
                   'transferNum': self.trannum,
                   'discApr': self.disapr,
                   'discount_per_partion': self.discount,
                   'access_token': token,
                   'user_id': user_id,
                   'api_request_way': '1'}
        r2 = requests.post(url=url + 'V_2_0/creditor/transferApply', data=zz_data)
        # 购买债权
        log2=add_md5.the_login()
        login2=log2.web_login(18386249157)
        token2=login2[0]
        user_id2=login2[1]
        sql1 = "SELECT id FROM yjd_creditor_transfer WHERE borrow_id=%s" % self.bid
        cur.execute(sql1)
        zzid = cur.fetchall()
        zzid = zzid[0][0]
        maizq_data = {'id': zzid, 'channel': '2', 'user_id': user_id2, 'access_token': token2, 'api_request_way': '1',
                      'noPwd': 1}
        r1 = requests.post(url=url + 'V_2_0/invest/buycreditor', data=maizq_data)
        return r1.json()['message']
if __name__ == '__main__':
    x=jie()
    x.jk1()
    x.jk2()
    x.jk3()