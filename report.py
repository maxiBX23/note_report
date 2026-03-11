## Étant donné une liste de notes :
## 14, 15, 10, 12, 8, 16, 11, 14, 19
## Affichez un rapport sous la forme suivante :
## 
## Nombre de notes = 9
## Note 1 = 14/20 (Très bien)
## Note 2 = 15/20 (Très bien)
## Note 3 = 10/20 (Passable)
## Note 4 = 12/20 (Bien)
## Note 5 = 05/20 (Insuffisant)
## Note 6 = 16/20 (Excellent)
## Note 7 = 11/20 (Passable)
## Note 8 = 14/20 (Très bien)
## Note 9 = 19/20 (Excellent)
## Note minimale = 8
## Note maximale = 19
## Moyenne = 13.2 (Bien)
## Delta = 11
## 
## Notes:
## 
## Delta :
## C'est la différence entre la note minimale et maximale
## 
## Mentions :
## 16 - 20   = Excellent
## 14 - 15.9 = Très bien
## 12 - 13.9 = Bien
## 10 - 11.9 = Passable
## 00 - 9.9  = Insuffisant

## # somme simple
## def somme (a:int, b:int) -> int:
##     somme = a+b
##     return somme
## 
## print (somme(14,15))
## 
## #somme list
## def somme (notes:list) -> int:
##     somme = 0
##     for note in notes:
##         somme = somme + note
##     return somme
## 
## print (somme([14, 15, 19]))
## 

def somme (notes:list) -> int:
    somme = 0
    for note in notes:
        somme = somme + note
    return somme

def compteur(notes:list) -> int:
    compteur=0
    for note in notes:
        compteur= compteur +1
    return compteur

def moyenne(notes:list) -> float: # attention nombre à virgule.
    moyenne = somme(notes)/compteur(notes)
    return moyenne
    
def mention(a:int | float) -> str:          # | égale "ou" (permet de laisser le choix)
    mention=" "
    if a<10:
        mention="Insuffisant"
    elif a<12:
        mention="Passable"
    elif a<14:
        mention="Bien"
    elif a<16:
        mention="Très bien"
    else:
        mention="Excellent"
    return mention

def mini(notes:list) -> int:
    mini=notes[0]
    for n in notes:
     if n<mini:
        mini=n
    return mini

def maxi(notes:list) -> int:
    maxi=notes[0]
    for n in notes:
     if n>maxi:
        maxi=n
    return maxi

def delta(notes:list) -> int:
    delta=max(notes)-min(notes)
    return delta


Résultats= [14, 15, 10, 12, 8, 16, 11, 14, 19]

print("Nombre de notes =", compteur(Résultats))

count=1
for n in Résultats:
    print ("Note", count, "=", n,"/20 (",mention(n),")")
    count=count+1

print("Note minimale =", mini(Résultats))
print("Note maximale =", maxi(Résultats))
print("Moyenne =", round(moyenne(Résultats),1),"(",mention(moyenne(Résultats)),")")
print("Delta =", delta(Résultats))
