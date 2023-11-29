PRONOMS = """Pronoms personnels : je, me, m’, moi ; tu, te, t’, toi, nous, vous ; il, elle, ils, elles ; se, en, y,

le, la, l’, les ; lui, soi ; leur, eux,

lui, leur

 :

Pronoms démonstratifs : celui, celui-ci, celui-là ; celle, celle-ci, celle-là,

ceux, ceux-ci, ceux-là ; celles, celles-ci, celles-là,

ce, ceci, cela, ça,

 :

Pronoms possessifs : le mien, le tien, le sien ; la mienne, la tienne, la sienne,

les miens, les tiens, les siens ; les miennes, les tiennes, les siennes,

le nôtre, le vôtre, le leur ; la nôtre, la vôtre, la leur,

les nôtres, les vôtres, les leurs,

 :

Pronoms relatifs : qui, que, quoi, dont, où,

lequel, auquel, duquel ; laquelle, à laquelle, de laquelle,

lesquels, auxquels, desquels ; lesquelles, auxquelles, desquelles,

 :

Pronoms interrogatifs : qui, que, quoi, qu'est-ce,

lequel, auquel, duquel ; laquelle, à laquelle, de laquelle,

lesquels, auxquels, desquels ; lesquelles, auxquelles, desquelles,

 :

Pronoms indéfinis : on, tout

un, une, l'un, l'une ; les uns, les unes,

un autre, une autre ; d'autres, l'autre, les autres,

aucun, aucune, aucuns, aucunes,

certains, certaine, certains, certaines,

tel, telle, tels, telles ; tout, toute, tous, toutes,

le même, la même, les mêmes ; nul, nulle, nuls, nulles,

quelqu'un, quelqu'une ; quelques uns, quelques unes,

personne, autrui, quiconque,

d’aucuns"""

PRONOMS = ''.join(PRONOMS.lower().split(':')[1::2])
PRONOMS = PRONOMS.replace(';',',').replace('\n',',')
PRONOMS = filter(lambda word: word!='', PRONOMS.split(','))
PRONOMS = [str.strip(word) for word in PRONOMS]