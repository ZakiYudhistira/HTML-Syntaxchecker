import re

filename = "index.html"

f = open(filename, "r")

s = f.read()

tags = re.findall(r'<[^>]+>', s)

tags = map(lambda x: x.strip('\n').strip('\t'), tags)

tags = list(filter(None, tags))
print(tags)

map_val = {
    "<html>" : "h",
    "</html>" : "h",
    "<head>" : "hd",
    "</head>" : "hd",
    "<body>" : "bd",
    "</body>" : "bd"
}

ans = []

for x in tags:
    if x in map_val:
        ans.append(map_val[x])
    #print(temp)


# initiate the machine
map_transition = {}


rules = open('pda.txt', 'r')
for line in rules:
    map_temp = {}
    list_temp = []
    
    line = line.strip('\n')
    x = line.split(' ')
    list_temp.append(x[1])
    list_temp.append(x[3])
    list_temp.append(x[4])
    
    print(x)
    print(map_transition)
    if(x[0] in map_transition):
        print('haha hihio')
        print(x[2])
        map_transition[x[0]][x[2]] = list_temp
        #map_transition[x[0]]
    else:
        map_temp[x[2]] = list_temp
        map_transition[x[0]] = map_temp

print(map_transition)

# start the PDA
isi_stack = ['Z']
currentState = 'Q'

print("--------------------------------------")
ans.append('e')
print(ans)

for inp in ans:
    temp = map_transition[currentState]
    lmao = temp.get(isi_stack[0])
    print(lmao)
    if (lmao[-1] == 'e'):
        isi_stack.pop(0)
    else:
        isi_stack.insert(0, inp)
    currentState = lmao[1]
    
    print('current state:', currentState)
    print('curr stack: ', isi_stack)
    print()
