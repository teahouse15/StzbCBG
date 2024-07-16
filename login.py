import requests

url = "https://stzb.cbg.163.com/cgi/api/login"

payload = {
   'username': 'bogendihong@163.com'
}

headers = {
   'Cookie': 'NTES_SESS=XnUHY_SjUOiv8itsKEXvRWYg.Ox5GaqHLuDt87AYpcsfKp8LKuA4P3aAAAshUZzZakB2REGZwd26en4QwbUPDQI5tWtoswugK4.zCVgIu87pZaWEGpnn6SyOWVnfBpsM4u0i_UL21kRnLoWfe52eBIweurGRlJZU7HSKvfLZsF1HnFWnMbJhuUsJstoeSMCbe9onmzIdvq0V3; _flow_group_v2=g1; is_log_active_stat=1; _external_mark=direct; fingerprint=5xbg3kxq2wf6dqhz; sid=v2.s.WSPMD3p9kJ3rPLokCS4saMVESyUpS9su81EBaCwnKTchCrlp; urs_share_login_token=Ym9nZW5kaWhvbmdAMTYzLmNvbSQ0N2JjZGUyNTNmZTZhMGQ5OTU5ODlkMzEwMDJlNTE1OQ==; urs_share_login_token_h5=Ym9nZW5kaWhvbmdAMTYzLmNvbSQ0N2JjZGUyNTNmZTZhMGQ5OTU5ODlkMzEwMDJlNTE1OQ==; login_id=ae38c56b-432b-11ef-a60b-aed2bf0eb665',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': 'stzb.cbg.163.com',
   'Connection': 'keep-alive',
   'Content-Type': 'multipart/form-data; boundary=--------------------------620297492023791600046471'
}

response = requests.post(url, headers=headers, data=payload)

# 获取所有cookies
cookies = response.cookies

# 打印所有cookies
for cookie in cookies:
   print(cookie.name, cookie.value)

print(response.text)