"""
Given a Latin letter, print its capital form if it's lowercase and print its lowercase otherwise.

[time limit] 4000ms (py)
[input] string arg1

A given string of length 1 representing the character.

[output] string

Desired character.
"""

def CaPsLoCk(arg1):
    ans = ""
    num_val = ord(arg1)
    if(num_val >= 97 and num_val <= 122):
        ans = chr(num_val - 32)
    elif (num_val >= 65 and num_val <= 90):
        ans = chr(num_val + 32)
    return ans
    
CaPsLoCk('B')
CaPsLoCk('z')
CaPsLoCk('r')