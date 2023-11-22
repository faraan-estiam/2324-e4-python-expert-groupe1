# Count the Letters in the String
def countLetters(chaine):
  return { e : chaine.count(e) for e in chaine }

# Replace the max frequency letters with the letter 'e'
def replaceLetters(chaine):
  lettreCount = countLetters(chaine)
  lettreMaxFrequency = max(lettreCount, key=lettreCount.get)
  return chaine.replace(lettreMaxFrequency, 'e')

print( replaceLetters('Mississippi') )