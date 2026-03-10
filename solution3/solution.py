from collections import Counter
import pandas as pd

action_file = pd.read_csv()

time_stamp=action_file['timestamp']
users = action_file['user_id']
actions = action_file['action']

# Most active user
user_action=Counter(users)
maximum_active=0
res_user=''

for user,freq in user_action.items():
    if freq>maximum_active:
        maximum_active=freq   # High frequency of activity-> Most active user
        res_user=user
print('User: ',res_user)


#Most common action
action_count=Counter(actions)
maximum_freq=0
res_action=''
for action, freq in action_count.items():
    if freq>maximum:
        maximum_freq=freq  # High frequency of actions -> Most common action
        res_action=action
print('Action: ',res_action)

