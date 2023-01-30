from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.errors import FloodWaitError
from constants import api_hash_bt,phone_bt,api_id_bt,bt_username,manager_bt,plain_text
import sys
import time
import pandas as pd
from datetime import datetime,timezone
current = datetime.now(timezone.utc)
api_id = api_id_bt 
api_hash = api_hash_bt
phone = phone_bt
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

time.sleep(10)

usernames= pd.read_csv("username.csv")
all_usernames=pd.read_csv("all_usernames.csv")
for i, row in usernames.iterrows():
	print("new user",i,row['username'])
	if row['username']==manager_bt[1:]:
		print(" this is admin")
	else:
		x=usernames.iloc[i+1:]
		x.to_csv('username.csv')
		j1=pd.read_csv('username.csv')
		print("send message ",row['username'],datetime.now(timezone.utc))
		client.send_message(row['username'],plain_text)
		time.sleep(5)	
		while True:
			c=datetime.now(timezone.utc)
			x=c - current
			secs=x.total_seconds()
			if secs>25200:
				current=datetime.now(timezone.utc)
				break
			else:
				for j, roww in all_usernames.iterrows():
					try:
						for message in client.iter_messages(roww['username']):
							if not message.out:
								if roww['username'] == manager_bt[1:]:
									msg=message.message.split()
									print(msg[0][1:]," ".join(msg[1:]))
									client.send_message(msg[0][1:]," ".join(msg[1:]))
									time.sleep(5)
									client.send_message(manager_bt[1:],"sent successfully")
									time.sleep(5)
									break
								
								print("some one replied")
								client.send_message(roww['username'], ".")
								time.sleep(5)
								client.send_message(manager_bt[1:],'@' + roww['username'] +" " + bt_username + " " + message.message)
								time.sleep(5)
								break
							break
						

					except:
						pass
while True:
	for j, roww in all_usernames.iterrows():
					try:
						for message in client.iter_messages(roww['username']):
							if not message.out:
								if roww['username'] == manager_bt[1:]:
									msg=message.message.split()
									client.send_message(msg[0][1:]," ".join(msg[1:]))
									time.sleep(5)
									client.send_message(manager_bt[1:],"sent successfully")
									break
								client.send_message(roww['username'], ".")
								time.sleep(5)
								client.send_message(manager_bt[1:],'@' + roww['username'] +" " + bt_username + " " + message.message)
								time.sleep(5)
								break
							break
						

					except:
						pass



client.send_message('tryyyyde',"my task is finished please change my code to receive messages")
time.sleep(10)
#client.send_message('trafficooo',"my task is finished please change my code to receive messages")

client.run_until_disconnected()
