words = {input() for _ in range(int(input()))}
words = sorted(list(words))
words.sort(key=len)

for word in words:print(word)
