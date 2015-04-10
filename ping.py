import os
import smtplib
import time

hostname = "st-patricksschool.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("username", "password")

msg = "\nServer down da goyyale!"

response = os.system("ping -c 1 " + hostname)
while True:
  if response == 0:
    print "Up!"
  else:
    print "Down!"
    server.sendmail("XXXXXX@gmail.com", "XXXXXX@gmail.com", msg)
  time.sleep(24*60*60)
