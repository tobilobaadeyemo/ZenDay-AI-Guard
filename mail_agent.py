# mail_agent.py
def check_mail(mailbox):
    for email in mailbox:
        if email["is_spam"]:
            block_email(email)
        else:
            draft_reply(email)
