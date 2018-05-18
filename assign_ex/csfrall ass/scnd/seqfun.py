def listOfWords(a):
    b = a.split()
    return b


#output:

>>> listOfWords('Bond. James Bond')
['Bond.', 'James', 'Bond']
>>> listOfWords('')
[]
>>> listOfWords('    ')
[]
>>> listOfWords('  Avada   Ked...   ')
['Avada', 'Ked...']
>>> 

