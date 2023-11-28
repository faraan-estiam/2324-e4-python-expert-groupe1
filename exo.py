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