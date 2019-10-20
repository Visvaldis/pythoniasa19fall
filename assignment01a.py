"""
Assignment 1-A
==============
<<<<<<< HEAD
Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.
"""


st = []
st.append('That kept the cock that crow\'d in the morn,' )
st.append('That waked the priest all shaven and shorn,')
st.append('That married the man all tatter\'d and torn,' )
st.append('That kissed the maiden all forlorn, ')
st.append('That milk\'d the cow with the crumpled horn,')
st.append('That tossed the dog, ')
st.append('That worried the cat, ')
st.append('That killed the rat, ')
st.append('That ate the malt ')
st.append('That lay in the house that Jack built.')

stAlt = []
stAlt.append('This is the farmer sowing his corn,')
stAlt.append('This is the cock that crow\'d in the morn,')
stAlt.append('This is the priest all shaven and shorn,')
stAlt.append('This is the man all tatter\'d and torn,')
stAlt.append('This is the maiden all forlorn,')
stAlt.append('This is the cow with the crumpled horn,')
stAlt.append('This is the dog,')
stAlt.append('This is the cat,')
stAlt.append('This is the rat,')
stAlt.append('This is the malt '  )
stAlt.append( 'This is the house that Jack built.')

n = 10
i = 1

for i in range(n):
    print(stAlt[n-i])
    for j in range(i):
        print(st[n-i + j])    
    print('\n')



poem = '''

"""

def poem():
    return ''


if __name__ == '__main__':
    import doctest
    doctest.testmod()