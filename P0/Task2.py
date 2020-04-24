"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

st={}

for i in calls:
    if i[0] not in st.keys():
        st[i[0]]=int(i[3])
    else:
        st[i[0]]+=int(i[3])    
    if i[1] not in st.keys():
        st[i[1]]=int(i[3])
    else:
        st[i[1]]+=int(i[3])    

ans=0
tele=0
for k in st:
    if (ans<st[k]):
        tele=k;
        ans=st[k]

print(tele, "spent the longest time,", ans, "seconds, on the phone during september 2016.")
