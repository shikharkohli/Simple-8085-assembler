opCodeFile = file("opcodeslisting.txt")
tempString = opCodeFile.read()
tempString = tempString.upper()
opCodesList = tempString.split("\n")
opCodesMap = {}
for i in range(0,len(opCodesList)):
    if len(opCodesList[i]):
        tempList = opCodesList[i].split("|")
        if len(tempList) >= 3:
            opCodesMap[tempList[1].rstrip()] = tempList[2].rstrip()

#for k in opCodesMap:
#    print k + "=>" + opCodesMap[k]
