import schedule
import time
import datetime
import smtplib, ssl

def mail():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "infinityokayy@gmail.com"
    receiver_email = "adityamsahane07@gmail.com"
    password = "xrit vgiv lyth ocvk"
    message ="""Hello mail  sent through python automation"""
    context = ssl.create_default_context()
    print(datetime.datetime.now)
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def main():
    schedule.every(10).seconds.do(mail)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()

