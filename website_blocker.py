import time
from datetime import datetime as dt

hosts_path="/etc/hosts"
ip="127.0.0.1"
website_list=["facebook.com", "espn.com", "sports.yahoo.com", "wired.com", "reddit.com", "fanduel.com"]
www_list = ["www."+i for i in website_list]
www_list.extend(website_list)

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,6) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Get to work!!")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in www_list:
                if website in content:
                    pass
                else:
                    file.write(ip+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in www_list):
                    file.write(line)
            file.truncate()
        print("Feed the sports addiction!!")
    time.sleep(3600)
