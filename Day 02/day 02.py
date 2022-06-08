'''
https://adventofcode.com/2021/day/2
'''
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
file.close()


########### D  F
position = [0, 0]

for line in lines:
    dir, pos = line.strip().split(" ")
    if dir == "up":
        position[0] = position[0] - int(pos)
    if dir == "down":
        position[0] = position[0] + int(pos)
    if dir == "forward":
        position[1] = position[1] + int(pos)
#    print(dir, pos, position)

print("Star 1: ", position[0] * position[1])



########### D  F  A
position = [0, 0, 0]

for line in lines:
    dir, pos = line.strip().split(" ")
    if dir == "up":
#        position[0] = position[0] - int(pos)
        position[2] = position[2] - int(pos)
    if dir == "down":
#        position[0] = position[0] + int(pos)
        position[2] = position[2] + int(pos)
    if dir == "forward":
        position[1] = position[1] + int(pos)
        position[0] = position[0] + position[2] * int(pos)
#    print(dir, pos, position)

print("Star 2: ", position[0] * position[1])