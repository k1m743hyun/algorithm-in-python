from collections import Counter

word = input().upper()
if len(word) > 1:
    result = Counter(word).most_common(2)
    print(result[0][0] if result[0][1] != result[1][1] else '?')
else:
    print(word)
