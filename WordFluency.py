"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    strlist = list(set(s.split(" ")))
    pairlist = []
    for each in strlist:
        pair = (each, s.split(" ").count(each))
        pairlist.append(pair)
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    pairlist.sort(compare)
    #lambda x,y:cmp(y[1],x[1])
    
    top_n = pairlist[:n]
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n

def compare(x, y):
    if x[1] == y[1]:
        return cmp(x[0],y[0])
    else:
        return cmp(y[1], x[1])
        

def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
