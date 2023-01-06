# Modifying db

flask db migrate
flask db upgrade

# Starting app

set FLASK_DEBUG=1
flask run

# Run fake mail server

 <!-- pip install nullsmtpd -->

nullsmtpd --no-fork --mail-dir .\mails\
