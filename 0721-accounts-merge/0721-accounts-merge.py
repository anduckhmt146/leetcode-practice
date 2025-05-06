from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            parent[find(x)] = find(y)
        
        email_to_name = {}

        # Union all emails under the same person
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                union(first_email, email)

        # Merge emails by their root parent
        merged = defaultdict(list)
        for email in parent:
            root = find(email)
            merged[root].append(email)

        # Build final result
        result = []
        for root, emails in merged.items():
            # Because all email have the same root
            name = email_to_name[root]
            result.append([name] + sorted(emails))

        return result
