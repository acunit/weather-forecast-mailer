import smtplib
import config

def send_emails(emails, schedule, forecast):
    # connect to the gmail SMTP server or whatever email you want to send from and add port for encryption
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login and ask for password of the email
    password = getpass.getpass("What's your password?")
    from_email = my_email_address
    server.login(from_email, password)

    # Send to email list
    for to_email, name in emails.items():
        message = 'Subject: Ready For Some Fun!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += 'We have an exciting day planned. Please see below:\n\n'
        message += schedule + '\n\n'
        message += "Can't wait!"

        server.sendmail(from_email, to_email, message)

    server.quit()