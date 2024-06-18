s=open("D:\Programing\INTERNAL II\Assig 11.txt" ,mode='r')
number_of_words=0
number_of_words_chars=0
number_of_line=0
for line in s:
    number_of_line+=1
    line=line.strip("\n")
    number_of_words_chars+=len(line)
    list1=line.split()
    number_of_words+=len(list1)
s.close
print("number of lines:" ,number_of_line)
print("number of lines:" ,number_of_words)
print("number of lines:" ,number_of_line)