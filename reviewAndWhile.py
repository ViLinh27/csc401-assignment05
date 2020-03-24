#reviewAndWhile.py

####midterm####
'''
can bring one double sided page of notes( or 2 single sided)
hard copy notes(will be collected)
2parts:
multiple choice(like quiz qs)
programming(like hw but on paper)
*****MAKE SURE YOUR INDENTATION IS CLEAR************

to study:
-review quizzes ( may see question that looks like quiz question on exam, but read
it carefully-it might be changed).
-solve problems from book/hw/etc.
-see midtermPractice.py in week 5 notes
'''
###go over quizzes############
'''
look at question 8 of quiz 1 for example of code that is poorly written.
look at question 9 in quiz 1 for mean question about or. OR returns non trivial
non zero expression
quiz 1 question10 gives insgiht on commas in a print and how they make spaces

look over acumulations and searches.

pytho: or can be used for more than just booleans. it's pretty general

python searches locally first then goes globally
'''
###hw q's
'''
5.26-rps
hint-don't use loop
>>>rps('R','S')#player 1 wins
-1
>>>rps('P','S')#player 2 wins
1
>>>rps('S','S')#tie

def rps(p1,p2):
    if/elif/else-how many cases?
    3 or 9?

hints:
p1='R',p2='S'
1) what is p1+p2? 'RS'
2)
>>>y==1 or y==3 or y==5
True
>>>y in [1,3,5]
True
>>>
3) ['RS', 'SP', 'PR']
'''

#5.39-exclamation
'''
hint: don't use replace! (can actually make this work)
acculumator problem

>>>exclamation('moon')
'mooooooooon!'

this is iterating but also modfiying, BE CAREFUL WHEN DOING THIS!!!!!

0) iterate over the word
m
o
o
n
1)detect vowels and multiply tem
>>>exclamation('moon')
m
oooo
oooo
n
2)accumulate that stuff
>>>exclamation("moon')
m
moooo
moooooooo
moooooooon
3) add the !
'''
###review######
'''
two ways to iterate
1)-easier one
>>> s='apple'
>>> for c in s:
	print(c)

	
a
p
p
l
e

2)
>>> #index iteration
>>> s = 'apple'
>>> for i in range(len(s)):
	print(i,s[i])

	
0 a
1 p
2 p
3 l
4 e
>>>

3)
(also a third way:)
>>> s = 'apple'
>>> enumerate(s)
<enumerate object at 0x000001B130682A20>
>>> list(enumerate(s))
[(0, 'a'), (1, 'p'), (2, 'p'), (3, 'l'), (4, 'e')]
>>> for i,c in enumerate(s):
	print(i,c)

	
0 a
1 p
2 p
3 l
4 e
>>>>
'''

#accumulation
'''
4 step process:
0)print version first
1) initialize accumulator before loop(variable with some object)
2)accumulate in loop
3)return after loop
'''

#search pattern
'''
for
    if
        return
return

*******DO NOT PUT IF ELSE IN SIDE LOOP. THAT WILL BE TWO RETURNS THAT WILL MAKE LOOP USELESS
'''
#practice
def f(s):
    x=0
    for i in range(len(s)):
        if s[i]==s[i].upper():
            x+=i
    return x

'''
what is the output?
>>>f('abcABC')
???
>>>('HowAREYou')
>>>
18
'''

def g(nums):
    answer = []
    for num in nums:#checks instances of nums
        if num%2==0:#checks for even numbers
            answer.append(num)
    return answer
'''
>>>g(range(0,100,5))
[0,10,20,30...90]
>>>g(range(0,100,7))
[0,14,28,42...98]
'''

def h(s):######look back at this one
    n=0
    m=0
    for c in s:
        if c not in 'aeiou':
            n+=1
            m=max(m,n)
        else:
            n=0
    return m

'''
n= number of consecutive consonants during iteration
m=max of all n values seen
>>>h('fight')
3
>>>h('bottle')
>>>h('mississippi')
'''
'''
is the given list of numbers always non-decreasing(i.e., either increasing
or constant/level)

>>> isSorted([2,3,3,4,5,7,9,10])
True
>>> isSorted([2,3,3,4,5,2,7,9,10])
False

this is a search for a consecutive pair that decreases. If you find such a pair,
return false,otherwise return true after loop

need indexed iteration in order to look at pairs.

'''

def isSorted(numlst):
    for i in range(len(numlst)):
        #if pair is decreasing
        if numlst[i]>numlst[i+1]:
            #print(i,numlst[i],numlst[i+1])
            return False#in this case you can return early b/c if you find one bad thing then this list will never be sorted
    return True#all data examined first

'''
>>>acronym('Federal Bureau Investigation' )
'FBI'
>>>acronym('national security agency')
'NSA'
'''

def acronym(phrase):
    acro=""
    #iterate over words
    for word in phrase.split():
        acro += word[0]
    return acro.upper()

####while################

'''
while <bool expression>:
    <body>
<rest of your code>

while
-like a repating if statement
-continues to execute body until boolean expression is false, then you continue
with rest of program

use a for loop if you can, but you may have to use a while loop if you don't know
ahead of time what you are going to iterate over.

body of loop many execute an infinte number of times

important : condition needs false condition to get out( or some way of stopping
loop).

loop modifiers-apply to for loops as well
    **eturn-terminates function, hence all loops
    *break-terminates inner most loop
    continue-terminates current iteration, continues with next iteration
    pass-does nothing
'''

#won't cover on midterm!
'''
want this to work:
>>>pigLatin('apple')
'appleay'
>>>pigLatin('pear')
'earpay'

>>>pigLatin('string')
'ingstray'
'''
#v1-only handles one consonant
def pigLatin(word):
    #if consoant, move it to back
    if word[0] not in 'aeiou':
        word = word[1:]+ word[0]
    #always add 'ay'
    return word+ 'ay'

#v2-handles up to 3(or n) consonants
#not ideal
def pigLatin(word):
    #if consoant, move it to back
    if word[0] not in 'aeiou':
        word = word[1:]+ word[0]
    if word[0] not in 'aeiou':
        word = word[1:]+ word[0]
    if word[0] not in 'aeiou':
        word = word[1:]+ word[0]
    #always add 'ay'
    return word+ 'ay'
#v3-handles any number of consonants
def pigLatin(word):
    #if consoant, move it to back
    while word[0] not in 'aeiou':
        word = word[1:]+ word[0]
    #always add 'ay'
    return word+ 'ay'
#ctrl-c can interrupt an execution


def d(n):#looking at digits #called loop invariants
    n= abs(n)
    c=0
    while n>0:
        n//10 # n=n//10
        c+=1
    return c

'''
>>>d(165)
???
>>>d(123456789)
????
'''

#######33user input while

'''
make this work:
>>>SumUser Nums()
Enter a number;12
Enter a number:9
Enter a number:3.3
Enter a number:
24.3
>>>
'''
#accumulator, while
######loop and a half patter#####------good for user input, some people don't like this
def sumUserNums():
    total=0
    ans= input('Enter a number: ') #either a number or ''
    while ans!='':
        total+=eval(ans)
        ans= input('Enter a number: ') #either a number or ''
    return total


#######infinite loop pattern######mimics do while loop

def sumUserNums():
    total=0
    while True:############will technically 
        ans= input('Enter a number: ')
        if ans=='':##############basically condition is at the end of the loop
            break#can return here to make this more succint and get out loop
        else:####more exp;licit, if and else could in theory be flipped
            total+=eval(ans)
    return total



####### rewriting loop as a while ###################3

'''
while loop is more general than a for loop. Every for looop can be rewritten as a while
'''


























