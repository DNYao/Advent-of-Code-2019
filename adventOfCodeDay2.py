#INTCODE Computer challenge

codeInputs = [1,1,1,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0]

#codeInputs = [1,0,0,0,99]

def addition(codes, pointer):
    position1 = codes[pointer+1]
    position2 = codes[pointer+2]
    position3 = codes[pointer+3]
    codes[position3] = codes[position2] + codes[position1]

def multiplication(codes, pointer):
    position1 = codes[pointer+1]
    position2 = codes[pointer+2]
    position3 = codes[pointer+3]
    codes[position3] = codes[position2] * codes[position1]

def stop(codes):
    return codes

def computer(codes):
    pointer = 0

    while True:
        if codeInputs[pointer] == 1:
            addition(codes, pointer)
            pointer += 4

        elif codeInputs[pointer] == 2:
            multiplication(codes, pointer)
            pointer += 4
        
        elif codeInputs[pointer] == 99:
            return stop(codes)

        else:
            print('error')
            break

def bruteForcer(codeInputs):

    for noun in range(100):
        for verb in range(100):
            codeCopy = codeInputs.copy()
            codeCopy[1] = noun
            codeCopy[2] = verb
            output = computer(codeCopy)

            if output[0] == 19690720:
                print(noun, verb)
                break
            
    return

bruteForcer(codeInputs)