#************************************************************
# Created by Dipansh Arora
#************************************************************

true_atoms = []
rules_simplified = []

# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def run():
    while 1:

        user_input = input("kb>")
        user_input_list = user_input.split()

        if user_input_list[0]=="load":
            if(len(user_input_list)==2):
                try:
                    load_file(user_input_list[1])
                except:
                    print('"',user_input_list[1],'"',"File not found")
                    continue
            else:
                print("Enter a valid command")
                continue

        elif user_input_list[0]=="tell":
            if(len(user_input_list)<2):
                print("Error: tell needs at least one atom")
                continue
            tell_command(user_input_list)

        elif user_input_list[0]=="infer_all":
            if(len(user_input_list)>1):
                print("Enter a valid command")
                continue
            else:
                infer_all()

        else:
            print('"',user_input,'"',"is not a valid command")

    return

def valid_input_tell(user_input_list):

    for x in range(len(user_input_list)):
        if(is_atom(user_input_list[x])==False):
            print("Error",'"',user_input_list[x],'"',"is not a valid atom")
            return False
    return True

def valid_input_load(lines):
    for x in range(len(lines)):
        words = lines[x].split()
        for y in range(len(words)):
            
            if(y==0 or y%2==0):
                if(is_atom(words[y])==False):
                    return False
            elif y==1:
                   if(words[y]!="<--"):
                        return False
            else:
                   if(words[y]!='&'):
                        return False        
    return True

def load_file(filename):
    lines= []
    with open(filename) as fn:
        line = fn.readline()
        cnt = 1
        while line:
            if line == "\n":
                line = fn.readline()
                continue
            lines.append(line)
            line = fn.readline()
            cnt += 1     

        if valid_input_load(lines):
            true_atoms.clear()            #reset the true_atoms list
            rules_simplified.clear()      #reset rules_simplified list
            count=0
            for x in range(len(lines)):
                print("Rule",x+1,":",lines[x])
                count+=1
            print(count,"rules added\n")
            
            for x in range(len(lines)):
                words = lines[x].split()
                temp_str=""
                for y in range(len(words)):
                    if y==0 or y%2==0:
                        temp_str=temp_str+" "+words[y]
                
                rules_simplified.append(temp_str)

        else:
            print('"',filename,'"',"is not a valid knowledge base")
    return
    
def tell_command(user_input_list):
    if valid_input_tell(user_input_list)== False:
        return
    
    for x in range (1,len(user_input_list)):
        
        if user_input_list[x] in true_atoms:
            print('"',user_input_list[x],'"',"is already known to be true\n")
            continue
        true_atoms.append(user_input_list[x])
        print('"',user_input_list[x],'"',"added to kb\n")

    return

def infer_all():
    old_truth = true_atoms.copy()    
    new_infers=[]
    
    for x in range(len(rules_simplified)):
        temp = rules_simplified[x].split()
        
        for y in range(1,len(temp)):
            if temp[y] in true_atoms:
                if y==len(temp)-1:
                    if temp[0] in true_atoms:
                        continue
                    true_atoms.append(temp[0])
                    new_infers.append(temp[0])
                continue
            else:
                break
                
    if len(new_infers)>0:
        print("Newly inferred items :",new_infers,"\n")
    else:
        print("No new infers\n")
              
    print("Already known truth :",old_truth,"\n") 
    return

run()