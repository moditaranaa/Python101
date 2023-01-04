#Send EMAIL using Python
import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587) #587 is the gmail port number.
ob.ehlo()
ob.starttls()
ob.login('sender@gmail.com', 'sender_password')
subject="test "
body = "Python"
message = "subject : {}/n/n{}". format(subject,body)
listadd= ['receiversaddress@xyz.com', 'receiversaddress2@xyz.com']
ob.sendmail('sender@gmail.com', listadd, message)
print("send mail")
ob.quit()
