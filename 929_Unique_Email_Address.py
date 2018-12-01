
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]


def unique_email_address(emails):
    output = []
    for email in emails:
       # x = email.split("@")
       # email = email.replace(".", '')
        email = email.split("@")
        x0 = (email[0].replace(".", '')).split("+")[0]
        x1 = email[1]
        x = x0 + '@' + x1
        if x not in output:
            output.append(x)
    return len(output)


unique_email_address(emails)
