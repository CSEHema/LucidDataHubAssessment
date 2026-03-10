# Problem Statement: Top Frequent Words (Data Processing) 
You are given a text file containing millions of words (one word per line). 

Example: 
apple
banana
apple
orange
banana
apple 

# Task :Write a program that returns the top 10 most frequent words. Requirements 
# Handle large files efficiently. 


To solve the above problem, I have used SQL. I have considered that the data is being provided in a table named # word_counts 
with the columns word_id(int) and word(string).

## Approach

To solve the problem, firstly I have taken word and their frequency as a seperate table. Then I have performed a window function(rank) that ranks the words based on their frequencies. To obtain the top 10 frequent words, I have filtered using WHERE rank was greater than or equal to 10. To sort it based on their frequency, I have used ORDER BY that sorts the obtained result in ascending order of their frequencies. The program produces the word, and frequency as the output.
