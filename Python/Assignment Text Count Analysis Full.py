# Name: Ho Yeung Chan (Sunny)    Date 10 Aug 2022

# Convert the string to lowercase characters.
s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, 
instead of remaining fixed in their places, move freely about, on or in the surface, 
but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - 
and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, 
I should have said "my universe": but now my mind has been opened to higher views of things."""

s_lower = s.lower()
print(s_lower)

# Split the lowercase string into individual words.
words = list()
words = s_lower.split()
print(words) 

# Remove the punctuation from the lowercase words. Assume that all punctuation 
# is either the first character or the last character of each item in the list.

import string 
punctuation_list =  list(string.punctuation) 

print(words)
w_clean = list()
 
for word in words:
    if len(word) > 1:
        while (word[0] in punctuation_list or word[-1] in punctuation_list):
            if word[0] in punctuation_list:
                word = word[1:]
            elif word[-1] in punctuation_list:
                word = word[0:-1]
    w_clean.append(word)
            
print(w_clean)

# Perform a count analysis on the words without punctuation characters.
print("Number of words is", len(w_clean))
w_clean_set = set(w_clean)
print("Number of distinct words is", len(w_clean_set))

# Display the dictionary with the word counts and the number of distinct words in the original string.
word_freq = dict()
 
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
        
print("Original word counts:", word_freq)
words_set = set(words)
print("Number of distinct words in the orignial string is", len(words_set))
