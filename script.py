f = open('lmao.txt', 'r')
for line in f:
    line = line.split(' ')
    line = [x.strip('\n') for x in line]
    print(f"\'{line[0]}\' : \"{line[1]}\",")