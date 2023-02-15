##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list running forward and back.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    for i in range(len(lst)-1, -1, -1):     # iterate through list backwards
        lst.append(lst[i])

    return lst

# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    for i in range(len(seq)):
        seq[i] = fn(fn(seq[i]))     # replace value in seq w new value

    return seq
    

#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    x = []          # temp list

    for i in range(len(seq)):
        if pred(seq[i]) == True:    # find values to remove
            x.append(seq[i])            # save values to temp list

    for i in range(len(x)):         # remove values from seq
        seq.remove(x[i])

    return seq

#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    return [(x) for x in list(range(n)) if pred(x) == True]

#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    x = []          # temp list

    for i in range(len(lst)):
        if type(lst[i]) == list:        # if item is type list
            n = flatten(lst[i])             # call function again - get flattened list
            for j in range(len(n)):         # add flattened list to temp
                x.append(n[j])
        else:                           # if item not list, add to temp list x
            x.append(lst[i])

    return x


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
