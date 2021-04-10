def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    k=aDict.keys()
    n=0
    for w in k:
        if n== 0:
            n=len(aDict[w])
            key=w
        elif len(aDict[w])>n:
                key=w
                n=len(aDict[w])
    return key
    
print(biggest({'b': [], 'a': [1, 7, 5, 4, 3, 18, 10, 0]}))