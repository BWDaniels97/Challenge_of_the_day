'''
Python Write a function that accepts a sequence of whitespace separated 
words as a string input, sorts each item alphanumerically and removes any 
duplicate items, then returns the result as a string. Write a test for this function.

Suppose the following input is supplied to the program: 
hello world and practice makes perfect and hello world againThen, 
the output should be: again and hello makes perfect practice world

'''

def alpha(input):

    words = input.split(' ')
    uni_words = set(words)
    new = list(uni_words)
    new.sort()
    
    final = ' '.join(new)


    return final
  



