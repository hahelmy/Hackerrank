def repeatedString(s, n):

    print(f"The string to repeat: {s}")
    if len(s) != 0:
        s = s * int(n/len(s)) + s

    print(f"Repeated: {s}")
    print(f"Length: {len(s)}")
    print(f"N: {n}")
    print (f"Occurances: {s[0:n].count('a')}") 

    
    
s = 'agdfjrtgjfgjfdjdfjdfjkkghkykykt'
n = 80

repeatedString(s, n)