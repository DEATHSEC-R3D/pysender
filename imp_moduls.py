import imp_funcs
def send_mail_py(filename=''):
    fromaddr = input("Tqveni E-Mail: ")
    password = imp_funcs.getpass("Tqveni E-Mail-s paroli: ")
    toaddr = input("Mimgebis E-Mail: ")
    toaddr = toaddr.split(',')
    msg = imp_funcs.MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = ", ".join(toaddr) 
    msg['Subject'] = input("Subject: ")
    body = input("Body: ")
    msg.attach(imp_funcs.MIMEText(body, 'plain')) 
    if filename:
        attachment = open(filename, "rb") 
        p = imp_funcs.MIMEBase('application', 'octet-stream') 
        p.set_payload((attachment).read()) 
        imp_funcs.encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p) 
    smtp_server = input("Mailis servisi (gmail.com,mail.ru): ")
    smtp_server = "smtp."+smtp_server
    s = imp_funcs.smtplib.SMTP(smtp_server, 587) 
    s.starttls() 
    s.login(fromaddr, password) 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
    imp_funcs.os.system("cls")