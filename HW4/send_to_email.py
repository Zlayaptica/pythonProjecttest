import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

import yaml

with open("locators.yaml") as f:
    addr = yaml.safe_load(f)

fromaddr = addr["fromaddr"]
toaddr = addr["toaddr"]
mypass = addr["mypass"]
reportname = "log.txt"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Hello"

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part["Content-Disposition"] = 'attachment; filename="%s"' % basename(reportname)
    msg.attach(part)

body = "Test"
msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
server.login(msg['From'], mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
