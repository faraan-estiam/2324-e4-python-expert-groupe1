# 1. Remplacez l'une des lettre qui apparait avec la grande plus fréquence par la lettre e dans le mot m. Remplacez également les autres lettres qui apparaissent avec la même fréquence max.
q1=lambda w:''.join(['e'if l in(lambda c:list(filter(lambda i:False not in [c[i]>=n for n in c.values()],c)))({k:w.count(k)for k in set(w)})else l for l in w])

# 2. Calculez la fréquence d'apparition de chaque lettre dans le mot m
q2=lambda w:{k:w.count(k)for k in set(w)}

# 3. Dans le texte suivant compter le nombre de fois que vous avez la prenom le, puis le nombre de e, et à l'aide d'un script effacez tous les e.
q3_1=lambda txt:txt.lower().count(' le ')
q3_2=lambda txt:txt.lower().count('e')
q3_3=lambda txt:txt.replace('e','')

# 4. A l'aide du code Python suivant enregistrez dans un fichier json les statistiques suivantes :
#       - nombre pronon
#       - nombre de e
import json
q4=lambda txt:json.dump({w:txt.lower().count(f' {w} ')for w in'je, me, moi, tu, te, toi, il, elle, on, le, la, lui, eux, leur, nous, vous, se, soi, en, y'.split(', ')}|{'e':txt.lower().count('e')},open('./q4.json','w'))

# 5. (facultatif ) Quel est le mot le plus utilisé dans le texte.
q5=lambda txt:(lambda data:list(filter(lambda key:False not in[data[key]>=val for val in data.values()],data)))((lambda newtxt:{word:newtxt.count(word)for word in set(newtxt)})(txt.lower().translate(str.maketrans("'"," ",".,()")).split()))

# 6. (facultatif ) Quel est le mot le plus utilisé dans le texte en dehors des pronons.
q6=lambda txt:(lambda data:list(filter(lambda key:False not in[data[key]>=val for val in data.values()],data)))((lambda newtxt:{word:newtxt.count(word)for word in filter(lambda word:word not in 'je, me, moi, tu, te, toi, il, elle, on, le, la, lui, eux, leur, nous, vous, se, soi, en, y'.split(', '),set(newtxt))})(txt.lower().translate(str.maketrans("'"," ",".,()")).split()))

# 7. Créez des couples de deux valeurs.
q7=lambda l,d:[tuple(l[i:len(l)])if len(l)-i<2*d else tuple(l[i:i+d])for i in range(0,len(l)+1-d,d)]


word='mississippi'
print("nombre de lettre du mot",word,q2(word))
print("remplacer les lettres du mot",word,"par des e",q1(word))

txt="Je vois là-bas un être sans tête qui grimpe à une perche sans fin.\n\
\n\
Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement\n\
soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment\n\
grimpe, et s'en va grimpant sur son terrible chemin vertical.\n\
\n\
Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une\n\
position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours.\n\
\n\
Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter\n\
et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas.\n\
\n\
Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace\n\
lui doive être plus haïssable encore.\n\
\n\
Henri Michaux"

print("nombre de le :",q3_1(txt))
print("nombre de e :",q3_2(txt))
print("le texte sans la lettre 'e':",q3_3(txt),sep='\n')
print("voir q4.json pour la question 4")
q4(txt)
print("les mots les plus fréquents",q5(txt))
print("les mots les plus fréquents sauf pronoms", q6(txt))
elems = ['a', 'b', 'c', 'a', 'b', 'a', 'd', 'e']
print("grouper la liste par deux", q7(elems,2))
