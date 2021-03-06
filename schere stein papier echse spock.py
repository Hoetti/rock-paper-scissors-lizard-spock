import random 

#main variables and lists
st = "stein"
sc = "schere"
pa = "papier"
ec = "echse"
sp = "spock"
randomlist = ['schere', 'stein',  'papier', 'echse', 'spock']

errormessage = "Entschuldigung aber dieses Handzeichen kenne ich nicht :/"
welcomemessage = """Hallo und Herzlich willkommen zu 'Schere, Stein, Papier, Echse, Spock' aus der Serie 'The Big Bang Theory'.
Ich hoffe dir gefällt es! 

Hier vorab noch mal die Regeln:

Also ...     
    Schere schneidet Papier         
    Papier bedeckt Stein                
    Stein zerquetscht Echse
    Echse vergiftet Spock
    Spock zertrümmert Schere
    Schere köpft Echse
    Echse frisst Papier
    Papier widerlegt Spock
    Spock verdampft Stein
    Stein schleift Schere

    Falls du noch mehr hilfe brauchst schreib einfach "help".
    Für den Fall, dass du keine Lust mehr hast schreib einfach "exit".


Da wir dies nun hoffentlich erledigt haben, fangen wir am besten direkt mit dem Spiel an.

Also, ... """
winsmessage = "Du hast scheinbar gewonnen ... Naja egal, herzlichen Glückwunsch und noch viel spaß =)"
losemessage = "Oh wie's aussieht hast du scheinbar verloren gegen mich verloren >=D ... naja probiers gerne nochmal =)"
drawmessage = "Unentschieden ! Probiers doch gerne nochmal =)"
commandlist = ["help: shows all comands",
"exit: leaves rounds",
"rules: opens game rules",
]



#welcome message
print(welcomemessage)


#main loop
while (True):
    
#input command and random output for opponent
    inpu = input("Schere, Stein, Papier, Echse oder Spock ? ")
    randomoutput = random.choice(randomlist)

#string-method .lower for input
    inpu = inpu.lower()

    wins = 0
    loses = 0
    draws = 0

# input error definition
    input_error = True

#scissors query
    if inpu == sc:
        
    #wins
        if randomoutput == pa:
            wins += 1 
        elif randomoutput == ec:
            wins += 1
        
    #loses
        elif randomoutput == st:
            loses += 1
        elif randomoutput == sp:
            loses += 1
        
    #draws
        elif randomoutput == sc:
            draws +=1
        
    #correctivity check
        input_error = False

#stone query
    elif inpu == st:
        
    #wins
        if randomoutput == sc:
            wins += 1 
        elif randomoutput == ec:
            wins += 1
        
    #loses
        elif randomoutput == sp:
            loses += 1
        elif randomoutput == pa:
            loses += 1
        
    #draws
        elif randomoutput == st:
            draws +=1
        
    #correctivity check
        input_error = False

#paper query
    elif inpu == pa:
        
    #wins
        if randomoutput == st:
            wins += 1 
        elif randomoutput == sp:
            wins += 1
        
    #loses
        elif randomoutput == sc:
            loses += 1
        elif randomoutput == ec:
            loses += 1
        
    #draws
        elif randomoutput == pa:
            draws +=1

    #correctivity check
        input_error = False

#lizard query
    elif inpu == ec:
        
    #wins
        if randomoutput == pa:
            wins += 1 
        elif randomoutput == sp:
            wins += 1
        
    #loses
        elif randomoutput == sc:
            loses += 1
        elif randomoutput == st:
            loses += 1
        
    #draws
        elif randomoutput == ec:
            draws +=1
        
    #correctivity check
        input_error = False

#spock query
    elif inpu == sp:
        
    #wins
        if randomoutput == sc:
            wins += 1 
        elif randomoutput == st:
            wins += 1
        
    #loses
        elif randomoutput == pa:
            loses += 1
        elif randomoutput == ec:
            loses += 1
        
    #draws
        elif randomoutput == sp:
            draws +=1
    
    #correctivity check
        input_error = False
        

#commands
    elif inpu == ("exit"):
        break

    elif inpu == ("help"):
        print("")
        print(commandlist)

    inpu = inpu.capitalize()
    randomoutput = randomoutput.capitalize()

    print("")
#result output
    
    #User input and bt output
    if input_error == False:
        print("Dein Zug: " + inpu)
        print("Der Zug des Computers: " + randomoutput)
    if input_error == True:
        print(errormessage)
    
    #win
    if wins > 0:
        print(winsmessage) 
    
    #lose
    elif loses > 0:
        print(losemessage)
    
    #draw
    elif draws > 0:
        print(drawmessage)

    print("")


#play again 
    '''print("")
    playagain = input("Willst du nochmal spielen ? ")
    playagain = playagain.lower()

    if playagain == ("ja"):
        print()
    elif playagain == ("nein"):
        break
    elif playagain == ("exit"):
        break
    else:
        print("")
        print("Probiere es nochmal")
        print("") '''
    

#loop ending
        

'''print("")        
print("Wins", wins)
print("")
print("Loses", loses)
print("")
print("Draws", draws)
print("")'''
