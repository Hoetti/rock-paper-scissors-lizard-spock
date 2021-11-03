import random 

#main variables and lists
st = "stein"
sc = "schere"
pa = "papier"
ec = "echse"
sp = "spock"
randomlist = ['schere', 'stein',  'papier', 'echse', 'spock']
wins = 0
loses = 0
draws = 0
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


Da wir dies nun hoffentlich erledigt haben, fangen wir am besten direkt mit dem Spiel an. Also, ... """
winsmessage = ""
losemessage = ""
drawmessage = ""

#welcome message, input command and random output for opponent
print(welcomemessage)

dic = {"help": "shows all comands",}


#main loop-


while (True):
    
#input command and random output for opponent
    inpu = input("Schere, Stein, Papier, Echse oder Spock ? ")
    randomoutput = random.choice(randomlist)

#string-method .lower for input
    inpu = inpu.lower()


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
        

#exit
    elif inpu == ("exit"):
        break




    #else :
     #   print(errormessage)

    elif inpu == ("help"):
         print(dic)
    
    
#result output
    print("Dein Zug: " + inpu)
    print("Der Zug des Computers: " + randomoutput)
    if wins == wins + 1:

        
        print(winsmessage) 


        
        

print(wins)
print(loses)
print(draws)
        
