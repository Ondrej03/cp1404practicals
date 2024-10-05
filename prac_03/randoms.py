"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
 - I see that we generate a random number from 5 to 20, and both of this numbers
    can occur there. The largest I have seen was 20 and the smallest was 7.

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
- I see tht we generate a random number from 3 to 10, with step of two. That
    means that the lowest number can be 3, while the largest one can be 9. 4 can
    not be produced

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
- The largest one was 5.335037769503536, the smallest one 2.960325270402107

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

from random import randrange
print(randrange(1,101))