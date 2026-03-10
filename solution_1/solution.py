#100 million mails are given which are read into the mails array
from collections import Counter

mails=list(map(str, input().split()))
res=[]
count_mails = Counter(mails)
for mail,count in count_mails.items():
    if count>1:
        res.append(mail)
print(res)
