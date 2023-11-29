#Faraan Rozbully; Lucas Cannizzaro; Nathan Schoepps; Matéo Oudart; Akbar Khan
from pronoms import PRONOMS

def nombre_de_chaque_lettres(mot): #prend en argument un mot
    compteur = {}   #on initialise un dictionaire vide
    for letter in mot: #pour chaque lettre du mot
        compteur[letter] = mot.count(letter) #on enregistre le nombre d'occurence de la lettre
    return compteur #on renvoie le nombre

def remplacer_par_e(mot): #prend en argument un mot
    a_remplacer = max(nombre_de_chaque_lettres(mot)) #on récupère la lettre qui reviens le plus souvent
    resultat = '' #on initialise un résultat
    for lettre in mot: #pour chaque lettre du mot
        if lettre == a_remplacer : #si on doit remplacer la lettre
            resultat += 'e' #on la replace
        else: # sinon
            resultat += lettre #on laisse la lettre d'origine
    return resultat #on retourne le resultat

# Replace the max frequency letters with the letter 'e'
def replaceLetters(chaine):
    lettreCount = nombre_de_chaque_lettres(chaine)
    maxFrequency = max(lettreCount.values()) #on récupère la fréquence de lettre à remplacer
    
    lettersToReplace = []
    for letter in lettreCount.keys():       #pour chaque lettre du mot
        frequency = lettreCount[letter]     #on récupère la fréquence d'apparition
        if frequency == maxFrequency:       #si la fréquence est le max
            lettersToReplace.append(letter) #on sauvegarde la lettre pour qu'elle soit remplacée
    
    # Replace each of these letters with 'e'
    for letter in lettersToReplace:
        chaine = chaine.replace(letter, 'e')
    
    return chaine

mot='Mississippi'
print("\nje remplace une des lettre qui revient le plus par 'e'",remplacer_par_e(mot))
print("\nje remplace les lettre qui reviennent le plus par 'e'",replaceLetters(mot))
print("\nnombre de chaque lettres",nombre_de_chaque_lettres(mot))


def countInText(txt):
    countStringLe = txt.lower().count(' le ')
    countLetterE = txt.lower().count('e')
    newTxt = txt.replace('e', ' ').replace('E',' ')
    return countStringLe, countLetterE, newTxt

def data_to_json(txt:str) :
    import json
    global PRONOMS
    path = "./data.json"
    txt = txt.lower()
    pronoms = {key:txt.lower().count(f' {key} ') for key in PRONOMS}
    letter_e = txt.lower().count('e')
    data = {"nombre pronom":pronoms,"nombre e":letter_e}

    with open(path,'w') as file :
        json.dump(data,file)

def mot_les_plus_frequent(txt:str):
    #on prépare le texte
    txt = txt.lower().translate(str.maketrans("'"," ",".,()"))
    #on met chaque mot dans une liste
    arr = txt.split()

    #on compte les occurence des mots
    data = {word:arr.count(word) for word in set(arr)}
    
    #on renvoie ceux qui reviennent le plus souvent ainsi que leur nombre d'occurence
    freq = max(data.values())
    return list(filter(lambda key: data[key]==freq ,data)), freq

def mot_les_plus_frequent_nopronouns(txt:str):
    #on prépare le texte
    txt = txt.lower().translate(str.maketrans("'"," ",".,()"))
    #on met chaque mot dans une liste
    arr = txt.split()

    #on compte les occurence des mots (sauf les pronoms)
    global PRONOMS
    data = {word:arr.count(word) for word in list(filter(lambda word: word not in PRONOMS,set(arr)))}
    
    #on renvoie ceux qui reviennent le plus souvent ainsi que leur nombre d'occurence
    freq = max(data.values())
    return list(filter(lambda key: data[key]==freq ,data)), freq
txt = """Je vois là-bas un être sans tête qui grimpe à une perche sans fin.

Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement
soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment
grimpe, et s'en va grimpant sur son terrible chemin vertical.

Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une
position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours.

Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter
et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas.

Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace
lui doive être plus haïssable encore.

Henri Michaux"""

print("\nje compte le nombre de fois où 'le' apparait, 'e' apparait et renvoie le texte sans 'e'")
le, e, res = countInText(txt)
print(f"le : {le}, e : {e} , txt :\n{res}")
data_to_json(txt)
print(mot_les_plus_frequent(txt))
print(mot_les_plus_frequent_nopronouns(txt))