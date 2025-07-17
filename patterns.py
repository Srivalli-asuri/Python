# Print given patterns
# Z
# Y
# M
rows = 5
for i in range(rows):
    res = ''
    for j in range(rows):
        if i == 0 or i == rows - 1 or i + j == rows - 1:
            res += '* '
        else:
            res += '  '
    print(res)

rows = 5
mid = rows // 2
for i in range(rows):
    res = ''
    for j in range(rows):
        if i < mid:
            if i == j or i + j == rows - 1:
                res += '* '
            else:
                res += '  '
        else:
            if j == mid:
                res += '* '
            else:
                res += '  '
    print(res)

rows = 5
for i in range(rows):
    res = ''
    for j in range(rows):
        if j == 0 or j == rows - 1 or (i == j and i <= rows // 2) or (i + j == rows - 1 and i <= rows // 2):
            res += '* '
        else:
            res += '  '
    print(res)


