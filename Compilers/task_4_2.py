import argparse 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)

output_file = open("task_4_2_result.txt", "w+")

rules = []
finalDashedRules = []
finalDashedRulesNoDuplicates = []
finalOutputDashedRules = []
finalOutputNonDashedRules = []
#yarabFinal = []
#finalAppendedString = ""

with open(args.file, "r") as file:
    for line in file:
     data = line.strip()
     rules.append(data)
#print(rules) 

def LeftFactoring(list1):
    startSymbol = list1[0]
    finalnonDashedStartSymbol = startSymbol + " " + ":"
    FinalStartSymbol = startSymbol + "'" + " " + ":"
    FinalStartSymbol2 = startSymbol + "'" 
    FinalRuleDone = ""
    dashedList = []
    FinalList1 = []
    finalNonDashedRule = ""
    dashedListNoDuplicates = []
    dashedListNoDuplicates2 = []
    i = 1
    j = 1
    while i < len(list1):
        while j < len(list1):
            stringI = list1[i]
            stringJ = list1[j]
            if stringI[0] == stringJ[0] and i != j:
                #stringStart = stringI[0].upper() + "'" + ":"
                dashedList.append(stringI[1:])
                dashedList.append(stringJ[1:])
                list1[i] = stringI[0]+FinalStartSymbol2
                list1[j] = stringJ[0]+FinalStartSymbol2
                #stringStart = stringStart + stringI[1:] + "|" + stringJ[1:]
                #print(stringStart)
                #finalDashedRules.append(stringStart)
            j += 1
        j = 0    
        i += 1
    for element in dashedList:
     if element not in dashedListNoDuplicates and element != "":
         dashedListNoDuplicates.append(element)
    for element in dashedListNoDuplicates:
        if "'" not in element:
            dashedListNoDuplicates2.append(element)
    #print(dashedListNoDuplicates2)
    #print(FinalStartSymbol)
    index = 0
    while index < len(dashedListNoDuplicates2):
        if index == len(dashedListNoDuplicates2) -1 :
         FinalRuleDone += dashedListNoDuplicates2[index]
        else:
         FinalRuleDone += dashedListNoDuplicates2[index] + "|"
        index += 1 

    FinalRuleDone = FinalRuleDone.replace("", " ")
    FinalRuleDone = FinalStartSymbol + FinalRuleDone
    print(FinalRuleDone)
    finalOutputDashedRules.append(FinalRuleDone)
    for element in list1:
        if element not in FinalList1:
            FinalList1.append(element)
    index3 = 0
    while index3 < len(FinalList1):
        if index3 == len(FinalList1) -1 :
         finalNonDashedRule += FinalList1[index3]
        else:
         finalNonDashedRule += FinalList1[index3] + "|" 
        index3 += 1
    finalNonDashedRule = finalNonDashedRule.replace("", " ")
    finalNonDashedRule = finalnonDashedStartSymbol + finalNonDashedRule
    print(finalNonDashedRule)
    finalOutputNonDashedRules.append(finalNonDashedRule)     
    '''index = 0
    charChecker = ""
    while index < len(dashedListNoDuplicates):
        FirstString = dashedListNoDuplicates[index]
        char = FirstString[0]
        if char != charChecker:
            yarabFinal.append(item[0] == char for item in dashedListNoDuplicates)
            charChecker = char
        index += 1        
    print(yarabFinal)'''

i = 0
i1 = 0
i2 = 0
while i < len(rules):
    data = []
    appendedString = rules[i].replace(" ", "")
    #print(appendedString)
    data = appendedString.split("|")
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
    LeftFactoring(data1)
    i += 1
while i1 < len(finalOutputNonDashedRules):
     output_file.write("%s" % finalOutputNonDashedRules[i1] + '\n')
     i1 += 1
while i2 < len(finalOutputDashedRules):
     output_file.write("%s" % finalOutputDashedRules[i2] + '\n')
     i2 += 1    

#TestList = ["S", "S+S", "SS", "(S)", "S*", "ab", "aad"]
#LeftFactoring(TestList)        










