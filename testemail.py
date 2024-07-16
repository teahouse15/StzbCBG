import requests
import re
import urllib3

#忽略证书警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class MAIL163:
    def __init__(self, username, password):
        self.session = requests.Session()

        self.username = username
        self.password = password
        self.sid = None

    def login(self):
        loginUrl = "https://mail.163.com/entry/cgi/ntesdoor?style=-1&df=mail163_letter&net=&language=-1&from=web&race=&iframe=1&product=mail163&funcid=loginone&passtype=1&allssl=true&url2=https://mail.163.com/errorpage/error163.htm"
        headers = {
            'Referer': "https://mail.163.com/",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"
        }

        postData = {
            'savelogin': "0",
            'url2': "http://mail.163.com/errorpage/error163.htm",
            'username': self.username,
            'password': self.password
        }

        response = self.session.post(loginUrl, headers=headers, data=postData, verify=False)
        print(response.text)
        #提取sid，获取邮件信息需要使用它
        pattern = re.compile(r'sid=(.*?)&', re.S)
        self.sid = re.search(pattern, response.text).group(1)

    def __repr__(self):
        return '<MAIL163 sid: {}>'.format(self.sid)

if __name__ == '__main__':
    mail = MAIL163("bogendihong@163.com", "zq05111402")
    mail.login()
    print(mail)