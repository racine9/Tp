notes = [12,8,15,17,9,11,14,6,13,16]

def Analyse_des_notes():#1
    nombre = len(notes)
    moyenne = sum(notes)/nombre
    minimum = min(notes)
    maximum = max(notes)
    print(nombre)
    print(moyenne)
    print(minimum)
    print(maximum)

def division_des_notes():#2
    valide = []
    ajournes = []
    for note in notes:
        if (note >= 10):
            valide.append(note)
        else:
            ajournes.append(note)
    print(valide)
    print(len(ajournes))

def ordre_croissant():#3
    croissant = sorted(notes)
    print(croissant)
    print(croissant[7::])

def bonus():#4
    nouveau = []
    for note in notes:
        if(note < 9 ):
            note += 2 
        elif(note < 10):
            note += 1
        nouveau.append(note)
    print(nouveau)
    
def histogramme(notes):#5
    t1 = []
    e1 = []
    t2 = []
    e2 = []
    t3 = []
    e3 = []
    t4 = [] 
    e4 = []
    for note in notes:
        if (note >= 0 and note <= 4):
            t1.append(note)
            e1.append("*") 
            j1 = "".join(e1)

        elif(note >= 5 and note <= 9 ):
            t2.append(note)
            e2.append("*")
            j2 = "".join(e2)

        elif(note >= 10 and note <= 14):
            t3.append(note)
            e3.append("*")
            j3 = "".join(e3)
        else :
            t4.append(note)
            e4.append("*")
            j4 = "".join(e4)
    if e1 == []:  
        print("0-4 | " )
    else:
        print("0-4 |" , j1)
    if e2 == []:  
        print("5-9 | " )
    else:
        print("5-9 |" , j2)
    if e3 == []:  
        print("10-14 | " )
    else:
        print("10-14 |" , j3)
    if e4 == []:  
        print("15-20 | " )
    else:
        print("15-20 |" , j4)
    
def rang(notes,note):#6
    r = notes[::-1]
    i = r.index(note) + 1
    print(i)
    
    
def fusioner_notes(notes):#7
    n = [15,6,18]
    notes = notes + n
    for note in notes:
        if (notes.count(note) > 1):
            notes.remove(note)        
    print(notes)


    


    

if (__name__ == "__main__"):
    Analyse_des_notes()
    division_des_notes()
    ordre_croissant()
    bonus()
    histogramme(notes)
    rang(notes,14)
    fusioner_notes(notes)