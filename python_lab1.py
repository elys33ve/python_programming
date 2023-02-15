""" Four Required questions for Lab 1."""
## Modify this file by adding your salutation and code. 
## Once you pass all the doctests, then 
# you can then submit you program for credit. 

_author_ = "Fiona O'Connell"
_credits_ = ["None"]
_email_ = "oconnefa@mail.uc.edu"

# RQ1
def both_negative(x, y):
    """Returns True if both x and y are negative.
 
    >>> both_negative(-1, 1)
    False
    >>> both_negative(1, 2)
    False
    >>> both_negative(-1, -2)
    True
    """

    if x < 0 and y < 0:
        print("True")
    else:
        print("False")
    
 
 
## while Loops ##
# RQ2
def not_factor (n):
    """Prints out all of the numbers that do not divide `n` evenly.
 
    >>> not_factor(10)
    9
    8
    7
    6
    4
    3
    """

    for i in range(n):
        x = n % (n-i)
        if x != 0:
            print(n-i)
 
# RQ3
def lucas(n):
    """Returns the nth Lucas number.
      Lucas numbers form a series similar to Fibonacci:
      2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843,...
 
    >>> lucas(0)
    2
    >>> lucas(1)
    1
    >>> lucas(2)
    3
    >>> lucas(3)
    4
    >>> lucas(11)
    199
    >>> lucas(100)
    792070839848372253127
    """

    # Xn = Xn-1 + Xn-2
    if n == 0:
        print(2)
    elif n == 1:
        print(1)
    elif n == 2:
        print(3)
    else:
        x, x1, x2 = 0, 1, 3
        for i in range(n-2):
            x = x1 + x2
            x1, x2 = x2, x
        print(x)


#RQ4
def gets_discount(p1, p2, p3):
    """ Returns True if p1 is an adult (age at least 18) and one or both of p2 and p3 are children (age 12 or below), 
    False otherwise. Do not use if statement.
    >>> gets_discount(15, 12, 11)
    False
    >>> gets_discount(90, 17, 12)
    True
    >>> gets_discount(18, 18, 18)
    False
    >>> gets_discount(40, 7, 15)
    True
    """

    while p1 >= 18 and (p2 <= 12 or p3 <= 12):
        print("True")
        break
    while p1 < 18 or (p2 > 12 and p3 > 12):
        print("False")
        break

    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
