import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    return bool(re.match(pattern, email))

def fun(N, emails):
    valid_emails = [email for email in emails if is_valid_email(email)]
    valid_emails.sort()
    return valid_emails

if __name__ == "__main__":
    N = int(input())
    emails = [input() for _ in range(N)]
    valid_emails = fun(N, emails)
for email in valid_emails:
    print(email)
