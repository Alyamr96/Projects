import queue

'''states_list = ["q0", "q1"]
alphabet_list = ["a"]
start_state_list = ["q0"]
end_states_list = ["q1"]
transition_list = ["q0, a, q1"]'''

'''states_list = ["q0", "q1", "q3"]
alphabet_list = ["a", "b"]
start_state_list = ["q0"]
end_states_list = ["q3"]
transition_list = ["q0, a, q1", "q1, b, q3"]'''

'''states_list = ["q0", "q1", "q2", "q3", "q4", "q5"]
alphabet_list = ["a", "b"]
start_state_list = ["q4"]
end_states_list = ["q5"]
transition_list = ["q0, a, q1", "q2, b, q3", "q4, , q0", "q4, , q2", "q1, , q5", "q3, , q5"]'''

'''states_list = ["q0", "q1", "q2", "q3", "q4"]
alphabet_list = ["a"]
start_state_list = ["q2"]
end_states_list = ["q3"]
transition_list = ["q0, a, q1", "q1, , q0", "q2, , q0", "q2, , q3", "q1, , q3"]'''

'''states_list = ["q0", "q1", "q2", "q3", "q4", "q5"]
alphabet_list = [" ","a"]
start_state_list = ["q4"]
end_states_list = ["q5"]
transition_list = ["q0, a, q1", "q2, , q3", "q4, , q0", "q4, a, q2", "q1, , q5", "q3, , q5"]'''

'''states_list = ["q0", "q1"]
alphabet_list = [" "]
start_state_list = ["q0"]
end_states_list = ["q1"]
transition_list = ["q0, , q1"]'''

'''states_list = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13"]
alphabet_list = ["a", "b", "c"]
start_state_list = ["q12"]
end_states_list = ["q13"]
transition_list = ["q0, a, q1", "q2, b, q3", "q4, , q0", "q4, , q2", "q1, , q5", "q3, , q5", "q6, c, q7", "q5, , q6", "q5, , q9", "q7, , q11", "q9, , q10", "q10, , q11", "q12, , q13", "q12, , q4", "q11, , q4", "q11, , q13"]
'''

states_list = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
alphabet_list = [" ", "s", "t"]
start_state_list = ["q0"]
end_states_list = ["q8"]
transition_list = ["q0, , q8", "q0, , q1", "q1, , q2", "q1, , q4", "q2, s, q3", "q3, , q7", "q4, , q5", "q5, t, q6", "q6, , q7", "q7, , q1", "q7, , q8"]

output_file = open("task_2_2_results.txt", "w+")
NFA_StatesListDuplicates = []
NFA_StatesList = []

DFA_Alphabet_list = []
for element in alphabet_list:
    if element != " ":
        DFA_Alphabet_list.append(element)
DFA_Final_states_list = []
DFA_Start_states_list = []
DFA_Transitions_list = []

def epsilon_closure(list1, list2):
    list1String = ','.join(list1)
    i = 0
    j = 0
    while i < len(list1String):
        while j < len(list2):
            WholeString = list2[j]
            FirstStateInTransition = WholeString.split(",")[0]
            alphabet_symbol = WholeString.split(",")[1]
            SecondStateInTransition = WholeString.split(",")[2]
            if list1String[i:i+2] in FirstStateInTransition and alphabet_symbol == " ":
                list1String = list1String + "," +  SecondStateInTransition
            j += 1
        j = 0
        i += 1
    NFA_StatesListDuplicates.append(list1String.replace(" ", ""))
    for element in NFA_StatesListDuplicates:
        if element not in NFA_StatesList:
            NFA_StatesList.append(element)
    print(list1String)
    list1Checker = 0
    while list1Checker < len(list1String):
        if list1String[list1Checker:list1Checker+2] == end_states_list[0]:
            DFA_Final_states_list.append(list1String.replace(" ", ""))
        if list1String[list1Checker:list1Checker+2] == start_state_list[0]:
            DFA_Start_states_list.append(list1String.replace(" ", ""))    
        list1Checker += 1

def SymbolTransition(inputString, inputChar):
    SymbolTransitionList = []
    i = 0
    j = 0
    while i < len(inputString):
        while j < len(transition_list):
            WholeString = transition_list[j]
            FirstStateInTransition = WholeString.split(",")[0]
            alphabet_symbol = WholeString.split(",")[1]
            SecondStateInTransition = WholeString.split(",")[2]
            if inputString[i:i+2] in FirstStateInTransition and inputChar in alphabet_symbol:
                SymbolTransitionList.append(SecondStateInTransition)
            j += 1
        j = 0
        i += 1
    print(SymbolTransitionList)
    epsilon_closure(list(dict.fromkeys(SymbolTransitionList)), transition_list)    

def ConvertNfaToDfa():
    '''epsilon_closure(start_state_list, transition_list)
    SymbolTransition(NFA_StatesList[0], "t")
    DFA_Transitions_list.append(NFA_StatesList[0] + " " + "," + " " + "t" + " " + "," + " " + NFA_StatesList[len(NFA_StatesList)-1])
    SymbolTransition(NFA_StatesList[0], "s")
    DFA_Transitions_list.append(NFA_StatesList[0] + " " + "," + " " + "s" + " " + "," + " " + NFA_StatesList[len(NFA_StatesList)-1])
    SymbolTransition("q3,q7,q1,q8,q2,q4,q5", "s")
    DFA_Transitions_list.append("q3,q7,q1,q8,q2,q4,q5" + " " + "," + " " + "s" + " " + "," + " " + NFA_StatesList[len(NFA_StatesList)-1])
    SymbolTransition("q6,q7,q1,q8,q2,q4,q5", "t")
    DFA_Transitions_list.append("q6,q7,q1,q8,q2,q4,q5" + " " + "," + " " + "t" + " " + "," + " " + NFA_StatesList[len(NFA_StatesList)-2])
    SymbolTransition("q6,q7,q1,q8,q2,q4,q5", "s")
    DFA_Transitions_list.append("q6,q7,q1,q8,q2,q4,q5" + " " + "," + " " + "s" + " " + "," + " " + NFA_StatesList[len(NFA_StatesList)-1])
    SymbolTransition("q3,q7,q1,q8,q2,q4,q5", "t")
    DFA_Transitions_list.append("q3,q7,q1,q8,q2,q4,q5" + " " + "," + " " + "t" + " " + "," + " " + NFA_StatesList[len(NFA_StatesList)-2])
    
    DFA_Final_states_list_Without_Duplicates = []
    for element in DFA_Final_states_list:
        if element not in DFA_Final_states_list_Without_Duplicates:
            DFA_Final_states_list_Without_Duplicates.append(element)'''

    epsilon_closure(start_state_list, transition_list)
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(NFA_StatesListDuplicates[0], element)
            DFA_Transitions_list.append(NFA_StatesListDuplicates[0] + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition(NFA_StatesListDuplicates[0], "t")
    #DFA_Transitions_list.append(NFA_StatesListDuplicates[0] + " " + "," + " " + "t" + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition(NFA_StatesListDuplicates[0], "s")
    #DFA_Transitions_list.append(NFA_StatesListDuplicates[0] + " " + "," + " " + "s" + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition("q3,q7,q1,q8,q2,q4,q5", "s")
    string1 = NFA_StatesListDuplicates[1]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string1, element)
            DFA_Transitions_list.append(string1 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition(string1, "s")
    #DFA_Transitions_list.append(string1 + " " + "," + " " + "s" + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition(string1, "t")
    #DFA_Transitions_list.append(string1 + " " + "," + " " + "t" + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1]) 

    string2 = NFA_StatesListDuplicates[2]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string2, element)
            DFA_Transitions_list.append(string2 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition(string2, "s")
    #DFA_Transitions_list.append(string2 + " " + "," + " " + "s" + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition(string2, "t")
    #DFA_Transitions_list.append(string2 + " " + "," + " " + "t" + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string3 = NFA_StatesListDuplicates[3]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string3, element)
            DFA_Transitions_list.append(string3 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition(string3, "s")
    #DFA_Transitions_list.append(string3 + " " + "," + " " + "s" + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    #SymbolTransition(string3, "t")
    #DFA_Transitions_list.append(string3 + " " + "," + " " + "t" + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])
    string4 = NFA_StatesListDuplicates[4]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string4, element)
            DFA_Transitions_list.append(string4 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string5 = NFA_StatesListDuplicates[5]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string5, element)
            DFA_Transitions_list.append(string5 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string6 = NFA_StatesListDuplicates[6]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string6, element)
            DFA_Transitions_list.append(string6 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])                      
    
    string7 = NFA_StatesListDuplicates[7]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string7, element)
            DFA_Transitions_list.append(string7 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string8 = NFA_StatesListDuplicates[8]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string8, element)
            DFA_Transitions_list.append(string8 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string9 = NFA_StatesListDuplicates[9]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string9, element)
            DFA_Transitions_list.append(string9 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string10 = NFA_StatesListDuplicates[10]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string10, element)
            DFA_Transitions_list.append(string10 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string11 = NFA_StatesListDuplicates[11]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string11, element)
            DFA_Transitions_list.append(string11 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string12 = NFA_StatesListDuplicates[12]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string12, element)
            DFA_Transitions_list.append(string12 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string13 = NFA_StatesListDuplicates[13]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string13, element)
            DFA_Transitions_list.append(string13 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string14 = NFA_StatesListDuplicates[14]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string14, element)
            DFA_Transitions_list.append(string14 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string15 = NFA_StatesListDuplicates[15]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string15, element)
            DFA_Transitions_list.append(string15 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string16 = NFA_StatesListDuplicates[16]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string16, element)
            DFA_Transitions_list.append(string16 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    '''string18 = NFA_StatesListDuplicates[18]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string18, element)
            DFA_Transitions_list.append(string18 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string19 = NFA_StatesListDuplicates[19]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string19, element)
            DFA_Transitions_list.append(string19 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])

    string20 = NFA_StatesListDuplicates[20]
    for element in alphabet_list:
        if element != " ":
            SymbolTransition(string20, element)
            DFA_Transitions_list.append(string20 + " " + "," + " " + element + " " + "," + " " + NFA_StatesListDuplicates[len(NFA_StatesListDuplicates)-1])'''

    DFA_Final_states_list_Without_Duplicates = []
    for element in DFA_Final_states_list:
        if element not in DFA_Final_states_list_Without_Duplicates:
            DFA_Final_states_list_Without_Duplicates.append(element)

    DFA_Transitions_list_Without_Duplicates = []
    for element in DFA_Transitions_list:
        if element not in DFA_Transitions_list_Without_Duplicates:
            DFA_Transitions_list_Without_Duplicates.append(element)        

    '''below are the test cases that prove that my functions epsilon_closure and SymbolTransition work perfectly:
    epsilon_closure(start_state_list, transition_list)
    SymbolTransition("q3,q7,q1,q8,q2,q4,q5", "s")
    SymbolTransition("q3,q7,q1,q8,q2,q4,q5", "t")
    SymbolTransition("q6,q7,q1,q8,q2,q4,q5", "s")
    SymbolTransition("q6,q7,q1,q8,q2,q4,q5", "t")
    SymbolTransition("q0,q8,q1,q2,q4,q5, "t")
    SymbolTransition("q0,q8,q1,q2,q4,q5, "s")'''

    print(DFA_Alphabet_list)
    print(NFA_StatesList)
    print(DFA_Final_states_list_Without_Duplicates)
    print(DFA_Start_states_list)
    print(DFA_Transitions_list_Without_Duplicates)

    i = 0
    j = 0
    i1= 0
    i2= 0
    i3= 0
    while i < len(NFA_StatesList)-1:
     output_file.write("{%s}, " % NFA_StatesList[i])
     i += 1
    output_file.write("{%s} " %NFA_StatesList[len(NFA_StatesList)-1] + '\n')

    while i1 < len(DFA_Alphabet_list)-1:
     output_file.write("%s, " % DFA_Alphabet_list[i1])
     i1 += 1
    output_file.write(DFA_Alphabet_list[len(DFA_Alphabet_list)-1] + '\n')

    while i2 < len(DFA_Start_states_list)-1:
     output_file.write("%s, " % DFA_Start_states_list[i2])
     i2 += 1
    output_file.write(DFA_Start_states_list[len(DFA_Start_states_list)-1] + '\n')

    while i3 < len(DFA_Final_states_list_Without_Duplicates)-1:
     output_file.write("{%s}, " % DFA_Final_states_list_Without_Duplicates[i3])
     i3 += 1
    output_file.write("{%s} " %DFA_Final_states_list_Without_Duplicates[len(DFA_Final_states_list_Without_Duplicates)-1] + '\n')
    
    while j < len(DFA_Transitions_list_Without_Duplicates): 
     output_file.write("{%s}," % DFA_Transitions_list_Without_Duplicates[j])
     j += 1
    
def ConvertZero():
    output_file.write("0" + '\n')
    output_file.write('\n')
    output_file.write("0" + '\n')
    output_file.write("0" + '\n')
    '''stating = []
    alphabeting = []
    startstating = []
    finalstating = []
    stating.append("0")
    alphabeting.append(" ")
    startstating.append("0")
    finalstating.append("0")
    i = 0
    j = 0
    i1= 0
    i2= 0
    i3= 0'''
    '''while i < len(stating)-1:
     output_file.write("{%s}, " % stating[i])
     i += 1'''
    #output_file.write("{%s} " %stating[0] + '\n')

    '''while i1 < len(DFA_Alphabet_list)-1:
     output_file.write("%s, " % DFA_Alphabet_list[i1])
     i1 += 1'''
    #output_file.write('''DFA_Alphabet_list[len(DFA_Alphabet_list)-1] +''' '\n')

    '''while i2 < len(DFA_Start_states_list)-1:
     output_file.write("%s, " % DFA_Start_states_list[i2])
     i2 += 1'''
    #output_file.write(startstating[0] + '\n')

    '''while i3 < len(DFA_Final_states_list_Without_Duplicates)-1:
     output_file.write("{%s}, " % DFA_Final_states_list_Without_Duplicates[i3])
     i3 += 1'''
    #output_file.write("{%s} " %finalstating[0] + '\n')
    
    '''while j < len(DFA_Transitions_list_Without_Duplicates): 
     output_file.write("{%s}," % DFA_Transitions_list_Without_Duplicates[j])
     j += 1'''


if len(alphabet_list) == 1 and alphabet_list[0] == "":
    ConvertZero()

else: 
 ConvertNfaToDfa()
