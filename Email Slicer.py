mail = input("Enter your mail id: ")
username = mail[: mail.index('@')]
domain = mail[mail.index('@')+1:]
print(f"Your username is '{username.upper()}' and your domain is '{domain.upper()}' " )