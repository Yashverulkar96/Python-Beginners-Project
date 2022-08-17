email = input("Enter the email address").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print("username:{},'\n' domainName:{}".format(username,domain))