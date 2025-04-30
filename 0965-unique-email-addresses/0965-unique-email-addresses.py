class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmail = []
        count = 0

        for email in emails:
            parts = email.split("@")
            if len(parts) != 2:
                continue
            localName = parts[0]

            # Remove . character
            localName = localName.replace(".", "")

            # Skip data after + in localName
            localName = localName.split("+")[0]

            # Domain name
            domainName = parts[1]

            # Email
            email = localName + "@" + domainName

            if email not in uniqueEmail:
                count += 1
                uniqueEmail.append(email)

        return count



        