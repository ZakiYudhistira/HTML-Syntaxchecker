from colorama import Fore, Style
import re
import argparse

class App:
    # init class
    def __init__(self):
        self.map_val = {
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

        self.tags_real = []
        self.tags = []

        self.htmlfile = ''
        self.pdafile = ''

        self.arr_temp = []

        self.ans = []
        self.map_transition = {}

        self.isi_stack = ['Z']
        self.currentState = 'Q'

        self.loadFiles()
        self.html_parser(self.htmlfile)

        self.tags = map(lambda x: x.strip('\n').strip('\t'), self.tags_real)
        self.tags = list(filter(None, self.tags))
        print(self.tags)

        self.arr_temp.extend(self.tags)

        self.tokenizer()

        exit()
        self.parsePDA(self.pdafile)
        self.ans.append('e')

        hahahihi, loc = self.travRec(self.currentState, self.isi_stack, self.ans, 0)
        print(loc)
        if (hahahihi):
            self.printCorrent()
            # print(Fore.GREEN + str(hahahihi) + Style.RESET_ALL)
        else:
            key_list = list(self.map_val.keys())
            val_list = list(self.map_val.values())
        
        self.printError(self.isi_stack[0], 1)
        exit()
    
    def travRec(self, currentState, isi_stack, ans, count):
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
        temp = self.map_transition[currentState]
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

            x, count = self.travRec(currentState, isi_stack, ans, count)
            print(currentState, isi_stack, ans)
            print(x)
            return x, count

    def parsePDA(self, rules):
        rules = open(rules, 'r')
        for line in rules:
            # print(line)
            map_temp = {}
            map_temp2 = {}
            list_temp = []
            
            line = line.strip('\n')
            x = line.split(' ')
            #list_temp.append(x[1])
            list_temp.append(x[3])
            list_temp.append(x[4])
            
            if(x[0] in self.map_transition):
                if(x[1] in self.map_transition[x[0]]):
                    map_temp2[x[2]] = list_temp
                    map_temp[x[0]] = map_temp2
                    self.map_transition[x[0]][x[1]][x[2]] = list_temp
                else:
                    map_temp2[x[2]] = list_temp
                    self.map_transition[x[0]][x[1]] = map_temp2
                #map_transition[x[0]]
            else:
                map_temp2[x[2]] = list_temp
                map_temp[x[1]] = map_temp2
                self.map_transition[x[0]] = map_temp
            # json_string = json.dumps(map_transition, indent=4)
            # print(json_string)
            # print("-----------------------------------------------")

        print(self.map_transition)
        rules.close()
    
    def tokenizer(self):
        for x in self.tags:
            temp = x[1:-1]
            temp = temp.split(' ')
            # print(temp)

            if(x[0:4] == '<!--'):
                self.ans.append('comment')
                if(x[-3:] == '-->'):
                    self.ans.append('comment')
                    continue
                else:
                    self.ans.append(self.map_val['<illegalStr>'])
                    continue
            # add ans
            x = '<' + temp[0] + '>'
            if x in self.map_val:
                self.ans.append(self.map_val[x])
            else:
                self.ans.append(self.map_val['<illegalStr>'])
                continue

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
                        if(lmao in self.map_val):
                            self.ans.append(self.map_val[lmao])
                        else:
                            self.ans.append(self.map_val['<illegalStr>'])
                    elif(lmao != '"'):
                        temp_lmao = lmao.split("\"")
                        temp_lmao = temp_lmao[0] + "\""
                        if(temp_lmao in self.map_val):
                            self.ans.append(self.map_val[temp_lmao])
                        else:
                            self.ans.append(self.map_val['<illegalStr>'])
                    elif(lmao == '"'):
                        if(lmao in self.map_val):
                            self.ans.append(self.map_val[lmao])

                print("-----")

        print(self.ans)

    def printError(self, x, pos):
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

    def printCorrent(self):
        # print err message
        print(Fore.GREEN + "+" + "-"*14 + "+")
        print("| " + " " * 3+ "CORRECT" +"   |")
        print("+" + "-"*14 + "+")
        #print("-" * (pos) + "↑")
        print("Syntax Checked" + Style.RESET_ALL)

    def html_parser(self, htmlfile):
        f = open(htmlfile, "r")
        s = f.read()
        tags = re.findall(r'[^\n\t]+', s)
        print(tags)
        print()
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
                self.tags_real.append(lmao)
            else:
                self.tags_real.extend(tags4)
                if(len(tags2) == 0 or tags2[0] == ''):
                    self.tags_real.extend(tags3)
                
                self.tags_real.extend(tags)
                if(not(len(tags2) == 0 or tags2[0] == '')):
                    self.tags_real.extend(tags2)
            # print(self.tags_real)
        
    
    def loadFiles(self):
        parser = argparse.ArgumentParser(description='HTML syntax checker')
        parser.add_argument('pda_file', help='Path to the pda.txt')
        parser.add_argument('html_file', help='Path to the .html file')
        args = parser.parse_args()

        self.pdafile = args.pda_file
        self.htmlfile = args.html_file
        
        print(self.pdafile)
        print(self.htmlfile)

App()