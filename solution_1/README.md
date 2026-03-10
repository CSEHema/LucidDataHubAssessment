# Problem Statements: Duplicate Detection 

# You are given a file containing 100 million email addresses. Some emails may appear multiple times. Design a solution to find all duplicate emails efficiently.


 To solve the above question, I have used ## Python as my programming language.

 ## Data Structure used:

 To identify the duplicates, hashmap data structure has been used. It is an efficient data structure, which allows to access the data in O(1) time complexity. Instead of using a data structure like array, which iterates through all elements squentially, to identify any duplicates; we can increase efficiency through hashmap, which takes an average time of O(1) to access, insert or delete the data.

 ## Algorithm used:

 In the provided solution, the emails are stored in a hashmap which stores the email string, and its frequency in the given file. Then we iterate through each of the distinct mails stored in the hashmap, and check if there is any mail that occurs more than once, which is our duplicate mail.

 Then the duplicate mails are stored in an array to print it on to display.


 Another way to this can be to use a hashset, and identify if a given mail has been visited or not. If visited, then it is a duplicate, which can be produced as an output later.

 ## Time complexity:
Iterating and storing all emails into hashmap takes O(n) time. (where n=total number of mails in the given file)

Access of elements in hashmap takes O(1) time.

Iterating through all elements in hashmap takes O(m) time. (where m=distinct number of mails in the given file)

On the total, it takes O(n) time to compute.
 
