import random
import string

st = (input("Enter any Message : "))
st1 = (input("Press number for 1:Encodeing and 2:Decoding : "))
words = st.split(" ")
if st1 == "1":    
    nwords =[]
    for word in words:
     if(len(word)>=3):
        random_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
        stNew = random_letters + word[1:] + word[0] + random_letters
        nwords.append(stNew)
     else:
      nwords.append(word[::-1])
    print(" ".join(nwords))

else: 
  nwords = []
  for word in words:
    if len(word)>=3:
     stNew = word[3:-3]
     stNew = stNew[-1] + stNew[:-1]
     nwords.append(stNew)
    else:
     nwords.append(word[::-1])
  print(" ".join(nwords))
 
  