import re

word_dict={}
char_dict={}
file=open("199801/199801.txt")
txt=file.read()
word_list=re.split(r'[\s\[\]]+', txt)
for word in word_list:
    word_char=word.split("/")
    if len(word_char)<2:
        continue
    word_dict[word_char[0]]=word_dict.setdefault(word_char[0],0)+1
    char_dict[word_char[1]]=char_dict.setdefault(word_char[1],0)+1
    
word_sort=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
char_sort=sorted(char_dict.items(),key=lambda x:x[1],reverse=True)
for i in range(10):
    print(word_sort[i],char_sort[i])

print(word_char)
