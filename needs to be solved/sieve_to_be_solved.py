"""
https://codility.com/media/train/9-Sieve.pdf
The sieve of Eratosthenes is a famous algorithm that finds all prime numbers up to N. 
The algorithm can be describes as follows:

    Write down all integers between 2 and N, inclusive.
    Find the smallest number not crossed out already and call it P; P is prime.
    Cross out P and all its multiples that aren't already crossed out.
    If some number is not crossed out yet, go to step 2.

Write a program that, given N and K, finds the Kth integer to be crossed out.

Example:

    Sieve(7, 3) = 6
    2,3,5,7

    Sieve(15, 12) = 7
    2,3,4,5,6,7,8,9,10,11,12
    Sieve(10,7) = 9

    [input] integer N

    [input] integer K
        2 <= K < N <= 1000

    [output] integer
        The Kth number to be crossed out.
"""

def Sieve(N):
    numbers = [n for n in range(2,N+1)]
    for i in range(len(numbers)):
        if i + 1 < len(numbers): j = i + 1
        while j < len(numbers):
            if numbers[j] % numbers[i]  == 0:
                numbers.remove(numbers[j])
            j += 1
    return numbers

def sieve_codility(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = 0
    i = 2
    while(i * i <= n):
        print i
        if(sieve[i]):
            k = i * i
            while(k <= n):
                sieve[k] = False
                k += i
        i += 1
    return sieve

print sieve_codility(7)

#print Sieve(15)
