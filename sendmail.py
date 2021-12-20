from netcat import Netcat

nc=Netcat()
#Ask for sender email.
sen_email = input("Enter the sender email ")

#Ask for receiver email
rec_email = input("Enter the receiver email ")

#Ask for Subject line
sub = input("Enter the subject line ")

#File name containing mail body. Should be absolute path
file_name = input("Enter the file name which contains the mail contents")

#Connect to IU smtp server
nc.connect("mail-relay.iu.edu", 25)
nc.write("HELO NIKET\r\n")
raw_data = nc.read(1024)
print(raw_data)
nc.write("MAIL FROM: {}\r\n".format(sen_email))
raw_data = nc.read(1024)
print(raw_data)
nc.write("RCPT TO: {}\r\n".format(rec_email))
raw_data = nc.read(1024)
print(raw_data)
nc.write("DATA\r\n")
raw_data = nc.read(1024)
print(raw_data)
nc.write("Subject: {}\r\n".format(sub))
body = ""
with open(file_name,"r") as f:
body = f.read()
nc.write(body+".\r\n")
nc.close()