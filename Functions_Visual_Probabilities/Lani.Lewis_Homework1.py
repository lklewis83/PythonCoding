# HOME WORK ASSIGNMENT 1
# Author: Lani Lewis
# Date: 1/21/25

https://thomas-cokelaer.info/tutorials/python/index.html

# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Q1. Please fill in an explanation of each function and an example of how to use it below. 
m = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]
l = [1,2,3,4]

# append() | numpy.append(arr, values, axis=None) Append a single value to the end of an array.
l.append(2)
print("Append 2 to the l list [1,2,3,4]: ", l)
print("-----------------------------------")

# extend() | extend(iterable) Extend an array with more then one value. 
## "If iterable is another array, it must have exactly the same type code; if not, TypeError will be raised."
l.extend([5,6,7,8,9])
print("Extend the l list with 5,6,7,8,9: ", l)
print("-----------------------------------")

# index() | index(x[, start[, stop]]) Returns the index of a specific element in the list
names = ["Blu", "Starr", "Amma", "Bean", "Niece"]
print("This is the list of Nicknames: ", names)
print("Index Number for Starr: ", names.index("Starr"))
print("-----------------------------------")

# insert() | insert(i, x) Insert(position, value) - Inserts a value into a list based on the specified position
l.insert(0,10) # In the first position insert a 10
print("Inserted 10 to the l list: ", l)
print("-----------------------------------")

# remove() | remove(x) Remove the first of "x" occurrence from the array
l.remove(2) # I had two number 2's
print("Remove the first occurence of 2: ", l)
print("-----------------------------------")

# pop() | pop([i]) Removes the last item with the index i from the array
l.append(10)
print("List with additional 10 at the end: ",l)
l.pop(10)
print("Pop will remove the last occurence of 10: ", l)
print("-----------------------------------")

# count() | count(x) Returns the instances in which the specified input occurs in the list
l.append(10)
print("List with additional 10 at the end: ",l)
print("Count how many 10's are in my list: ", l.count(10))
print("-----------------------------------")

# reverse() | Reverses the order of elements in a list
l.reverse()
print("Reverse the order of the l list: ", l)
print("-----------------------------------")

# sort() | numpy.sort(a, axis=-1, kind=None, order=None, *, stable=None) 
## Sorts all the elements in a list in ascending order by default (can be set to descending with sort(reverse=True))
## Beaware of the differences
l.sort()
print("Default SORT Method: ", l)
l.sort(reverse=True)
print("Reverse SORT method: ", l)
print("-----------------------------------")

# Concatenate two lists into one array
print("Concatenate two lists: [1] + [1] = ", [1]+[1])
print("-----------------------------------")

# Duplicate the list and concatenate the duplicate into one array
print("Duplicate and Concatenate: [2] * 2 = ", [2] * 2)
print("-----------------------------------")

# Matrix Index Knowledge [r,c]
# Array Index Knowledge [position]
print("[1,2][1:] | Returns every element of the list starting from index 1 and on... ", [1,2][1:])
print("[1,2,3,4,6][3:] | Returns every element of the list starting from index 1 and on... ", [1,2,3,4,6][3:])
print("-----------------------------------")

# For Loop
print("[x for x in [2,3]] | Returns every value in the given list in list form: ", [x for x in [2,3]])
print("[x for x in [2,3,5,6]] | Returns every value in the given list in list form: ", [x for x in [2,3,5,6]])
print("-----------------------------------")

# For Loop with If statement
print("[x for x in [1,2] if x ==1] | Returns every value that equals 1 in the given list: ", [x for x in [1,2] if x ==1])
print("[x for x in [1,2] if x !=1] | Returns every value that is 'NOT' equal to 1 in the given list: ", [x for x in [1,2] if x !=1])
print("-----------------------------------")

# Complex Multiplication
print("[y*2 for x in [[1,2],[3,4]] for y in x] | Every value in the list [[1,2],[3,4]] is assigned to x.\n"
      "Every value in x is then assigned to y and multiplied by 2, returning: ",
      [y*2 for x in [[1,2],[3,4]] for y in x])
print("-----------------------------------")

# Assign a list to a variable
A = [1]
print("A = [1] - A is now a list containing only the 1 element: ", A)
print("-----------------------------------")

# ------ #
# TUPLES #
# ------ #
# A tuple is an ordered, immutable (you cannot modify the element/s) collection of items. 
# Tuples are defined using parentheses () and can hold a mix of data types.
print("-----------------------------------")
my_tuple = (1, 1, 3.14, 4.5, 4.5, 5, 6, 'Blu', 'Starr', 'Amma', 'Bean', 'Niece', True)
print("My Tuple Example: ", my_tuple)
print("-----------------------------------")

# Tuple | Count()
print("Count how many 1's are in my list: ", my_tuple.count(1))
print("-----------------------------------")

# Tuple | Index()
print("Index Number for Starr from My Tuple: ", my_tuple.index("Starr"))
print("-----------------------------------")

# Build a dictionary from tuples 
starting_tup = ("Apple","Ball","Cat")
print("Starting Tuple before dictionary: ", starting_tup)
tup_dict=dict((x,y) for (x,y) in enumerate(starting_tup))
print("dict((x,y) for (x,y) in enumerate(starting_tup) | Tuple Dictionary; with element index included: ", tup_dict)
print("-----------------------------------")

# Unpack a Tuple
print("Unpack Tuple [x for x in starting_tup] returns original tuple without the index: ", [x for x in starting_tup])
print("-----------------------------------")


# ---------- #
# DICTIONARY #
# ---------- #
# Dictionary with Keys and Values
print("-----------------------------------")
a_dict = {'I love':'you', 'Please do not':'leave'}
print("Dictionary with Keys and Values: ", a_dict)
print("-----------------------------------")

# Another way to return all key-value pairs within a dictionary | items() 
print("a_dict.items() Returns all key-value pairs: ", a_dict.items())
print("-----------------------------------")

# keys() | returns the keys in a dictionary
print("a_dict.keys() Returns dictionary KEYS only: ", a_dict.keys())
print("-----------------------------------")

# values() | returns the values in a dictionary
print("a_dict.values() Returns dictionary VALUES only: ", a_dict.values())
print("-----------------------------------")

# Boolean Searches
## Search for a specific KEY
print("Boolean Search | Does dicitionary have the word 'Never' in it?: ", 'never' in a_dict)
print("-----------------------------------")

# Delete any entry with a matching Key from dictionary
## ERROR VERSION
#a_dict.__delitem__('me')
# print("Attempt to delete any entry for 'me': ", a_dict)
print("---------KeyError: 'me'-----------")
print("-----------------------------------")

## WORKING VERSION
print("DICTIONARY CHECK: ", a_dict)
a_dict.__delitem__('I love')
print("Attempt to delete a Key and Value for 'I love': ", a_dict)
print("-----------------------------------")

# CLEAR THE ENTIRE DICTIONARY
a_dict.clear()
print("Check that my dictionary has been cleared and is now empty: ", a_dict)
print("-----------------------------------")

# ---- #
# SETS #
# ---- #

set1 = {1,2,3,4,5}
print("-----------------------------------")
print("SET1 CHECK: ", set1)
print("-----------------------------------")

# add() a single entry to the set
set1.add(6)
print("Add the number 6 to the set1", set1)
print("-----------------------------------")

# copy() all elements in a set
set2 = set1.copy()
print("This is a copy of set1:", set2)
print("-----------------------------------")

# discard() a single element from the set
set2.discard(6)
print("I want to discard the value 6 from the set1:", set2)
print("-----------------------------------")

set2.add(8)
print("Set 1 Check:", set1)
print("Set 2 Check:", set2)

# difference() between sets
set_diff = set1.difference(set2)
print("This is the difference between set1 and set2:", set_diff)

set_diff2 = set2.difference(set1)
print("This is the difference between set2 and set1:", set_diff2)
print("-----------------------------------")

# intersection() | Returns similar entries from multiple sets
set_inter = set1.intersection(set2)
print("These are the similar entries between set1 and set2:", set_inter)
print("-----------------------------------")

# issubset() | Boolean | Only returns True if all the elements in the method set are present within the method input set
set3 = {1,2,3}
print("Set 1 Check:", set1)
print("Set 2 Check:", set2)
print("Set 3 Check:", set3)
subset_check = set1.issubset(set2)
print("Boolean Subset Check for set1 compared to set2:", subset_check)
print("Order Matters with issubset()")
subset_check2 = set3.issubset(set2)
print("Boolean Subset Check for set3 compared to set2:", subset_check2)
print("-----------------------------------")

# Clear and delete entire set
set3.clear()
print("Check that I have cleared set3:", set3)
print("-----------------------------------")

# pop() | Removes a random element from the set
set1.pop()
print("POP removes a random entry from set1:", set1)
print("-----------------------------------")

# remove() | Similar to pop, though no values are returned. 
## Instead, the specified value is just removed
set2.remove(2)
print("REMOVEs a specific entry '2' from set2:", set2)
print("-----------------------------------")

# union() - Returns a set that represents the union between multiple sets
set3 = set1.union(set2)
print("UNION of set1 and set2 to create set3:", set3)
print("-----------------------------------")

# update() - concatenates one set with the second set
## Can not assign to a variable otherwise you will get 'none'
set3.update(set2)
print("UPDATE concatenates set3 with set2:", set3)
print("-----------------------------------")

# ------- #
# STRINGS #
# ------- #
str1 = "lani lewis"
print("STRING1:", str1)
print("-----------------------------------")

# capitalize() | capitalizes the first character in the string if the character is a letter. 
## The remaining letter characters are converted to lowercase.
print("CAPITALIZE the first character in the string:", str1.capitalize())
print("-----------------------------------")

# casefold() | converts all letter characters into lowercase
print("CASEFOLD converts all letter characters into lowercase:",str1.casefold())
print("-----------------------------------")

# center() | creates evenly sized white-space on either side of the method string until the total number of characters 
## and whitespace equals the specified character limit
txt="a"
print("CENTER text 'a' with whitespace of 20 cushion")
print("-",txt.center(20),"-")
print("-----------------------------------")

# count() | counts the instances in which a given character appears within a string. 
## IS CASE SENSITIVE
print(str1)
print("COUNT how many times the character 'l' was used:",str1.count("l"))
print("-----------------------------------")

# encode() | encodes a string into a specified format and either 
## replaces or ignores anomalous characters based on a specified input
print("ENCODE string1 as ascii:",str1.encode('ascii', errors='replace'))
print("-----------------------------------")

# find() | returns the  index number of the first appearance of a specified character
print("FIND the index of the first occurance of 'l':", str1.find("l"))
print("-----------------------------------")

# partition() | returns a tuple that contains three strings.
print("PARTITION original string by a different string", str1.partition('lew'))
print("-----------------------------------")

# replace() | replaces one set of characters in the string with another set of characters
love = "I Love NewYork!"
print("Original Sentence:", love)
print("REPLACE the word NewYork with Texas:", love.replace("NewYork", "Texas"))
print("-----------------------------------")

# split() | separates characters in a string based on a separator character. 
## The default separator is white-space.
print("SPLIT my sentence by the whitespace:",love.split())
print("-----------------------------------")

# title() | capitalizes the first letter of each word in a string.
print("Original Text:", str1)
print("TITLE capitalizes the first letter of each word in a string:",str1.title())
print("-----------------------------------")

# zfill() - Returns a string of specified length where the final characters are the original string 
## and all other prior characters are 0
print("ZFILL returns a specified length of 15 and fills in the extra with zero:", str1.zfill(15))
print("-----------------------------------")

# 
# https://docs.python.org/3/library/collections.html#collections.Counter
# https://www.hackerrank.com/challenges/collections-counter/problem
# 

from collections import Counter
# collections.Counter()
## A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
print("My list:", l)
count1 = Counter(l)
print("Counter() | Count the times my list item appears:", count1)
print("A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.")
print("-----------------------------------")

# copy() - Copies every item in the counter and returns each copied element in dict form
lcopy = Counter(l).copy()
print("This is a copy of my previous counter container:", lcopy)
print("-----------------------------------")

# elements() - Returns a data structure composed of several instances of each unique value in the counter. 
## The number of instances of each value is equal to their value count
print("This is very similar to the copy function:",Counter(l).elements)
print("-----------------------------------")

# get() - Retrieves the value corresponding to the specified key
print("GET the value for the key# 10:",Counter(l).get(10))
print("-----------------------------------")

# keys() - Returns all keys in a counter
print("Another way to show the KEYS:",Counter(l).keys())
print("-----------------------------------")

# items() - Returns all key and value as a pairs
print("Returns all key and value as a pairs:", Counter(l).items())
print("-----------------------------------")

# most_common() - Returns a list of tuples where each tuple contains both the key and the value of the counter.
## The list is sorted in descending order based on the value of the key
l2 = l.copy()
l2.extend([10,7,5,10,5,1,10,7,5])
print("Extended List:",l2)
print("Counter for the extended list:",Counter(l2))
print(" ")
print("MOST_COMMON sorts the list in descending order based on the value of the key:",Counter(l2).most_common())
print("-----------------------------------")

# pop() - Removes EVERYTHING except the value corresponding to the input key
print("POP removes EVERYTHING except the value corresponding to the input key# 10 (l2):",Counter(l2).pop(10))
print("-----------------------------------")

# setdefault() - Returns the value corresponding with the input key. 
## If the key does not exist, insert the key into the Counter and assign it a value corresponding with the second method input
print("Reminder of List1 Counter:",Counter(l))
print("SETDEFAULT Returns the value corresponding with the input key# 10:",Counter(l).setdefault(10))
print("-----------------------------------")

# clear() - Removes every item in the counter, returning an empty counter
print("CLEAR Removes every item in the counter l2",Counter(l2).clear())
print("-----------------------------------")

# ----- #
# BONUS #
# ----- #
# https://docs.python.org/3/library/itertools.html
from itertools import cycle, islice
flower_orders=['W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','B/Y','B/Y','B/Y','B/Y','B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/G','W/G','W/G','W/G','R/Y','R/Y','R/Y','R/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','W/R/B/V','W/R/B/V','W/R/B/V','W/R/B/V','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','N/R/Y','N/R/Y','N/R/Y','W/V/O','W/V/O','W/V/O','W/N/R/Y','W/N/R/Y','W/N/R/Y','R/B/V/Y','R/B/V/Y','R/B/V/Y','W/R/V/Y','W/R/V/Y','W/R/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/N/R/B/Y','W/N/R/B/Y','W/N/R/B/Y','R/G','R/G','B/V/Y','B/V/Y','N/B/Y','N/B/Y','W/B/Y','W/B/Y','W/N/B','W/N/B','W/N/R','W/N/R','W/N/B/Y','W/N/B/Y','W/B/V/Y','W/B/V/Y','W/N/R/B/V/Y/G/M','W/N/R/B/V/Y/G/M','B/R','N/R','V/Y','V','N/R/V','N/V/Y','R/B/O','W/B/V','W/V/Y','W/N/R/B','W/N/R/O','W/N/R/G','W/N/V/Y','W/N/Y/M','N/R/B/Y','N/B/V/Y','R/V/Y/O','W/B/V/M','W/B/V/O','N/R/B/Y/M','N/R/V/O/M','W/N/R/Y/G','N/R/B/V/Y','W/R/B/V/Y/P','W/N/R/B/Y/G','W/N/R/B/V/O/M','W/N/R/B/V/Y/M','W/N/B/V/Y/G/M','W/N/B/V/V/Y/P']
#print(flower_orders)

# Counter()
cont_flow = Counter(flower_orders)
print("This is the Counter Object for Flower Orders:",cont_flow)
print("-----------------------------------")

# Count how many objects have color W in them
## For Loop goes through Keys looking for 'W'
cont_w = sum(1 for key in cont_flow if 'W' in key)
print("Count how many objects have color 'W' in them:", cont_w)
print("-----------------------------------")

# Histogram Assignment
## Grab Count for Keys
color_cnt = Counter() # Placeholder
for key, count in cont_flow.items():
    colors = key.split('/')  #'R/B/V/Y' | Splits these color codes
    for rgb_c in colors:
        color_cnt[rgb_c] += count
        #print(color_cnt)
        #print("--------")

## Create a List of Colors and their Counts
### LAMDA MAGIC | Sort colors by count in descending order
sort_color_cnt = sorted(color_cnt.items(), key=lambda x: x[1], reverse=True)
#### key=lambda x: x[1] ensures sorting is based on the count (value).
#### reverse=True makes the sorting in descending order (largest to smallest count).

# ZIP() Unzip sorted data into colors and counts
colors, counts = zip(*sort_color_cnt)

#sort_color_cnt = color_cnt.most_common()
print("Entire list of RGB Color Keys and it's count:",sort_color_cnt)
print("-----------------------------------")
#colors = list(color_cnt.keys())
#counts = list(color_cnt.values()) 
  

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
## ACTUAL HISTOGRAM/BAR CHART
plt.bar(colors,counts)
# hist causes an error so I used bar intead
plt.xlabel("Colors")
plt.ylabel("Count")
plt.title("Histogram of Flower Colors")
plt.show()

from itertools import combinations
# RANKINGS #
pairs_cnt = Counter() # placeholder

for key in flower_orders:
      colors = key.split('/')
      pairs = combinations(colors, 2)
      pairs_cnt.update(pairs)

print("Pair COMBINATION of colors:",pairs_cnt)  
print("Ranked Pairs of Colors:")
for pairs in pairs_cnt.most_common():
     print(f"{pairs}") 
print("-----------------------------------")   

triplet_cnt = Counter() # Container placeholder
all_colors = set() # List placeholder

for key in flower_orders:
      colors = key.split('/')
      all_colors.update(key.split('/'))
      sets = combinations(colors, 3)
      triplet_cnt.update(sets)

print("Triplet COMBINATION of colors:",triplet_cnt)  
print("Ranked Triplet of Colors:")
for sets in triplet_cnt.most_common():
     print(f"{sets}") 
print("-----------------------------------")  



#  Make a dictionary with key=”color” and values = “what other colors it is ordered with”.
set_key = []
counts = []

print(triplet_cnt.items())
for key, count in triplet_cnt.items():
     new_key = ''.join(key) # REMOVES '/'
     set_key.append(new_key)
     counts.append(count)

#print(set_key)
#print(counts)

# Sort the keys and counts based on counts (descending order)
## LAMBDA MAGIC
sorted_data = sorted(zip(set_key, counts), key=lambda x: x[1], reverse=True)
set_key, counts = zip(*sorted_data)
print("Sorted Keys:", set_key)
print("Sorted Counts:", counts)
print("-----------------------------------")  

# Histogram
plt.bar(set_key,counts)
plt.xlabel("Triplets")
plt.ylabel("Count")
plt.title("Histogram of Triplets")
plt.show()

# ------------------- #
# Numpy Square Matrix #
# ------------------- #
# Make a graph showing the probability of having an edge between two colors based on how often they co-occur.

## step1: place holders for counting
print("Reminder of ALL Colors:", colors)
print("Reminder of Color Pairs:", pairs_cnt)

## step2: Compute probabilities
total_pairs = sum(pairs_cnt.values()) 
print("Total number of pairs:", total_pairs)
color_list = sorted(all_colors)
print("Color list:", color_list)
color_idx = {color: i for i, color in enumerate(color_list)}
print("Color Index:", color_idx)

## step3: Create a square matrix
print("Create a Square Matrix:")
matrix_size = len(color_list)
print("Color List Matrix Size:", matrix_size)
prob_matrix = np.zeros((matrix_size,matrix_size)) # Create a matrix with zeros
print("Zero Matrix:", prob_matrix)

## step4: fill the matrix with probabilities
for (cnt1, cnt2), count in pairs_cnt.items():
      i,j = color_idx[cnt1], color_idx[cnt2]
      prob = count / total_pairs
      prob_matrix[i,j] = prob
      prob_matrix[j,i] = prob # Ensure Sysmetry
print("Probability Matrix:", prob_matrix)  
print("-----------------------------------")     

## step5: PLOT PROBABILITIES
### An imshow chart is a visualization technique in Python, 
### often used to display data in a 2D array or matrix as an image. 
plt.imshow(prob_matrix, cmap="ocean", interpolation='nearest')
plt.colorbar(label="Probability")
plt.title("Probability Matrix")
plt.show()

print("10 BUSINESS QUESTIONS")
print("---------------------")
print("Q1: What is the first most commonly seen color?")
print(" \n")
print("Q2: Which color PAIRS are most frequently ordered together?")
print(" \n")
print("Q3: Which color TRIPLETS are most frequently ordered together?")
print(" \n")
print("Q4: What is the least commonly seen color?")
print(" \n")
print("Q5: How many colors do we have in our set?")
print(" \n")
print("Q6: How many color PAIRS can we make?")
print(" \n")
print("Q7: How many color TRIPLET SETS can we make?")
print(" \n")
print("Q8: Is there any high probability suggesting our colors are similar or in the same family?")
print(" \n")
print("Q9: How many Flower Colors had 'W' in them?")
print(" \n")
print("Q10: What is the most common Flower Color Order?")
print("-----------------------------------") 

dead_men_tell_tales = [] # placeholder
dead_men_tell_tales = ['Four score and seven years ago our fathers brought forth on this',
'continent a new nation, conceived in liberty and dedicated to the',
'proposition that all men are created equal. Now we are engaged in',
'a great civil war, testing whether that nation or any nation so',
'conceived and so dedicated can long endure. We are met on a great',
'battlefield of that war. We have come to dedicate a portion of',
'that field as a final resting-place for those who here gave their',
'lives that that nation might live. It is altogether fitting and',
'proper that we should do this. But in a larger sense, we cannot',
'dedicate, we cannot consecrate, we cannot hallow this ground.',
'The brave men, living and dead who struggled here have consecrated',
'it far above our poor power to add or detract. The world will',
'little note nor long remember what we say here, but it can never',
'forget what they did here. It is for us the living rather to be',
'dedicated here to the unfinished work which they who fought here',
'have thus far so nobly advanced. It is rather for us to be here',
'dedicated to the great task remaining before us--that from these',
'honored dead we take increased devotion to that cause for which',
'they gave the last full measure of devotion--that we here highly',
'resolve that these dead shall not have died in vain, that this',
'nation under God shall have a new birth of freedom, and that',
'government of the people, by the people, for the people shall',
'not perish from the earth.']

print("UNCLEANED STORY:")
print("----------------")
print(dead_men_tell_tales)
print("-----------------------------------") 

# join() a list into a single string
cleaned_story = " ".join(dead_men_tell_tales)

print("CLEANED JOINED STORY:")
print("----------------")
print(cleaned_story)
print("-----------------------------------") 

# Remove() doesn't exist so I have to replace instead...
## Replace() space with no space at all
removed_space = cleaned_story.replace(" ","")
print("REMOVE SPACES FROM STORY:")
print("----------------")
print(removed_space)
print("-----------------------------------") 

# Count() Letter Occurances
removed_space = removed_space.lower()
letter_cnt = Counter(removed_space)
print("Letter Occurance:", letter_cnt)

# Sum() of all Letters
total_let = letter_cnt.values()
sum_let = sum(total_let)
print("SUM of Total Number of Letters:", sum_let)

# Probability of a letter
let_probs = {letter: count / sum_let for letter, count in letter_cnt.items()}

# Sorted Probability List | LAMDA MAGIC
sorted_probs = dict(sorted(let_probs.items(), key=lambda x: x[1], reverse=True))
print("Letter Probability:", sorted_probs)
print("-----------------------------------") 

# Histogram
plt.bar(sorted_probs.keys(),sorted_probs.values())
plt.xlabel("Letters")
plt.ylabel("Counts")
plt.title("Histogram of Letter Probabilities")
plt.show()

# 4. Tell me transition probabilities for every pair of letters
## This question was hard to understand what the request was and I did need help to understand
## Might be nice in the future if there was an example of the output?

from collections import defaultdict
# BIGRAMS #

# Count occurrences of bigrams (pairs of letters)
bigrams = [removed_space[i:i+2] for i in range(len(removed_space) - 1)]
print("Bigrams:", bigrams)
print("\n")
bigram_cnt = Counter(bigrams)
print("Bigram Creates a list of all possible pairs. Here is the bigram and their counts:",bigram_cnt)

# Calculate Transition Probabilities
transition_prob = defaultdict(dict) # placeholder

for bigram, count in bigram_cnt.items():
      first_let = bigram[0]
      # print(first_let)
      # print(count / letter_cnt[first_let])
      transition_prob[first_let][bigram] = count / letter_cnt[first_let]

for letter, trans in transition_prob.items():
      print(f"Transition probabilities for '{letter}':")
      for bigram, probs in trans.items():
            print(f"{bigram} -> {probs:.4f}")

# Make a 26x26 graph of 4. in numpy #
## representing the transition probabilities between all 26 letters of the English alphabet.

# Store Alphabet For Reference
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Create Matrix Structure
trans_matrix = np.zeros((26,26)) 

# Fill in Matrix
for bigram, count in bigram_cnt.items():
      row = ord(bigram[0]) - ord('a') # Map first letter to first row
      col = ord(bigram[1]) - ord('a') # Map first letter to first column to create the Probability Matrix
      
      if 0 <= row < 26 and 0 <= col < 26:
            b_prob = count / letter_cnt[bigram[0]]
            trans_matrix[row,col] = b_prob
            # trans_matrix[col,row] = b_prob

# print(trans_matrix)

plt.imshow(trans_matrix, cmap='Blues', interpolation='nearest')
plt.title("Letter Transistion Probabilities (26 x 26)")
plt.xlabel("Next Letter")
plt.ylabel("Current Letter")
plt.colorbar(label="Probabilities")
plt.show()