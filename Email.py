class Email():
    
    def __init__(self,username,password):
        import smtplib
        self.username=username
        self.smtp=smtplib.SMTP()
        self.smtp.connect(self._getsmtp()[0],self._getsmtp()[1])
        self.smtp.login(username,password)
        
    def _getsmtp(self):
        if 'gmail.com' in self.username:
            return 'smtp.'+self.username[self.username.index('@')+1:],'587'
        else:
            return 'smtp.'+self.username[self.username.index('@')+1:],'25'
        
    def send(self,recipient,subject,content):
        import email.mime.multipart
        import email.mime.text
        msg=email.mime.multipart.MIMEMultipart()
        msg['from']=self.username
        msg['to']=recipient
        msg['subject']=subject
        txt=email.mime.text.MIMEText(content)
        msg.attach(txt)
        self.smtp.sendmail(msg['from'],msg['to'],str(msg))
        self.smtp.quit()

if __name__=='__main__':
    content='test'
    a=Email('abc@163.com','xxxxxx')
    a.send('abc@163.com','test',content)