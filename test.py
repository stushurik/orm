#!/usr/bin/pythonfields.items()

import switcher.switcher as ss

sc = ss.SourceSwitcher()
sc.set_model('json_sample.json')

from data import relation
# print dir(relation)
tn = relation.Table1()
# print next(tn.idtablen()).re
# print next(tn.idtablen())
# print next(tn.idtablen())
# print tn.idtablen[0]
# print tn.fk_field[0].idtable1[0]
# print tn.fk_field[0].char_field[0]

# print tn.idtablen.relation
# print tn.fk_field.relation

# tn.int_field[3] = 5
tn.char_field[3] = "test_char"
tn.save()