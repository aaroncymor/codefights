"""
Trick-or-treat! It's Halloween! Like every year, you've decided to distribute candy tonight for all the trick-or-treaters. Your supplies are limited however, and you want to give all of them the same amount for each type of candy.

With a list of every type of candy you have and the number of the average number of kids who knock on your door for the previous years, create a string of instructing how many candies of every kind you should give to each kid. Please do keep in mind that if there are leftover candy that is smaller than the number of kids, do not give them away. Those are for you. The format should be:
"Give <List of candies> to every kid"

You're also trying to make sure there's enough candy for everyone. So if there isn't enough candy of one kind for the trick-or-treaters, you need to remind yourself to buy some more candy by returning a string where it should say:
"Oops! You should buy some more <Missing Candy/Candies>!"

How the array is formatted:

[ ["Candy Type", "Number of Candy"], ["Candy Type 2", "Number of Candy 2"], etc ]

Using an array of every type of candy and its quantity with a number of how many kids there are, return a string with instructions on how many candy of each type you should give to every kid, while making sure there's enough candy for everyone. Extra candy won't be given out if it's less than the number of kids.

Note: Grammar doesn't matter for this question. Just use the candy name given from the list, you don't need to change between the singular or plural form.

Example
For candies = [["Chocolate", "34"], ["Jellybean", "45"]]
and kids = 15, the output should be
givingCandy(candies, kids) = "Give 2 Chocolate and 3 Jellybean to every kid".
"""
import math

def givingCandy(candies, kids):
	str_ans = ""
	div,ediv = [],[]
	cant_give_candy = False
	for candy, qty in candies:
		iqty = int(qty)
		res = math.floor(iqty / kids)

		if res == 0:
			cant_give_candy = True
			ediv.append(candy)
		else:
			div.append([candy,res])

	if cant_give_candy:
		str_ans += "You should buy some more "
		if len(ediv) > 1:
			for a in ediv[:-1]:
				str_ans += a + ', '

			str_ans += "and " + ediv[-1] + "!"
		else:
			str_ans += ediv[0] + "!"
	else:
		str_ans += "Give "
		if len(div) > 1:
			for a,b in div[:-1]:
				str_ans += str(b) + ' ' + a + ', '

			str_ans += "and " + str(div[-1][1]) + ' ' + div[-1][0] + ' to every kid'
		else:
			str_ans += str(div[0][1]) + ' ' + div[0][0] + ' to every kid'

	return str_ans


print(givingCandy([["Chocolate","12"], ["Jellybean", "5"]], 15))
