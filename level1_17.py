currentLine = ""
stack = [currentLine]
stackCursor = 0
wasUndoOrRedo = False

def BastShoe(command):
    global stack
    global stackCursor
    global currentLine
    global wasUndoOrRedo
    
    if command[0] == "1" or command[0] == "2":
        if wasUndoOrRedo:
            stack = [currentLine]
            stackCursor = 0
            wasUndoOrRedo = False

        actionNumber = command[0]
        actionData = command[2:]
        if actionNumber == "1":
            currentLine += actionData
        elif actionNumber == "2":
            currentLine = currentLine[:(len(currentLine) - int(actionData))]

        stack.append(currentLine)
        stackCursor += 1



    if command[0] == "3":
        commandItems = command.split()
        index = int(commandItems[1])
        if index < 0 or index >= len(currentLine): 
            return ""
        else:
            return str(currentLine[index])
        
    if command[0] == "4":
        if len(stack) > 1 and stackCursor > 0:
            stackCursor -= 1
            currentLine = stack[stackCursor]
            wasUndoOrRedo = True
            
        
    if command[0] == "5":
        if len(stack) > 1 and stackCursor < len(stack) - 1:
            stackCursor += 1
            currentLine = stack[stackCursor]
            wasUndoOrRedo = True

    return currentLine   

