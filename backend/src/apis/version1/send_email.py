from fastapi import BackgroundTasks
from starlette.responses import JSONResponse

class Envs:
    MAIL_USERNAME="waitbuddy64"
    MAIL_PASSWORD="waitbuddy1234"
    MAIL_FROM="waitbuddy64@gmail.com"
    MAIL_PORT=587
    MAIL_SERVER="smtp.gmail.com"
    MAIL_FROM_NAME="Waitbuddy"
    MAIL_TLS=True,
    MAIL_SSL=False
    

def send_email(subject: str, email_to: str, body: dict):
    import smtplib

    FROM = "waitbuddy64@gmail.com"
    TO = email_to if isinstance(email_to, list) else [email_to]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(Envs.MAIL_USERNAME, Envs.MAIL_PASSWORD)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except :
        print("failed to send mail")
    return JSONResponse(status_code=200, content={"message": "email has been sent"}) 
