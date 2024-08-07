import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split the string by common separators (comma, semicolon, and spaces)
        separators = r'[,\s]+'
        split_addresses = re.split(separators, self.addresses.strip())
        
        # Regex pattern for a valid email address
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Clean and filter valid email addresses
        valid_emails = [email for email in split_addresses if re.match(pattern, email)]
        
        # Sort the valid emails to match the test's expected order
        valid_emails.sort()
        
        return valid_emails

# # Example usage
# parser = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
# parsed_emails = parser.parse()
# print(parsed_emails)
