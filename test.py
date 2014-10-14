#!/usr/bin/python

import switcher.switcher as ss

sc = ss.SourceSwitcher()
sc.set_model('json_sample.json')

from data import relation
# print dir(relation)
tn = relation.Tablen()
print next(tn.idtablen())
print next(tn.idtablen())
print next(tn.idtablen())
print tn.idtablen[0]
print tn.fk_field[0].idtable1[0]
print tn.fk_field[0].char_field[0]