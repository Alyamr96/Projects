import argparse 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)

output_file = open("task_4_1_result.txt", "w+")

rules = []
FinalRules = []
FinalRulesOutput = []
FinalDashRulesOutput = []
with open(args.file, "r") as file:
    for line in file:
     data = line.strip()
     rules.append(data)

def CheckStrings(string1, string2):
    i = 0
    j = 0
    appendedString = string1
    data = string2.split("|")
    stringX = data[0]
    data1 = []
    index = 0
    while index < len(data[0]):
         if stringX[index] == ":":
             stringY = stringX[:index]
             stringZ = stringX[index+1:]
             data1.append(stringY)
             data1.append(stringZ)
             break
         index += 1
    jndex = 1
    while jndex < len(data):
         data1.append(data[jndex])
         jndex += 1
    #print(data1)
    while i < len(string1):
        if string1[i] == data1[0].replace(" ",""):
            RestOfString = string1[i+1:]
            RestOfWord = RestOfString.split('|')[0]
            appendedString = appendedString.replace(string1[i], data1[1])
            index2 = 2
            while index2 < len(data1):
                appendedString = appendedString + " " +"|" + " " + data1[index2] + " " + RestOfWord
                index2 += 1
        i += 1
    appendedString = appendedString.replace("  ", " ")
    FinalRules.append(appendedString)
    #print(appendedString)

def LeftRecursionElimination(string1):
    data = string1.split("|")
    stringX = data[0]
    data1 = []
    i = 0
    while i < len(data[0]):
        if stringX[i] == ":":
            stringY = stringX[:i]
            stringZ = stringX[i+1:]
            data1.append(stringY)
            data1.append(stringZ)
            break
        i += 1
    j = 1
    while j < len(data):
         data1.append(data[j])
         j += 1
    #print(data1)
    secondRule = data1[0].replace(" ", "") + "'" 
    secondRule2 = secondRule + " " + ":"
    #print(secondRule)
    index = 1
    VariableWithoutSpace = data1[0]
    VariableWithoutSpace = VariableWithoutSpace.replace(" ","")
    #print(VariableWithoutSpace)
    while index < len(data1):
        StringWithoutSpace = data1[index]
        StringWithoutSpace = StringWithoutSpace.replace(" ", "")
        #print(data1[len(data1)-1].replace(" ", ""))
        if VariableWithoutSpace == StringWithoutSpace[0]:
            #del data1[index]
            String2WithoutSpaces = StringWithoutSpace[1:]
            secondRule2 = secondRule2 + " " + ":" + String2WithoutSpaces.replace(""," ") + secondRule + "|"
        index += 1
    secondRule2 = secondRule2 + " " + " " +"epsilon"
    secondRule2 = secondRule2.replace(":", "")
    secondRule2 = secondRule2.replace("  ", " ")
    FirstSubSecondRule2 = secondRule2[:2] + ":" +  " "
    SecondSubSecondRule2 = secondRule2[4:]
    secondRule2 = FirstSubSecondRule2 + SecondSubSecondRule2
    #print(secondRule2)
    FinalRuleStart = data1[0].replace(" ","") + " " + ":"
    FinalRule = ""
    index2 = 1
    index3 = 0
    FinalData = []
    while index2 < len(data1):
        StringWithoutSpace = data1[index2]
        StringWithoutSpace = StringWithoutSpace.replace(" ", "")
        if VariableWithoutSpace != StringWithoutSpace[0]:
            FinalData.append(StringWithoutSpace.replace("", " "))
        index2 += 1       
    while index3 < len(FinalData):
        if index3 == len(FinalData)-1:
            FinalRule = FinalRule + FinalData[index3] + secondRule
        if index3 != len(FinalData)-1:    
            FinalRule = FinalRule + FinalData[index3] + secondRule + "|"
        index3 += 1
    FinalRule = FinalRuleStart + FinalRule
    #print(FinalRule)
    FinalRulesOutput.append(FinalRule)
    FinalDashRulesOutput.append(secondRule2)

def Main():
    i = 0
    j = 0
    i1 = 0
    i2 = 0
    while i < len(rules):
        while j < i:
            CheckStrings(rules[i], rules[j])
            j += 1
        j = 0
        #LeftRecursionElimination(rules[i])
        i += 1 
    #print(FinalRules)
    for element in FinalRules:
       LeftRecursionElimination(element)
    print(FinalRulesOutput)
    print(FinalDashRulesOutput)
    output_file.write("%s " % rules[0] + '\n')
    while i1 < len(FinalRulesOutput):
     output_file.write("%s" % FinalRulesOutput[i1] + '\n')
     i1 += 1
    while i2 < len(FinalDashRulesOutput):
     output_file.write("%s" % FinalDashRulesOutput[i2] + '\n')
     i2 += 1           

Main()
#LeftRecursionElimination("A : A a c | b d | b c | A b d | A b c | A a | b d a")
#CheckStrings(rules[1], rules[0]) 
'''def SplitRule(string1):
    data = string1.split("|")
    stringX = data[0]
    data1 = []
    i = 0
    while i < len(data[0]):
        if stringX[i] == ":":
            stringY = stringX[:i]
            stringZ = stringX[i+1:]
            data1.append(stringY)
            data1.append(stringZ)
            break
        i += 1
    j = 1
    while j < len(data):
         data1.append(data[j])
         j += 1
    print(data1)'''            