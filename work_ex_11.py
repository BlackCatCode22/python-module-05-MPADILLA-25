# From stephen.marquard|@|uct.ac.za| |Sat Jan 5 09:14:16 2008
#                      21           31

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@') # what is the slicing number for '@'
print(atpos) # >> 21

sppos = data.find(' ', atpos) # what is the slicing number for 'space'.
print(sppos) # >> 31

host = data[atpos+1 : sppos] # what is between slices 21 and 31.
print(host) # >> uct.ac.za
    # Extracting a host name - using find() and string slicing.

# The Double Split Pattern
# From | stephen.marquard@uct.ac.za | Sat | Jan | 5 | 09:14:16 | 2008
#   0               1                   2   3     4       5        6

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

words = line.split() # line: 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
email = words[1] # stephen.marquard@uct.ac.za
pieces = email.split('@') # [stephen.marquard', 'uct.ac.za']
print(pieces[1]) # 'uct.ac.za'

# The Regex Version
# From stephen.marquard@(uct.ac.za) Sat Jan 5 09:14:16 2008

import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y) # >> ['uct.ac.za']
    # '@([^ ]*)'
        # @ = Look through the string until you find (@).
        # [^ ] = Match non-blank character.
        # * = Match many of them.
    
    # '^From .*@([^ ]*)' << More precise
        # ^ = Start at the beginning of the line.
        # From = Loo for the string 'From'.


# Spam Confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))


# Escape Character
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y) # >> $10.00
    # \$[0-9.]+
        # $ = A real dollar sign
        # [0-9.] = A digit or period
        # + = At least one or more
