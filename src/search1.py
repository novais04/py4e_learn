'''
consultado só os emails do arquivo mbox-short.txt
'''

fhand = open('../src/mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith("From: "):
        print(line)