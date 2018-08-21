import requests
import hashlib
class add_md5():
    def am5(self,src):
        m=hashlib.md5()
        m.update(src)
        src=m.hexdigest()
        return src
class the_login():
    def __init__(self):
        self.url='http://api.yjdtest.cn/'
    def login(self,username,url='http://api.yijiedai.org/V_2_0/login',password='a123456789',api_request_way='2',device_no='454312',mobile_type='android'):
        psd_lock=add_md5()
        psw=psd_lock.am5(password)
        r=requests.post(url=url,data={'username':username,'password':psw,'api_request_way':api_request_way,'device_no':device_no,'mobile_type':mobile_type})
        return [r.json()['data']['access_token'],r.json()['data']['user_id']]
    def ci_login(self,username,password='a123456789',api_request_way='2',device_no='454312',mobile_type='android'):
        psd_lock=add_md5()
        psw=psd_lock.am5(password)
        r1=requests.post(url='http://test1117-api.yijiedai.org/V_2_0/login',data={'username':username,'password':psw,'api_request_way':api_request_way,'device_no':device_no,'mobile_type':mobile_type})
        return [r1.json()['data']['access_token'],r1.json()['data']['user_id']]
    def web_login(self,username,api_request_way='1',password='a123456'):
        get_w=add_md5()
        passw=get_w.am5(password)
        r=requests.post(url=self.url+'V_2_0/login/handle',data={'username':username,'password':passw,'api_request_way':api_request_way,'channel':'1'})
        return [r.json()['data']['access_token'],r.json()['data']['user_id'],r.json()['data']['username']]




