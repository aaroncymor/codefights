"""
There is a promotional offer in a bookstore: "Take 3, pay 
for 2 most expensive ones". So, each customer who picks 3 
books gets the cheapest one for free. Of course, the customer 
can take even more books and, depending on the way the books 
are arranged into groups of three, get the cheapest one in each 
group for free.

The lady working in the bookstore is well-intentioned and always 
wants to lower the price for each customer. For the given book 
prices p, help the lady to arrange the books into groups in the best 
way possible, so that the total price the customer has to pay is 
minimized.

Please note: the number of books isn't necessarily divisible by 3.

For n = 7 and p = [10,3,2,4,6,4,9], the answer is
offer(n, p) = 29.

The customer can divide the books, for example, into the following groups:
 (10, 3, 2), (4, 6, 4) and (9). This way he will have to pay (10 + 3) + (4 + 6) + 9 = 32.
However, there's another option that the nice lady can suggest: (10, 6, 9), (3, 4, 4) and (2). In this case the customer will have to pay (10 + 9) + (4 + 4) + 2 = 29, which is the best price.
"""

def offer(n, p):
	x = sorted(p)[::-1]
	s = 0
	for i in range(len(x)):
		if i % 3 == 2:
			continue
		else:
			s += x[i]
	return s

print offer(7,[10, 3, 2, 4, 6, 4, 9])