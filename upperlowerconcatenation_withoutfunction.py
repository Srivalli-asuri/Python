def st(a):
    u=''
    l=''
    for ch in a:
        if 65<=ord(ch)<=91:
            u+=ch

        else:
            l+=ch
    return u+l
print(st('adhFGHTbsgxf'))
