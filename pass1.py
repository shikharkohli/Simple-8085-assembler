import opcodemap

code = '''ORG 4000H
        START:LXI H,4000H
        MOV R,M
        INX H
        ADD M
        INX H
        MOV M,R
        HLT
        JMP START'''

def buildSymbolTable(code):
    code = code.lstrip().rstrip()
    lines = code.split("\n")
    #print lines
    symbolTable = {}
    i = 0 
    if "ORG" in lines[0]:
        i = int(lines[0].split(" ")[1][:-1])-1
    symbolTable['codestartshere'] = i
    #print lines[1]
    #print "i ==>",
    #print i
    for line in lines:
        if line[0] == ";":
            continue
        if len(line.split(":")) > 1:
            symbolTable[line.split(":")[0].rstrip().lstrip()] = i
        i += 1
        if line.split(",")[-1][:-1].isdigit():
            if int(line.split(",")[-1][:-1]) >= 0xFF:
                i += 2
            else:
                i += 1
    #print i
    #print "The symbol table is"
    #print symbolTable
    return symbolTable

def createMachineCode(symbolTable,code,opcodesMap):
    loc = symbolTable['codestartshere'] + 1
    lines = code.split("\n")
    objectCode = {}
    for line in lines:
        if line[0:3] == "ORG":
            continue
        #if line[0] == ";":
        #    continue
        print line
        line = line.rstrip().lstrip()
        if ":" in line:
            line = line.split(":")[1]
        if line in opcodemap.opCodesMap.keys():
            objectCode[loc] = opcodemap.opCodesMap[line]
            loc += 1
        elif line[-3:-1].isdigit() or line[-5:-1].isdigit():
            codeLine = line.split(",")
            print codeLine[-1]
            if int(codeLine[-1][:-1]) >= 0xFF:
                objectCode[loc] = opcodemap.opCodesMap[codeLine[0]+",NN"]
                loc += 1
                objectCode[loc] = codeLine[1][-3:-1]
                loc += 1
                objectCode[loc] = codeLine[1][-5:-3]
                loc += 1
            else:
                objectCode[loc] = opcodemap.opCodesMap[codeLine[0]+",N"]
                loc += 1
                objectCode[loc] = codeLine[1][-3:-1]
                loc += 1
        else:
            line = line.split(' ')
            objectCode[loc] = opcodemap.opCodesMap[line[0] +" A"]
            loc += 1
            objectCode[loc] = symbolTable[line[1]]
    return objectCode
    
print createMachineCode(buildSymbolTable(code),code,opcodemap.opCodesMap)
#print opcodemap.opCodesMap
