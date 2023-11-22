# 1. Remplacez l'une des lettre qui apparait avec la grande plus fréquence par la lettre e dans le mot m. Remplacez également les autres lettres qui apparaissent avec la même fréquence max.
q1=lambda w:''.join(['e'if l in(lambda c:list(filter(lambda i:False not in [c[i]>=n for n in c.values()],c)))({k:w.count(k)for k in set(w)})else l for l in w])
# 2. Calculez la fréquence d'apparition de chaque lettre dans le mot m
q2=lambda w:{k:w.count(k)for k in set(w)}

word='mississippi'
print(q1(word))