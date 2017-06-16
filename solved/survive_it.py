"""
Your spaceship is carrying the last few people from Earth towards a distant planet that will become the new home of the Earth civilization. You've just gotten a distress signal, and since nothing could possibly go wrong, you've decided to investigate the source of the signal.

Unfortunately, it turns out that the signal was sent by a hostile alien army. Your spaceship is now facing n alien spacecrafts, and it's your duty to destroy them! Luckily, you have an amazing defense system that destroys half of the hostile army at a time by vaporizing all the enemy spacecrafts that are at odd positions.

The system will keep destroying alien ships until there's only one left. What number will this spacecraft have?

Example

For spacecrafts = 10, the output should be
surviveIt(spacecrafts) = 8.

Initially, there are 10 spacecrafts. After your first attack, only half of them will survive: 2, 4, 6, 8 and 10.
After your second attack, only 2 spacecrafts will remain: 4 and 8.
Finally, spacecraft 4 will be vaporized, so spacecraft 8 will be the only one left.

Output/Input

[time limit] 4000ms (py)
[input] integer spacecrafts

Guaranteed constraints:
1 ≤ spacecrafts ≤ 109.

[output] integer

The number of the last spacecraft to survive your attacks.
~ HOW I SOLVED IT ~
1.) I manually counted and removed digits from odd positions. I even got to 50.
2.) Eventually I found out that by removing every digit in odd position, for every ,
    the remaining numbers would be divisible by 2 to the power of that level (refer below example)

    Example:
    
    if spacecrafts/range of 25:
    level 0    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
    level 1      2   4   6   8   10    12    14    16    18    20    22    24    - divisible by 2
    level 2          4       8         12          16          20          24    - divisible by 4
    level 3                  8                     16                      24    - divisible by 8
    level 4                                        16                            - divisible by 16
 3.) The first thing that came to my mind was to loop 2 to the nth power until it's less than the
    given spacecrafts or range. But it's not efficient. Therefore I did some researching and found out that
    using bitwise operator, "bit and" to get the highest power of 2 of a given number will speed up the calculation.
    Link: http://bit.ly/2rCjRHw

    Explanation:
    Let's say you want to get the highest divisible of power by 2 from 5. n = 5, and n - 1 = 4. 5 & 4 (5 bit and 4)
    would be:
    101 = 5 in binary
   &100 = 4 in binary
   --------
    100 = 4 is the answer. 

    is 4 a power of 2? yes. then that is the answer. 
"""
def surviveIt(spacecrafts):
    while(spacecrafts & spacecrafts - 1 != 0):
        spacecrafts = spacecrafts & spacecrafts - 1
    return spacecrafts

print(surviveIt(10000))
