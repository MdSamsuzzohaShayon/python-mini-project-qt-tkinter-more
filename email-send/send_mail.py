# WE NEED TO LOGIN TO GMAIL
from keys import login_info
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   # FOR BOTH BULNK TEXT EMAIL AND AN HTMLEMAIL


# LOGIN INFO IS A DICTINORY CONTAINING EMAIL AND PASSWORD
# username = login_info['gmail']
# password = login_info['password']
username = login_info['gmail']
password = login_info["password"]




def send_mail(text="Email body", subject="Hello world", from_email=login_info['gmail'] , to_emails=None):
    # https://docs.pytest.org/en/stable/assert.html
    # https://docs.python.org/3/library/functions.html#isinstance
    assert isinstance(to_emails, list)  # IT WILL GIVE AN ERROR IF THIS IS NOT A LIST


    msg= MIMEMultipart("alternative")
    msg["From"] = from_email
    msg['To'] = ", ".join(to_emails)   # comma seperated list
    msg['Subject'] = subject

    txt_part = MIMEText(text, "plain")
    msg.attach(txt_part)

    html_part = MIMEText("<h1 style='color: green; padding: 10px; background:purple'> This is working </h1>", "html")
    msg.attach(html_part)



    msg_str = msg.as_string()



    # https://docs.python.org/3/library/smtplib.html
    # LOGIN TO SMTP SERVER
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    print(username, password)
    server.ehlo() # RUN THIS BY DEFAULT
    server.starttls() # SECURE THE CONNECTION
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()




send_mail(to_emails=['mdshayon0@gmail.com'])
