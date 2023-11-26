import re
import json
from colorama import Fore, Back, Style

filename = "index.html"

f = open(filename, "r")

s = f.read()
tags = re.findall(r'[^\n\t]+', s)
print(tags)
print()
tags_real = []
for lmao in tags:
    # print("-----------------------------------------------")
    # print(lmao)
    tags = re.findall(r'<[^>]+>', lmao) 
    tags2 = re.findall(r'</\w+>\s*(.*)', lmao)
    tags3 = []
    if(tags2 != []):
        tags3 = re.findall(r'\s*(.*)<\w+>', tags2[0])
    tags4 = re.findall(r'(.*)<\w+>', lmao)
    

    tags2 = [x for x in tags2 if '<' not in x or '>' not in x]
    tags3 = [x for x in tags3 if '<' not in x or '>' not in x]
    tags4 = [x for x in tags4 if '<' not in x or '>' not in x]
    # if
    # print("2----", tags2) 
    # print(tags3)
    # print("4----", tags4)
    if tags == []:
        tags_real.append(lmao)
    else:
        tags_real.extend(tags4)
        if(len(tags2) == 0 or tags2[0] == ''):
            tags_real.extend(tags3)
        
        tags_real.extend(tags)
        if(not(len(tags2) == 0 or tags2[0] == '')):
            tags_real.extend(tags2)
        # print(tags_real)


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
    "<link>" : "lk",
    "</link>" : "lk",
    "<script>" : "s",
    "</script>" : "s",
    "<h1>" : "h1",
    "</h1>" : "h1",
    "<h2>" : "h2",
    "</h2>" : "h2",
    "<h3>" : "h3",
    "</h3>" : "h3",
    "<h4>" : "h4",
    "</h4>" : "h4",
    "<h5>" : "h5",
    "</h5>" : "h5",
    "<h6>" : "h6",
    "</h6>" : "h6",
    "<p>" : "p",
    "</p>" : "p",
    "<br>" : "br",
    "<em>" : "em",
    "</em>" : "em",
    "<b>" : "b",
    "</b" : "b",
    "<abbr>": "ab",
    "</abbr>": "ab",
    "<strong>" : "str",
    "</strong>" : "str",
    "<small>" : "sm",
    "</small>" : "sm",
    "<hr>" : "hr",
    "<a>" : "a",
    "</a>" : "a",
    "<button>" : "bt",
    "</button>" : "bt",
    "<form>" : "f",
    "</form>" : "f",
    "<input>" : "in",
    "<table>" : "tbl",
    "</table>" : "tbl",
    "<tr>" : "tr",
    "</tr>" : "tr",
    "<td>" : "td",
    "</td>" : "td",
    "<th>" : "th",
    "</th>" : "th",
    "<img>" : "img",
    "<div>" : "dv",
    "</div>" : "dv",
    "<illegalStr>" : "ill",
    "id=\"" : "id",
    "class=\"": "cl",
    "style=\"": "sl",
    "src=\"": "sc",
    "\"": "petik",
    'rel=\"' : "re",
    'href=\"' : "hf",
    'alt=\"' : "at",
    'type=\"submit' : "tb",
    'type=\"reset' : "tb",
    'type=\"button' : "tb",
    'type=\"text' : "ti",
    'type=\"password' : "ti",
    'type=\"email' : "ti",
    'type=\"number' : "ti",
    'type=\"checkbox' : "ti",
    'action=\"' : "an",
    'method=\"GET' : "md",
    'method=\"POST' : "md",
    'src=\"' : "sc",
    '<!--' : "comment",
    '-->' : "comment",
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

def printCorrent():
    
    # print err message
    
    print(Fore.GREEN + "+" + "-"*14 + "+")
    print("| " + " " * 3+ "CORRECT" +"   |")
    print("+" + "-"*14 + "+")
    #print("-" * (pos) + "↑")
    print("Syntax Checked" + Style.RESET_ALL)
        

# def validateGlob(search, glob_idStr):

#     result = [m.start() for m in re.finditer('(?=%s)(?!.{1,%d}%s)' % (search, len(search)-1, search), glob_idStr)]
#     print(glob_idStr)
#     print(result)
    
    # isEqual = False
    # for x in result:
    #     isEqual = False
    #     char_temp = ""
    #     haha = 0
    #     state = False
    #     for i in range(x, len(glob_idStr)):
    #         if glob_idStr[i] == '=':
    #             if(search != char_temp):
    #                 print(search, char_temp)
    #                 return False
    #             else:
    #                 char_temp = ""
    #                 isEqual = True
    #                 continue
    #         elif glob_idStr[i] == '"':
    #             haha+=1
    #         else:
    #             char_temp += glob_idStr[i]
            
    #         if haha == 2:
    #             state = True
    #             break
    #         #print(glob_idStr[i])
    #     if not state:
    #         return False
    #     #print(char_temp, haha, state)
    # if (result == [] or result == None):
    #     return True

    # return True and isEqual


# ini TOKENIZER
ans = []

for x in tags:
    temp = x[1:-1]
    temp = temp.split(' ')
    # print(temp)

    if(x[0:4] == '<!--'):
        ans.append('comment')
        if(x[-3:] == '-->'):
            ans.append('comment')
            continue
        else:
            ans.append(map_val['<illegalStr>'])
            continue
    # print(x[0:4], x[-3:])

    # add ans
    x = '<' + temp[0] + '>'
    if x in map_val:
        ans.append(map_val[x])
    else:
        ans.append(map_val['<illegalStr>'])

    # cek global aatrbute
    combined_right = ''.join(temp[1:])
    print(combined_right)
    if(combined_right != ''):
        anso = []
        ch_temp = ''
        count = 0
        for x in combined_right:
            if(x == '"'):
                count += 1
            if(count == 2):
                anso.append(ch_temp)
                ch_temp = ''
                count = 0
                anso.append('"')
            else:
                ch_temp += x
        if(ch_temp != ''):
            anso.append(ch_temp)

        print(anso)

        # print(ans)
        for lmao in anso:
            if('method' in lmao or 'type' in lmao):
                if(lmao in map_val):
                    ans.append(map_val[lmao])
                else:
                    ans.append(map_val['<illegalStr>'])
            elif(lmao != '"'):
                temp_lmao = lmao.split("\"")
                temp_lmao = temp_lmao[0] + "\""
                if(temp_lmao in map_val):
                    ans.append(map_val[temp_lmao])
                else:
                    ans.append(map_val['<illegalStr>'])
            elif(lmao == '"'):
                if(lmao in map_val):
                    ans.append(map_val[lmao])

        # temp2 = combined_right.split('"')
        # print(temp2)
        
            
        print("-----")
        # check illegal string
        # if('<'+temp[0]+'>' not in map_val and x[0] != '<'):
        #     temp = ['illegalStr']
        # # check wrong tag name
        # if('<'+temp[0]+'>' not in map_val):
        #     print('FAILED awikwok')
        #     printError(x, 1)
        #     exit()
        
        # # check global identifier
        # glob_id = ''.join(temp[1:])
        # if glob_id != '':
        #     xId = validateGlob('id', glob_id)
        #     xClass = validateGlob('class', glob_id)
        #     xStyle = validateGlob('style', glob_id)

        #     print(xId, xClass, xStyle)
        #     if(not(xId and xClass and xStyle)):
        #         print('Failed awikwok')
        #         printError(x, 1)
        #         exit()

        # # add to ans
        # #print(temp)

print(ans)
exit()
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
        print("n element:", elements)
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
        printCorrent()
        # print(Fore.GREEN + str(hahahihi) + Style.RESET_ALL)
    else:
        key_list = list(map_val.keys())
        val_list = list(map_val.values())

        # print key with val 100
        # print(arr_temp[loc])
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
        
        # printError(arr_temp[loc], 1)
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
