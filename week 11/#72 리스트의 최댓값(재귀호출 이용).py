def find_max(t,l,r):
    if l == r:
        return  t[r]
    if t[l] > t[r]:
        return find_max(t,l,r-1)
    elif t[l] < t[r]:
        return find_max(t,l+1,r)
    elif t[l] == t[r]:
        return  find_max(t,l+1,r)
