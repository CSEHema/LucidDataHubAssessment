# Problem Statement: Log Analysis

You are given a file containing system logs in the format: timestamp, user_id, action 
Example: 
10:01,user1,login
10:03,user2,search
10:05,user1,purchase
10:07,user2,search
10:10,user3,login 
Task Write a program to compute: 
 
 The most active user (user with highest number of actions) 
 
 The most common action 


 To solve this problem, I have used # Python
 as the programming language. 

 ## Approach:

 For this problem, I have assumed that the input is given as a .csv file, which can be read through pandas. I have taken my necessary data, user_id, actions and timestamp into separate arrays for easy access. 

 ### To identify the most active user

 To identify the most active user, I have considered the users in the user array, represented by their user_ids. Then I went ahead and generated a hashmap of users along with their actions frequency. Then I have produced the user with the highest action frequency as the output. 

 ## To identify the most common action

 To identify the most common action, I have generated the hashmap for the actions and their frequencies. Thereby, the action with the highest frequency is produced as the output.

 ## Time Complexity

 For the above solution, forming the hashmap takes O(n) time, and iterating through all unique users/actions takes O(m) time, where n is the total number of users/actions and m is the number of unique users/actions. Overall, the solution takes O(n) time.
