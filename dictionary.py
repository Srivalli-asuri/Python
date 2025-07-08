# Find it is anagram or not using dictionary
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    d = {}
    for ch in s1:
        d[ch] = d.get(ch, 0) + 1

    for ch in s2:
        if ch in d:
            d[ch] -= 1
        else:
            return False

    for value in d.values():
        if value != 0:
            return False
    return True
# Example
print("Anagram" if is_anagram("listen", "silent") else "Not anagram")
# Find the highest frequency character in the string
st='abcccdee'
res={}
for ch in st:
    if ch in res:
        res[ch]+=1
    else:
        res[ch]=1
print(res)

# Find character with highest frequency
max_char = ''
max_count = 0
for ch in res:
    if res[ch] > max_count:
        max_count = res[ch]
        max_char = ch

print("Highest frequency character:", max_char)
print("Frequency:", max_count)



