filename=input("Enter the filename:")
with open(filename,'r')as file:
   text=file.read()
words=text.split()
d={}
for word in words:
   if word  in d:
      d[word]=d[word]+1
   else:
      d[word]=1
max_wrd=max(d,key=d.get)
print("Most frequent word is:",max_wrd)
print("Frequency:",d[max_wrd])
