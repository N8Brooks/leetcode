from bisect import insort
from typing import List


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    def find(email):
        return email if email == parent.get(email, email) else find(parent[email])

    parent = {}
    lookup = {}
    for name, *emails in accounts:
        zero = find(emails[0])
        for email in emails:
            parent[find(email)] = zero
            lookup[email] = name

    groups = {}
    for email in parent:
        name = lookup[email]
        zero = find(email)
        emails = groups.setdefault(zero, [name])
        insort(emails, email, 1)

    return list(groups.values())
