# # your code goes here!
# import re

# class EmailAddressParser():
#     def __init__(self, addresses):
#         self.addresses = addresses

#     def parse(self):
#         # Split the string by comma or space to separate the email addresses
#         email_list = re.split(r"\s|,", self.addresses)
#         # Remove any empty strings
#         email_list = [email.strip() for email in email_list if email.strip()]
#         # Remove duplicates and sort the email addresses
#         unique_emails = sorted(set(email_list))
#         return unique_emails

import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        email_list = re.findall(r'[\w\.-]+@[\w\.-]+', self.addresses)
        unique_emails = sorted(set(email_list))
        return unique_emails
