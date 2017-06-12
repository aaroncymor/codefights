"""
https://codefights.com/challenge/bzkdx7vP3QJ8DgQTL
Given a string s, your mission is to apply the following easy-to-comprehend algorithm to it:

Find all the words in s, where a word is a sequence of consecutive alphanumeric characters with no other letters around it;
Reverse the characters in each word;
For each word, swap the cases of its characters so that the case of a character at each position differs from the case at the corresponding position of the original (unreversed) word.
Return the obtained string as the answer.

Example

For s = "So, what is CodeFights?", the answer should be
reverseInverse(s) = "oS, TAHW SI sTHGiFEDOC?".

There are 4 words in s: "So", "what", "is", and "CodeFights". Let's take the word "CodeFights" as an example:

The letters 'C' at index 0 and letter 'F' at index 4 are uppercase, while all the other letters are lowercase;
"codefights" reversed becomes "sthgifedoc";
With the cases swapped, the letters at indices 0 and 4 should be lowercase and all the other letters should be uppercase;
Thus, the final word is "sTHGiFEDOC".
Input/Output

[time limit] 4000ms (py)
[input] string s

A string containing only alphanumeric characters and punctuation marks.

Guaranteed constraints:
0 ≤ s.length < 500.

[output] string

The result of applying the algorithm described above to s.
"""
sentence = "3 days to go. Get your 100 images for $100."
lst_upper = []
lst_spec = []

for i in range(len(sentence)):
    if(sentence[i].isalnum()):
        if(sentence[i].isupper()):
            lst_upper.append(i)
    else:
        if(sentence[i] != ' '):
            lst_spec.append(i)

i = 0
for num in lst_spec:
    words = sentence[i:num].split(" ")
    rev_words = []
    for word in words:
        rev_word = ""
        for j in range(len(word)-1, -1, -1):
            rev_word += word[j]
        rev_words.append(rev_word)
    sentence = sentence[:i] + ' '.join(rev_words) + sentence[num:]
    #print(sentence)
    i = num + 1

i2 = 0
ans = ""
for i2 in range(len(sentence)):
    if(i2 in lst_upper):
        ans += sentence[i2].lower()
    else:
        ans += sentence[i2].upper()

print(ans)
