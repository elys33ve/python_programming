## Required Questions: Linked Lists ##
## Use the Linked List ADT defined below

#RQ1
def has_prefix(s, prefix):
	"""Returns whether prefix appears at the beginning of linked list s.

	>>> x = link(3, link(4, link(6, link(6))))
	>>> print_link(x)
	3 4 6 6
	>>> has_prefix(x, empty)
	True
	>>> has_prefix(x, link(3))
	True
	>>> has_prefix(x, link(4))
	False
	>>> has_prefix(x, link(3, link(4)))
	True
	>>> has_prefix(x, link(3, link(3)))
	False
	>>> has_prefix(x, x)
	True
	>>> has_prefix(link(2), link(2, link(3)))
	False
	"""
	if is_link(prefix) == True or is_link(s) == True:		# when prefix and s are both links
		while s != empty and prefix != empty:
			if first(s) != first(prefix):
				return False
			s = rest(s)
			prefix = rest(prefix)
		
		if s == empty and prefix != empty:
			return False
		else:
			return True
	else:
		if is_link(s):
			if first(s) == prefix:		# if s is still link
				return True
		else:
			if s == prefix:				# if prefix is still link or neither are links
				return True
		return False

#RQ2
def has_sublist(s, sublist):
	"""Returns whether sublist appears somewhere within linked list s.

	>>> has_sublist(empty, empty)
	True
	>>> aca = link('A', link('C', link('A')))
	>>> x = link('G', link('A', link('T', link('T', aca))))
	>>> print_link(x)
	G A T T A C A
	>>> has_sublist(x, empty)
	True
	>>> has_sublist(x, link(2, link(3)))
	False
	>>> has_sublist(x, link('G', link('T')))
	False
	>>> has_sublist(x, link('A', link('T', link('T'))))
	True
	>>> has_sublist(link(1, link(2, link(3))), link(2))
	True
	>>> has_sublist(x, link('A', x))
	False
	"""
	if s == sublist:		# if both are same
		return True
	if sublist == empty:	# if sublist empty
		return True

	while s != empty:
		temp = sublist
		if temp != empty:
			while first(s) == first(temp):		# while firsts are same, 
				s = rest(s)
				temp = rest(temp)
				if temp == empty:						# if temp runs out, then sublist exists in s
					return True
				elif s == empty:
					break
		if s != empty:					# check if s empty from previous loop
			s = rest(s)

	return False	


#RQ3
def has_kitty_gene(dna):
	"""Returns whether the linked list dna contains the CATCAT gene as a sublist.

	>>> dna = link('C', link('A', link('T')))
	>>> dna = link('C', link('A', link('T', link('G', dna))))
	>>> print_link(dna)
	C A T G C A T
	>>> has_kitty_gene(dna)
	False
	>>> end = link('T', link('C', link('A', link('T', link('G')))))
	>>> dna = link('G', link('T', link('A', link('C', link('A', end)))))
	>>> print_link(dna)
	G T A C A T C A T G
	>>> has_kitty_gene(dna)
	True
	>>> has_kitty_gene(end)
	False
	"""
	sublist = link('C', link('A', link('T', link('C', link('A', link('T'))))))
	if dna == sublist:		# if both are same
		return True

	while dna != empty:
		temp = sublist
		if temp != empty:
			while first(dna) == first(temp):		# while firsts are same, 
				dna = rest(dna)
				temp = rest(temp)
				if temp == empty:						# if temp runs out, then sublist exists in s
					return True
				elif dna == empty:
					break
		if dna != empty:					# check if s empty from previous loop
			dna = rest(dna)

	return False



# A set of coins makes change for n if the sum of the values of the coins is n. 
# For example, if you have 1-cent, 2-cent and 4-cent coins, the following sets make change for 7:
#
# 7 1-cent coins
# 5 1-cent, 1 2-cent coins
# 3 1-cent, 2 2-cent coins
# 3 1-cent, 1 4-cent coins
# 1 1-cent, 3 2-cent coins
# 1 1-cent, 1 2-cent, 1 4-cent coins
# Thus there are 6 ways to make change for 7. Write a function count_change that takes a positive integer n 
# and a linked list of the coin denominations and returns the number of 
# ways to make change for n using these coins:

def count_change(amount, denominations):
	"""Returns the number of ways to make change for amount where denominations is a linked list of coins
		in descending sorted order.
	>>> denominations = link(50, link(25, link(10, link(5, link(1)))))
	>>> print_link(denominations)
	50 25 10 5 1
	>>> count_change(7, denominations)
	2
	>>> count_change(100, denominations)
	292
	>>> denominations = link(16, link(8, link(4, link(2, link(1)))))
	>>> print_link(denominations)
	16 8 4 2 1
	>>> count_change(7, denominations)
	6
	>>> count_change(10, denominations)
	14
	>>> count_change(20, denominations)
	60
	"""
	if amount == 0:				# if amount is zero
		return 1
	if (denominations == empty and amount > 0) or amount < 0:	# if denominations empty but amount is larger than 0
		return 0

	return count_change(amount, rest(denominations)) + count_change(amount - first(denominations), denominations) 





# Linked list ADT
# Interface Definitions and Implementations
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)