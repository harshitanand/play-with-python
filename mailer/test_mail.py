
import mailer

sender = str(raw_input("Enter your email address: "))
reciever = str(raw_input ("Enter recivers adress: "))
password = str(raw_input("Enter your password: "))
message = """From: Thinqbot Technologies
             To: XXXXXX@gmail.com
             Subject: Hello

             Hello World.
          """

mailer.mailer(sender, password, reciever, message)
