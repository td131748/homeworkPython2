#Instructions
#Please write a program that:
#1. reads a text file containing some English text and counts all words that are:
#a) at least 4 letters long and
#2. Print a list of those words and the number of their occurrences

my_file = 'text.txt'
f = open(my_file, 'r')
lines = f.readlines()
i = 0
word_count_1 = 0
word_list_1=[]
for line in lines:
    i += 1
    words = line.split()
    for word in words:
        if len(word) >= 4:
            word_count_1 += 1
            word_list_1.append(word)

sentence_1 = "Number of words that are at least 4 letters long:"
print(sentence_1,word_count_1)
print(word_list_1)

#b) start with a capital letter or are all capitalized (abbreviations etc.)
#2. Print a list of those words and the number of their occurrences

my_file = 'text.txt'
f = open(my_file, 'r')
lines = f.readlines()
i = 0

word_count_2 = 0
word_list_2=[]
for line in lines:
    i += 1
    words = line.split()
    for word in words:
        if word[0].isupper() or word.isupper():
            word_count_2 += 1
            word_list_2.append(word)

sentence_2 = 'Number of words that start with a capital letter or are all capitalized:'
print(sentence_2, word_count_2)
print(word_list_2)

#3. Use matplotlib or plotly and generate a bar chart showing the top 10 most common words
# (same conditions 1a) and 1b) apply) with the number of their occurrences in descending order.
# Save this plot to a file and submit it along the code.

import matplotlib.pyplot as plt
word_list_3 = word_list_1 + word_list_2

word_count = {}
for word in word_list_3:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

from collections import Counter
word_counter = Counter(word_list_3)
most_common = word_counter.most_common(10)
x, y = zip(*most_common)

plt.bar(x, y)
plt.xlabel('x')
plt.xticks(rotation=20, ha='right')
plt.ylabel('Number of word occurrences')
plt.title('Top 10 occurrences of words with two conditions')
plt.savefig('Top 10 occurrences of words with two conditions')
plt.show()

#4. For an extra 1 point play with packages that generate clouds of words and generate one for this set of words (conditions 1a) and 1b)) as well as for the whole text.

from wordcloud import WordCloud

word_string_3 = ' '.join(word_list_3)
wordcloud = WordCloud(width=1000, height=1000, background_color='white').generate(word_string_3)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('Wordcloud')
plt.show()

#Please submit the result as individual files to teams (not zipped).
# These should include: the code, the text file and the graphics files (i.e. png) with the appropriate charts and word clouds.

#Hint: Please note you can use a dictionary structure.

