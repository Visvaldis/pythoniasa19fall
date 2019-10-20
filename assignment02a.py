"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    st = []
    st.append('That kept the cock that crowed in the morn,' )
    st.append('That waked the priest all shaven and shorn,')
    st.append('That married the man all tattered and torn,' )
    st.append('That kissed the maiden all forlorn,')
    st.append('That milked the cow with the crumpled horn,')
    st.append('That tossed the dog,')
    st.append('That worried the cat,')
    st.append('That killed the rat,')
    st.append('That ate the malt')
    st.append('That lay in the house that Jack built.')

    stAlt = []
    stAlt.append('This is the farmer sowing his corn,')
    stAlt.append('This is the cock that crowed in the morn,')
    stAlt.append('This is the priest all shaven and shorn,')
    stAlt.append('This is the man all tattered and torn,')
    stAlt.append('This is the maiden all forlorn,')
    stAlt.append('This is the cow with the crumpled horn,')
    stAlt.append('This is the dog,')
    stAlt.append('This is the cat,')
    stAlt.append('This is the rat,')
    stAlt.append('This is the malt')
    stAlt.append( 'This is the house that Jack built.')

    n = 10
    i = 1
    s = ''
    for i in range(n+1):
        s+= stAlt[n-i] + '\n'
        for j in range(i):
            s+= st[n-i + j]+'\n'    
        s+= '\n'
    #print(s)
    return s[:-1]



if __name__ == '__main__':
    import doctest
    doctest.testmod()
