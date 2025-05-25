
# Problem 22 input
with open("./data/0022_names.txt", "r", encoding="utf-8") as f:
    inputText22 = f.read().replace('"', '').split(',')

#print(inputText22)
#print(len(inputText22))
#names = inputText22.split()

# sort in alphabetical order
inputText22.sort()
#print(inputText22)


def alphabetical_value(word):
    val = 0
    for c in word:
        val = val + ord(c) - 64
    return val


print(alphabetical_value('COLIN'))

totalScore = 0
for index, w in enumerate(inputText22):
    score = (index + 1) * alphabetical_value(w)
    #if w == 'COLIN':
    #    print(w,":",score)
    #    break
    totalScore = totalScore + score

print("Total score:", totalScore)
