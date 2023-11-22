import re
import json
from colorama import Fore, Back, Style

filename = "index.html"

f = open(filename, "r")

s = f.read()
tags = re.findall(r'[^\n\t]+', s)
tags_real = []
for lmao in tags:
    tags = re.findall(r'<[^>]+>', lmao)
    if tags == []:
        tags_real.append(lmao)
    else:
        tags_real.extend(tags)
#tags = re.findall(r'\n[^\n]+', s)
print("tags_real:", tags_real)
tags = map(lambda x: x.strip('\n').strip('\t'), tags_real)
tags = list(filter(None, tags))
print(tags)

arr_temp = []
arr_temp.extend(tags)

map_val = {
    "<html>" : "H",
    "</html>" : "H",
    "<head>" : "hd",
    "</head>" : "hd",
    "<body>" : "bd",
    "</body>" : "bd",
    "<title>" : "T",
    "</title>" : "T",
    "<link>" : "L",
    "</link>" : "L",
    "<script>" : "s",
    "</script>" : "s",
    "<p>" : "p",
    "</p>" : "p",
    "<br>" : "br",
    "<div>" : "dv",
    "</div>" : "dv",
    "<illegalStr>" : "str",
}

def printError(x, pos):
    # check in file which line
    f = open("index.html", "r")
    i = 1
    for line in f:
        if x in line:
            break
        i+=1
    
    # print err message
    
    print(Fore.RED + "+" + "-"*(len(x)+9 + len(str(i))) + "+")
    print("| Line " + str(i) + ": " + x + " |")
    print("+" + "-"*(len(x)+9 + len(str(i))) + "+")
    #print("-" * (pos) + "↑")
    print("Syntax Error" + Style.RESET_ALL)
        

def validateGlob(search, glob_idStr):
    result = [m.start() for m in re.finditer('(?=%s)(?!.{1,%d}%s)' % (search, len(search)-1, search), glob_idStr)]
    #print(glob_idStr)
    #print(result)
    
    isEqual = False
    for x in result:
        isEqual = False
        char_temp = ""
        haha = 0
        state = False
        for i in range(x, len(glob_idStr)):
            if glob_idStr[i] == '=':
                if(search != char_temp):
                    print(search, char_temp)
                    return False
                else:
                    char_temp = ""
                    isEqual = True
                    continue
            elif glob_idStr[i] == '"':
                haha+=1
            else:
                char_temp += glob_idStr[i]
            
            if haha == 2:
                state = True
                break
            #print(glob_idStr[i])
        if not state:
            return False
        #print(char_temp, haha, state)
    if (result == [] or result == None):
        return True

    return True and isEqual


# ini TOKENIZER
ans = []

for x in tags:
    temp = x[1:-1]
    temp = temp.split(' ')
    # check illegal string
    if('<'+temp[0]+'>' not in map_val and x[0] != '<'):
        temp = ['illegalStr']
    # check wrong tag name
    if('<'+temp[0]+'>' not in map_val):
        print('FAILED awikwok')
        printError(x, 1)
        exit()
    
    # check global identifier
    glob_id = ''.join(temp[1:])
    if glob_id != '':
        xId = validateGlob('id', glob_id)
        xClass = validateGlob('class', glob_id)
        xStyle = validateGlob('style', glob_id)

        print(xId, xClass, xStyle)
        if(not(xId and xClass and xStyle)):
            print('Failed awikwok')
            printError(x, 1)
            exit()

    # add to ans
    x = '<' + temp[0] + '>'
    if x in map_val:
        ans.append(map_val[x])
    #print(temp)


# initiate the machine
map_transition = {}


print("--------------------------------------------")
rules = open('pda.txt', 'r')
for line in rules:
    map_temp = {}
    map_temp2 = {}
    list_temp = []
    
    line = line.strip('\n')
    x = line.split(' ')
    #list_temp.append(x[1])
    list_temp.append(x[3])
    list_temp.append(x[4])
    
    if(x[0] in map_transition):
        if(x[1] in map_transition[x[0]]):
            map_temp2[x[2]] = list_temp
            map_temp[x[0]] = map_temp2
            map_transition[x[0]][x[1]][x[2]] = list_temp
        else:
            map_temp2[x[2]] = list_temp
            map_transition[x[0]][x[1]] = map_temp2
        #map_transition[x[0]]
    else:
        map_temp2[x[2]] = list_temp
        map_temp[x[1]] = map_temp2
        map_transition[x[0]] = map_temp
    # json_string = json.dumps(map_transition, indent=4)
    # print(json_string)
    # print("-----------------------------------------------")

print(map_transition)

# start the PDA
isi_stack = ['Z']
currentState = 'Q'

print("--------------------------------------")
ans.append('e')
print(ans)

def travRec(currentState, isi_stack, ans, count):
    global map_transition
    print(currentState, isi_stack, ans)
    # basis
    if (currentState == 'F' and not ans):
        return True, 0
    if (currentState == 'F' and ans):
        return False, 0
    if (not ans and currentState != 'F'):
        return False, 0

    # kalau inputan ga ada di map kita --> invalid

    #cek currentState
    temp = map_transition[currentState]
    #print('ini temp',temp)

    # cek input
    lmao = temp.get(ans[0])
    print("lmao:", lmao)

    if (lmao == None):
        return False, count
    
    # cek top stack
    lmao2 = lmao.get(isi_stack[0])
    print("lmao-2:", lmao2)
    
    if (lmao2 == None):
        lmao2 = lmao.get('e')
        if(lmao2 == None):
            return False, count
    print("--------------------", currentState, ans[0], isi_stack[0]) 
    print('ini lmao:',lmao)
    print('ini lmao2:',lmao2)
    for elements in lmao2:
        print(elements)
        if (lmao2[-1] == 'e'):
            isi_stack.pop(0)
        elif (',' in lmao2[-1]):
            print("push stack")
            isi_stack.insert(0, ans[0])
        currentState = lmao2[0]
        ans.pop(0)
        count += 1

        x, count = travRec(currentState, isi_stack, ans, count)
        print(currentState, isi_stack, ans)
        print(x)
        return x, count

if __name__ == "__main__":
    hahahihi, loc = travRec(currentState, isi_stack, ans, 0)
    print(loc)
    if (hahahihi):
        print(Fore.GREEN + str(hahahihi) + Style.RESET_ALL)
    else:
        key_list = list(map_val.keys())
        val_list = list(map_val.values())

        # print key with val 100
        print(arr_temp[loc])
        #position = val_list.index(arr_temp[loc])
        #print(position)
        #ash = key_list[position]
        #ash = list(ash)
        #ash.insert(1, '/')
        #ash = ''.join(ash)
        #print(key_list[position])

        #print(Fore.RED + str(hahahihi) + Style.RESET_ALL)
        #print(loc)
        #print(arr_temp)
        #printError(key_list[position], 1)
        #printError(ash, 1)
        
        printError(arr_temp[loc], 1)
        printError(isi_stack[0], 1)
        exit()
        

#for inp in ans:
#    temp = map_transition[currentState]
#    lmao = temp.get(isi_stack[0])
#    print(lmao)
#    if (lmao[-1] == 'e'):
#        isi_stack.pop(0)
#    else:
#        isi_stack.insert(0, inp)
#    currentState = lmao[1]
#    
#    print('current state:', currentState)
#    print('curr stack: ', isi_stack)
#    print()
