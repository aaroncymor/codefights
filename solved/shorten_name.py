"""
You need to insert a bunch of names into the database, but some of them are too large and should be shortened. Each name is given in one of the two formats:

<surname>, <name> <middlename>;
<surname>, <name>.
It is known that <surname> and <middlename> always consist of a single word, and <name> can consist of several words.

Your task is to write a function that will shorten the given name. If it's given in the 1st format, you should cut the middle name and leave only its initial followed by a full stop. If the name is given in the second format, there's no need to shorten it.

Example

For name = "Placedo, Silver Van", the output should be

ShortenName(name) = "Placedo, Silver V".

For name = "Aguilar, Ventura", the output should be

ShortenName(name) = "Aguilar, Ventura".

Input/Output

[time limit] 4000ms (py)
[input] string name

A name in the format given above.

Constraints:

10 ≤ name.length ≤ 60.

[output] string

Shortened name.
"""
def ShortenName(name):
    last_fname = ""
    names = name.split(", ")
    fnames = []
    #print(names)
    if(len(names) > 1):
        fnames = names[len(names)-1].split(" ")
        print(len(fnames), fnames)
        if(len(fnames) > 1):
            fnames[len(fnames)-1] = fnames[len(fnames)-1][0] + '.'
    names[len(names)-1] = " ".join(fnames)
    return ", ".join(names)

print(ShortenName("Daenerys, Aaron"))