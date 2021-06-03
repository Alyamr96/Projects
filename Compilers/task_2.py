import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)
   
output_file = open("task_2_result.txt", "w+")

Input = ""
States = []
Alphabets = []
StartState = []
EndStates = []
TransitionStates = []
#StateCounter = 0
CounterList = ["0"]
#Operations = []
with open(args.file, "r") as file:
    for line in file:
     data = line.strip()
     Input = data

#print(StringInput)

def Concatenation(StringInput):
    counter = int(CounterList.pop())
    i = 0
    NewStartState = "q" + str(counter)
    StartState.append(NewStartState)
    States.append(NewStartState)
    #counter = 0
    while i < len(StringInput):
        if StringInput[i].isalpha() or "ε" or StringInput[i].isdigit():
            #counter = int(CounterList.pop())
            counter += 1
            state = "q" + str(counter)
            if StringInput[i] == "ε":
                if "ε" not in Alphabets:
                 Alphabets.append(" ")
                TransitionStates.append(States[len(States)-1] + "," + " " + "," + " " + state)  
            else:
                if StringInput[i] not in Alphabets:
                 Alphabets.append(StringInput[i])
                TransitionStates.append(States[len(States)-1] + "," + " " + StringInput[i] + "," + " " + state) 
        States.append(state)
        i += 1
    EndStates.append(States[len(States)-1])
    CounterList.append(counter+1)
    '''print(States)
    print(Alphabets)
    print(StartState)
    print(EndStates)
    print(TransitionStates)'''    

def ORING(String1, String2):
    Concatenation(String1)
    String1StartState = StartState.pop()
    String1FinalState = EndStates.pop() 
    Concatenation(String2)
    String2StartState = StartState.pop()
    String2FinalState = EndStates.pop()
    
    counter = CounterList.pop()
    NewStartState = "q" + str(counter)
    counter += 1
    TransitionStates.append(NewStartState + "," + " " + "," + " " + String1StartState)
    TransitionStates.append(NewStartState + "," + " " + "," + " " + String2StartState)
    StartState.append(NewStartState)
    States.append(NewStartState)
    NewEndState = "q" + str(counter)
    counter += 1
    CounterList.append(counter)
    TransitionStates.append(String1FinalState + "," + " " + "," + " " + NewEndState)
    TransitionStates.append(String2FinalState + "," + " " + "," + " " + NewEndState)
    EndStates.append(NewEndState)
    States.append(NewEndState)

    '''print(States)
    print(Alphabets)
    print(StartState)
    print(EndStates)
    print(TransitionStates)
    print(CounterList)'''

def KleeneStarClosure(StartState1, EndState1):
    counter = int(CounterList.pop())
    NewStartState = "q" + str(counter)
    counter += 1
    NewEndState = "q" + str(counter)
    counter += 1
    CounterList.append(counter)
    StartState.append(NewStartState)
    EndStates.append(NewEndState)
    States.append(NewStartState)
    States.append(NewEndState)
    TransitionStates.append(NewStartState + "," + " " + "," + " " + StartState1)
    TransitionStates.append(NewStartState + "," + " " + "," + " " + NewEndState)
    TransitionStates.append(EndState1 + "," + " " + "," + " " + StartState1)
    TransitionStates.append(EndState1 + "," + " " + "," + " " + NewEndState)
    if " " not in Alphabets:
        Alphabets.append(" ")

def Concat(symbol):
    counter = int(CounterList.pop())
    if counter == 0:
        NewStartState = "q" + str(counter)
        counter += 1
        NewEndState = "q" + str(counter)
        counter += 1
        CounterList.append(counter)
        States.append(NewStartState)
        States.append(NewEndState)
        StartState.append(NewStartState)
        EndStates.append(NewEndState)
        if symbol == "ε":
            Alphabets.append(" ")
            TransitionStates.append(NewStartState + "," + " " + "," + " " + NewEndState)
        elif symbol.isdigit() or symbol.isalpha():
            Alphabets.append(symbol)
            TransitionStates.append(NewStartState + "," + " " + symbol + "," + " " + NewEndState)
    else:
        FormerEndState = EndStates.pop()
        NewEndState = "q" + str(counter)
        counter += 1
        CounterList.append(counter)
        States.append(NewEndState)
        if symbol not in Alphabets:
            Alphabets.append(symbol)
        EndStates.append(NewEndState)
        TransitionStates.append(FormerEndState + "," + " " + symbol + "," + " " + NewEndState)
            
def ORINGSTATES(StartStateString1, StartStateString2, FinalStateString1, FinalStateString2):
    counter = CounterList.pop()
    NewStartState = "q" + str(counter)
    counter += 1
    TransitionStates.append(NewStartState + "," + " " + "," + " " + StartStateString1)
    TransitionStates.append(NewStartState + "," + " " + "," + " " + StartStateString2)
    StartState.append(NewStartState)
    States.append(NewStartState)
    NewEndState = "q" + str(counter)
    counter += 1
    CounterList.append(counter)
    TransitionStates.append(FinalStateString1 + "," + " " + "," + " " + NewEndState)
    TransitionStates.append(FinalStateString2 + "," + " " + "," + " " + NewEndState)
    EndStates.append(NewEndState)
    States.append(NewEndState)

def PlusClosure(StartState1, EndState1):
    counter = int(CounterList.pop())
    NewStartState = "q" + str(counter)
    counter += 1
    NewEndState = "q" + str(counter)
    counter += 1
    CounterList.append(counter)
    StartState.append(NewStartState)
    EndStates.append(NewEndState)
    States.append(NewStartState)
    States.append(NewEndState)
    TransitionStates.append(NewStartState + "," + " " + "," + " " + StartState1)
    #TransitionStates.append(NewStartState + "," + " " + "," + " " + NewEndState)
    TransitionStates.append(EndState1 + "," + " " + "," + " " + StartState1)
    TransitionStates.append(EndState1 + "," + " " + "," + " " + NewEndState)
    if " " not in Alphabets:
        Alphabets.append(" ")

def QuestionMark(symbol):
    Concat(symbol)
    FormerStartState = StartState.pop()
    FormerEndState = EndStates.pop()
    counter = int(CounterList.pop())
    epsilonStartState = "q" + str(counter)
    counter += 1
    epsilonEndState = "q" + str(counter)
    counter += 1
    States.append(epsilonStartState)
    States.append(epsilonEndState)
    if " " not in Alphabets:
        Alphabets.append(" ")
    TransitionStates.append(epsilonStartState + "," + " " + "," + " " + epsilonEndState)
    FinalStartState = "q" + str(counter)
    counter += 1
    FinalEndState = "q" + str(counter)
    counter += 1
    CounterList.append(counter)
    States.append(FinalStartState)
    States.append(FinalEndState)
    StartState.append(FinalStartState)
    EndStates.append(FinalEndState)
    TransitionStates.append(FinalStartState + "," + " " + "," + " " + FormerStartState)    
    TransitionStates.append(FinalStartState + "," + " " + "," + " " + epsilonStartState)
    TransitionStates.append(FormerEndState + "," + " " + "," + " " + FinalEndState)
    TransitionStates.append(epsilonEndState + "," + " " + "," + " " + FinalEndState)

def ConvertToNfa(RegularExpression1):
    Operations = []
    RegularExpression = RegularExpression1
    RegularExpression = RegularExpression.replace(" ", "")
    RegularExpression = RegularExpression.replace("(", " ")    
    RegularExpression = RegularExpression.replace(")", " ")
    Operations = RegularExpression.split(" ")
    
    i = 0
    while i < len(Operations):
        if len(RegularExpression1) == 0:
            States.append("q0")
            States.append("q1")
            Alphabets.append(" ")
            StartState.append("q0")
            EndStates.append("q1")
            TransitionStates.append("q0" + "," + " " + "," + " " + "q1")
        if "|" in Operations[i] and "*" not in Operations[i]:
            substring1 = Operations[i].split("|")[0]
            substring2 = Operations[i].split("|")[1]
            ORING(substring1, substring2)
        if "|" in Operations[i] and "*" in Operations[i]:
            substring1 = Operations[i].split("|")[0]
            substring2 = Operations[i].split("|")[1]
            StartStateString1 = ""
            FinalStateString1 = ""
            StartStateString2 = ""
            FinalStateString2 = ""
            if "*" in substring1:
                subSub = substring1.split("*")[0]
                Concatenation(subSub)
                KleeneStarClosure(StartState.pop(), EndStates.pop())
                StartStateString1 = StartState.pop()
                FinalStateString1 = EndStates.pop()
            else:
                Concatenation(subSub)
                StartStateString1 = StartState.pop()
                FinalStateString1 = EndStates.pop()
            if "*" in substring2:
                subSub = substring2.split("*")[0]
                Concatenation(subSub)
                KleeneStarClosure(StartState.pop(), EndStates.pop())
                StartStateString2 = StartState.pop()
                FinalStateString2 = EndStates.pop()
            else:
                Concatenation(subSub)
                StartStateString2 = StartState.pop()
                FinalStateString2 = EndStates.pop()
            ORINGSTATES(StartStateString1, StartStateString2, FinalStateString1, FinalStateString2)
            
            j = i+1
            while j < len(Operations):
                if Operations[j] == "*":
                    FormerStartState = StartState.pop()
                    FormerEndState = EndStates.pop()
                    KleeneStarClosure(FormerStartState, FormerEndState)
                j += 1    
            #print(StartState)
            #print(EndStates)
            #print(TransitionStates)
            break        
                
        if "|" not in Operations[i]:
            if "*" not in Operations[i]:
                if "+" not in Operations[i]:
                    if "?" not in Operations[i]:
                        
                        j = 0
                        WorkWith = Operations[i]
                        while j < len(WorkWith):
                         Concat(WorkWith[j])
                         j +=1
        if Operations[i] == "*":
            KleeneStarClosure(StartState.pop(), EndStates.pop())
        if "*" in Operations[i] and Operations[i] != "*":
            substring = Operations[i].split("*")[0]
            Concatenation(substring)
            KleeneStarClosure(StartState.pop(), EndStates.pop())            
        if Operations[i] == "+":
            PlusClosure(StartState.pop(), EndStates.pop())
        if "+" in Operations[i] and Operations[i] != "+":
            substring = Operations[i].split("+")[0]
            print(substring)
            Concatenation(substring)
            PlusClosure(StartState.pop(), EndStates.pop())
        if "?" in Operations[i]:
            subChar = Operations[i].split("?")[0]
            QuestionMark(subChar)
        i += 1    

    print(Operations)


'''if "|" in Operations[i]:
            substring1 = Operations[i].split("|")[0]
            substring2 = Operations[i].split("|")[1]
            ORING(substring1, substring2)
         if "|" not in Operations[i]:
            if "*" not in Operations[i]:
                j = 0
                WorkWith = Operations[i]
                while j < len(WorkWith):
                    Concat(WorkWith[j])
                    j +=1
         if "∗" in Operations[i]:
            print("true")'''

#Concat("a")
#Concat("b")
#ORING("ε", "a")
#Concat("")
#Concatenation("b")
#ConvertToNfa(Input)
#Concatenation("ε")
#ORING("ab", "abcd")
#KleeneStarClosure(StartState.pop(), EndStates.pop())
#Concatenation(Input, 0)
#QuestionMark("b")
ConvertToNfa(Input)
#print(Operations)
print(States)
print(Alphabets)
print(StartState)
print(EndStates)
print(TransitionStates)
print(int(CounterList.pop())) 

i = 0
j = 0
i1= 0
i2= 0
i3= 0
while i < len(States)-1:
    output_file.write("%s, " % States[i])
    i += 1
output_file.write(States[len(States)-1] + '\n')

while i1 < len(Alphabets)-1:
    output_file.write("%s, " % Alphabets[i1])
    i1 += 1
output_file.write(Alphabets[len(Alphabets)-1] + '\n')

while i2 < len(StartState)-1:
    output_file.write("%s, " % StartState[i2])
    i2 += 1
output_file.write(StartState[len(StartState)-1] + '\n')

while i3 < len(EndStates)-1:
    output_file.write("%s, " % EndStates[i3])
    i3 += 1
output_file.write(EndStates[len(EndStates)-1] + '\n')
    
while j < len(TransitionStates)-1: 
    output_file.write("%s," % {TransitionStates[j]})
    j += 1 
output_file.write("%s" % {TransitionStates[len(TransitionStates)-1]})    