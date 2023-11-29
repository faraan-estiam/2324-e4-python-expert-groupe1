import json

# Count the Letters in the String
def countLetters(chaine):
  return { e : chaine.count(e) for e in chaine }

# Replace the max frequency letter with the letter 'e'
def replaceLetter(chaine):
  lettreCount = countLetters(chaine)
  lettreMaxFrequency = max(lettreCount, key=lettreCount.get)
  return chaine.replace(lettreMaxFrequency, 'e')

# Replace the max frequency letters with the letter 'e'
def replaceLetters(chaine):
  lettreCount = countLetters(chaine)
  maxFrequency = max(lettreCount.values())
  
  lettersToReplace = []
  for letter in lettreCount.keys():
    frequency = lettreCount[letter]
    if frequency == maxFrequency:
        lettersToReplace.append(letter)
  
  # Replace each of these letters with 'e'
  for letter in lettersToReplace:
    chaine = chaine.replace(letter, 'e')
  
  return chaine

# Test
print(countLetters('Mississippi'))

print(replaceLetter('Mississippi'))

print(replaceLetters('Mississippi'))

###Part2

txt = "Je vois là-bas un être sans tête qui grimpe à une perche sans fin. Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment grimpe, et s'en va grimpant sur son terrible chemin vertical. Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours. Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas. Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace lui doive être plus haïssable encore. Henri Michaux"

##Exo 3
def countInText(txt):
  countStringLe = txt.count('le')
  countLetterE = txt.count('e')
  newTxt = txt.replace('e', ' ')
  return countStringLe, countLetterE, newTxt
 
print(countInText(txt=txt))

##JSON count E + pronoms
def jsonExo(txt):
  mots = txt.split()
  pronoms = ['je', 'tu', 'il', 'nous', 'vous', 'ils']
  pronom_counts = {pronom: 0 for pronom in pronoms}
  e_count = 0

  for mot in mots:
    for pronom in pronoms:
      if mot.lower() == pronom:
        pronom_counts[pronom] += 1
    e_count += mot.lower().count('e')

  ##Store in JSON
  data = {"pronom_counts": pronom_counts, "e_count": e_count}
  path = "res.json"

  with open(path, 'w') as file:
    json.dump(data, file)
