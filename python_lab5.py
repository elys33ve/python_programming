## Lab 5: Required Questions - Dictionaries  ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    merged = {}

    keys = list(dict1) + list(dict2)                        # get list of combined dict keys
    vals = list(dict1.values()) + list(dict2.values())      # get lsit of combined dict values
    
    for i in range(len(dict1) + len(dict2)):        # add keys w respective values to new dict
        merged[keys[i]] = vals[i]

    return merged


# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    dictionary = {}
    keys = message.split()

    for i in range(len(keys)):      # create dict with values of zero
        dictionary[keys[i]] = 0

    for i in range(len(keys)):      # add one for each instance of word in keys list
        dictionary[keys[i]] = dictionary[keys[i]] + 1
    
    return dictionary


# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> d2= replace_all(d, 3, 'poof')
    >>> d2 == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    keys = list(d)

    for i in range(len(keys)):
        if d[keys[i]] == x:         # if value is x
            d[keys[i]] = y              # replace value with y
    
    return d

# RQ4
def sumdicts(lst):
	""" 
	Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
	if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
	as the value mapped for that key
	>>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
	>>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
	True
	"""
	dictionary = {}

	for i in range(len(lst)):                   # create new dict with all values set to zero
		for j in range(len(list(lst[i]))):
			dictionary[list(lst[i])[j]] = 0

	for i in range(len(lst)):                   # get some of values for each identical key
		keys = list(lst[i])
		for j in range(len(keys)):
			dictionary[keys[j]] = dictionary[keys[j]] + lst[i][keys[j]]

	return dictionary

#RQ5
def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of median length starting with word, 
    and choosing successors from table. It is difficult to write a doctest for this function, 
    since it is randomized. But my experiments showed that with 5 random samples you should usually
    get a tweet that is roughly ordinary size sentence (6-10 words).
    """
    from rand_tweet_functions import random_tweet       # py doc with random_tweet() and construct_tweet() functions from Lab05 worksheet

    rand_twt = []
    lengths = []

    for i in range(5):
        rand_twt.append(random_tweet(table))    # get list of 5 random tweets
        lengths.append(len(rand_twt[i]))        # get list of their lengths

    lengths.sort()      # sort lengths from shortest to longest

    return rand_twt[2]


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)