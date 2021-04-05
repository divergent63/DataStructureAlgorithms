

word1 = 'apple'
word2 = 'pleap'

cnt1 = [0]*26
cnt2 = [0]*26

same = None

for i in range(len(word1)):
    pos = ord(word1[i]) - ord('a')
    cnt1[pos] += 1

for i in range(len(word2)):
    pos = ord(word2[i]) - ord('a')
    cnt2[pos] += 1

for i in range(len(cnt1)):
    if cnt1[i] != cnt2[i]:
        same = 0
    else:
        same = 1

print(same)
