#You can download the file from www.py4e.com/code3/mbox-short.txt
'''
Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out
the average spam confidence.
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
'''
name=input('Enter a file name:')
try:
    fhand=open(name)
except:
    print('File can not be opened:',name)
    quit()
total=0
count=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        pos=line.find(':')
        number=line[pos+2:]
        number=float(number)
        total+=number
        count+=1
average=total/count
print('Average spam confidence:',average)
