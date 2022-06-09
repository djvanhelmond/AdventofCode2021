'''
https://adventofcode.com/2021/day/3
'''
#filename = 'testinput.txt'
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
file.close()

#print(lines)
length = len(lines)

zeroes = [0 for i in range(len(lines[0])-1)]
ones = [0 for i in range(len(lines[0])-1)]
outcome = [0 for i in range(len(lines[0])-1)]

for str in lines:
    val = list(str.strip())
#    print(val)
    for i in range(len(val)):
        if val[i] == '0': zeroes[i] = zeroes[i] + 1
        if val[i] == '1': ones[i] = ones[i] + 1

#print(zeroes)
#print(ones)

for i in range(len(zeroes)):
    if zeroes[i] > ones[i]: outcome[i] = 0
    if zeroes[i] < ones[i]: outcome[i] = 1

gamma = 0
epsilon = 0
exp = 0
for i in range(len(outcome)):
    val = outcome.pop()
    gamma = gamma + (val * 2**exp)
    if val ==0: invval = 1
    if val ==1: invval = 0
    epsilon = epsilon + (invval * 2**exp)
    exp = exp + 1

#print(gamma)
#print(epsilon)

print("Star 1: ", gamma * epsilon)
