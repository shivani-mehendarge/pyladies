#!/usr/bin/env python3
def f(fname):
    fobj = open(fname,'w')
    num_count = 0
    print("Enter the text to be entered in the file\n")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)

    fobj.write(text)
    fobj.close()

    fread = open(fname , 'r')
    for l in fread: 	#read line by line
        words = l.split() #words is a list containing each element of the line
        for c in words:
            if c.isalpha() == False:
                num_count += 1
    if num_count == 0:
        print("The file doesnot contain any numbers.")
    else:
        print("The file contains numbers")
    fread.close()
 
if __name__ == '__main__':
    n = input("Enter the name of file to be created: ")
    f(n)
