import argparse 

if __name__ == '__main__':
	parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

	parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
						metavar="file")

	args = parser.parse_args()

	print(args.file)

	#with open('task2_1.txt', 'r') as myfile:
	 #data=myfile.read().replace('\n', '')
	 #print(data)
	output_file = open("task_5_1_result.txt", "w+")

rules = []    
with open(args.file, "r") as file:
	for line in file:
	 data = line.strip()
	 rules.append(data)
	 #print(data)
#print(rules)

FirstOutput = []
FollowOutput = []
FinalOutputRules = []

def First(symbol):
	FinalOutput = symbol + " " + ":" + " " 
	i = 0
	rule2 = ""
	while i < len(rules):
		rule = rules[i]
		if rule[0] == symbol:
			rule2 = rule
		i += 1
	rule2 = rule2.replace(" ", "")
	#rule2Split = []
	data = rule2.split("|")
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

	i2 = 1
	while i2< len(data1):
		rule = data1[i2]
		if rule[0].islower() and rule != "epsilon":
			FinalOutput = FinalOutput + rule[0] + " " 
		if rule == "epsilon":
			FinalOutput = FinalOutput + "epsilon"
		if rule[0].isupper():
			i = 0
			while i < len(rule):
			 First(rule[i])
			 i += 1
			#print(FinalOutputRules)
		i2 += 1
	FinalOutputRules.append(FinalOutput)
	#print(FinalOutputRules)
	if len(FinalOutputRules) > 1:
	 i4 = 0
	 while i4 < len(FinalOutputRules):
		 rule = FinalOutputRules[i4]
		 data = rule.split(":")
		#print(data)
		 if "epsilon" in data[1]:
			 FinalOutput += data[1]
		 if "epsilon" not in data[1]:
			 FinalOutput += data[1]
			 break  
		 i4 += 1
	 FinalOutput = FinalOutput.replace("epsilon", "")
	 FinalOutput = FinalOutput.replace("  ", " ")
	#print(FinalOutput)
	stringy = ""
	i5 = 0
	while i5 < len(FinalOutput):
	 if FinalOutput[i5] == ":":
		 stringy = FinalOutput[i5+1:]
	 i5 += 1
	if stringy != " ":
	 FirstOutput.append(FinalOutput)
		


def follow(symbol):
	i = 0
	while i < len(rules):
		rule1 = rules[0]
		if rule1[0] == symbol:
			First(symbol)
			FinalStartStateRule = FirstOutput[len(FirstOutput)-1]
			FinalStartStateRule = FinalStartStateRule + ":" + " " + "$"
			FollowOutput.append(FinalStartStateRule)
			output_file.write(FinalStartStateRule + '\n')
			break
		else:
			rule = rules[i]
			data = rule.split(":")
			RestOfString = data[1]
			i = 0
			while i < len(RestOfString):
				if RestOfString[i] == symbol:
					RestOfStringAfterSymbol = RestOfString[i+1:]
					RestOfStringAfterSymbol = RestOfStringAfterSymbol.replace(" ", "")
					#print(RestOfStringAfterSymbol)
					FinalOutputString = "$"
					j = 0
					while j < len(RestOfStringAfterSymbol):
						char = RestOfStringAfterSymbol[j]
						First(char)
						if len(FirstOutput) > 0:
						 FinalOutputString2 = FirstOutput[len(FirstOutput)-1]
						else:
						  break
						#print(FinalOutputString2)
						FirstOutput.clear()
						FinalOutputRules.clear()
						data = FinalOutputString2.split(":")
						data2 = data[1]
						if "epsilon" not in data2:
							FinalOutputString = FinalOutputString.replace("$", "")
							FinalOutputString += data2
							break
						else:
							FinalOutputString += data2  

						j += 1
					FinalOutputString = FinalOutputString.replace("epsilon", "")
					First(symbol)
					FinalOutputStringYarab = FirstOutput[len(FirstOutput)-1]
					FinalOutputString = FinalOutputStringYarab + " " + ":" + " " + FinalOutputString
					FinalOutputString = FinalOutputString.replace("  ", " ")  
					if "$" in FinalOutputString:
						FinalOutputString = FinalOutputString.replace("$", "")
						FinalOutputString = FinalOutputString + "$"
						FinalOutputString = FinalOutputString.replace("  ", " ")
					print(FinalOutputString)
					output_file.write(FinalOutputString + '\n')    
				i += 1
			#print(RestOfString)    
		i += 1

		
'''i = 0
while i < len(rules):
 rule = rules[i]
 First(rule[0])
 print(FirstOutput[len(FirstOutput)-1])
 FirstOutput.clear()
 FinalOutputRules.clear()
 i += 1'''

j = 0
while j < len(rules):
	rule = rules[j]
	follow(rule[0])
	#print(FollowOutput)
	FirstOutput.clear()
	FinalOutputRules.clear()
	j += 1
#follow("S")
#print(FollowOutput)
#First("S")
#print(FirstOutput[len(FirstOutput)-1])


'''stringx = 'c : '
stringy = ""
i = 0
while i < len(stringx):
	if stringx[i] == ":":
		stringy = stringx[i+1:]
	i += 1
if stringy == " ":
	print("yaaas")'''



