
import os 

email_user = os.environ.get('EMAIL_USER')
email_password = os.environ.get('EMAIL_PASS')
SECRET_KEY = os.environ.get('SECRET_KEY')
print(email_user)
print(email_password)