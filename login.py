import requests

url = "https://stzb.cbg.163.com/cgi/api/login"

payload = {
   'username': 'bogendihong@163.com',
   'exter': 'direct',
   'page_session_id': '0190B6C3-0611-CB19-F28D-60080E85162B'
}

headers = {
   'Cookie': 'reco_sid=yzKiti7YOJ16tlBeBLsFKPjzMyJ4Bpj6B6K9CvW9;transmit_info=%7B%22time%22%3A1721053006734%2C%22bs%22%3A%7B%22ticket_id%22%3A%2200_30326_1721053006734%22%2C%22bd_id%22%3A%7B%7D%7D%7D;trace_session_id=0190B5BB-2D44-9DBB-10BB-2F989609292A	;timing_user_id	=time_Sho1HqLlhP;is_log_active_stat=1;fingerprint=syzcfRI0X7vtlEhNI23OhV85;_flow_group_v2=g18;_external_mark=direct;NTES_SESS=XnUHY_SjUOiv8itsKEXvRWYg.Ox5GaqHLuDt87AYpcsfKp8LKuA4P3aAAAshUZzZakB2REGZwd26en4QwbUPDQI5tWtoswugK4.zCVgIu87pZaWEGpnn6SyOWVnfBpsM4u0i_UL21kRnLoWfe52eBIweurGRlJZU7HSKvfLZsF1HnFWnMbJhuUsJstoeSMCbe9onmzIdvq0V3; _flow_group_v2=g31; _external_mark=direct; fingerprint=4id1bzwxowhyux3p; reco_sid=bvd-BQXJMYZ2QPK1X3RczlNBQCt8t6GO-hHmuV42; is_log_active_stat=1',
}

response = requests.post(url, headers=headers, data=payload)
# 获取所有cookies
cookies = response.cookies

# 打印所有cookies
for cookie in cookies:
   print(cookie.name, cookie.value)

print(response.text)