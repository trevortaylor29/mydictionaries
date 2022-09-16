import string
infile = open("sometext.txt", 'r')

words = dict()

for line in infile:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    chars = line.split(' ')

    for char in chars:
        if char in words:
            words[char] = words[char] + 1

        else:
            words[char] = 1

print(words)
print(len(words))