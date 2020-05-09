# I comprehend that `sentences` is a list of lines
sentences = []
longest = 0

line = input()

while line:
    # Loop continues as long as `line` is available
    line1 = [' ']*100
    # Keep a track of all the lines
    # Get the length of this line
    length = len(line)

    for i in range(len(line)):
        line1[i] = line[i]
    sentences.append(line1)
    line = input()   
    if length > longest:
        longest = length

for i in range(longest):
    x = ''
    for j in range(len(sentences) - 1, -1, -1):
        x+=sentences[j][i]
    if len(sentences) > 1:
        print(x)

    
sentences = []
