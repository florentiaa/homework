x = ['mix', 'xyz', 'apple', 'xanadu', 'rovio']
newlist = []
def sort(s):
    for elem in s[:]:
        if elem.startswith('x'):
            newlist.append(elem)
            s.remove(elem)
    print(sorted(newlist)+sorted(s))
    del newlist[:]

sort(x)
