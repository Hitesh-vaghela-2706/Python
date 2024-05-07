from flask_mail import Mail
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "hiteshmeac@gmail.com",
    MAIL_PASSWORD = "meaccount"
)
mail = Mail(app)

mail.send_message(
    'new message from'+name,
    sender = email,
    recipent = [parameter["mail_username"]],
    body = message + "\n" +phone
        )