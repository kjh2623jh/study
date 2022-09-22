result = """Moved from 1 to 6 (dice = 5, lucci = 2)
Moved from 6 to 10 (dice = 4, lucci = 2)
Moved from 10 to 19 (dice = 5, lucci = 2)
Moved from 19 to 25 (dice = 6, lucci = 2)
Moved from 25 to 31 (dice = 6, lucci = 1)
Moved from 31 to 41 (dice = 5, lucci = 3)
Moved from 41 to 44 (dice = 4, lucci = 1)
Moved from 44 to 52 (dice = 6, lucci = 3)
Moved from 52 to 53 (dice = 1, lucci = 3)
Moved from 53 to 54 (dice = 1, lucci = 3)
Moved from 54 to 55 (dice = 1, lucci = 5)
Moved from 55 to 64 (dice = 6, lucci = 5)
"""

for _ in range(16):
    result+="""Moved from 64 to 6 (dice = 6, lucci = 2)
Moved from 6 to 10 (dice = 4, lucci = 2)
Moved from 10 to 19 (dice = 5, lucci = 2)
Moved from 19 to 25 (dice = 6, lucci = 2)
Moved from 25 to 31 (dice = 6, lucci = 1)
Moved from 31 to 41 (dice = 5, lucci = 3)
Moved from 41 to 44 (dice = 4, lucci = 1)
Moved from 44 to 52 (dice = 6, lucci = 3)
Moved from 52 to 53 (dice = 1, lucci = 3)
Moved from 53 to 54 (dice = 1, lucci = 3)
Moved from 54 to 55 (dice = 1, lucci = 5)
Moved from 55 to 64 (dice = 6, lucci = 5)
"""

result+="""
"""

print(result)