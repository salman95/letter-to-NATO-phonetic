def phoneticRead(letter) :
    if letter == 'a':
        print("Alpha ", end = " ")
    elif letter == 'b' :
        print("Beta ", end = " ")
    elif letter == 'c' :
        print("Charlie", end = " ")
    elif letter == 'd' :
        print("Delta", end = " ")
    elif letter == 'e' :
        print("Echo", end = " ")
    elif letter == 'f' :
        print("Foxtrot", end = " ")
    elif letter == 'g' :
        print("Golf", end = " ")
    elif letter == 'h' :
        print("Hotel", end = " ")
    elif letter == 'i' :
        print("India", end = " ")
    elif letter == 'j' :
        print("Juliet", end = " ")
    elif letter == 'k' :
        print("Kilo", end = " ")
    elif letter == 'l' :
        print("Lima", end = " ")
    elif letter == 'm' :
        print("Mike", end = " ")
    elif letter == 'n' :
        print("November", end = " ")
    elif letter == 'o' :
        print("Oscar", end = " ")
    elif letter == 'p' :
        print("Papa", end = " ")
    elif letter == 'q' :
        print("Quebec", end = " ")
    elif letter == 'r' :
        print("Romeo", end = " ")
    elif letter == 's' :
        print("Sierra", end = " ")
    elif letter == 't' :
        print("Tango", end = " ")
    elif letter == 'u' :
        print("Uniform", end = " ")
    elif letter == 'v' :
        print("Victor", end = " ")
    elif letter == 'w' :
        print("Whiskey", end = " ")
    elif letter == 'x' :
        print("X-Ray", end = " ")
    elif letter == 'y' :
        print("Yankee", end = " ")
    elif letter == 'z' :
        print("Zulu",end = " ")
    elif letter == (' ') :
        print(end = " ")
    else :
        print(letter,end = " ")

input1 = input("Type letters: ")
i = 0
while i < len(input1) :
    phoneticRead(input1[i])#Strings can be read as a list. Dont need to put in list.
    i += 1
