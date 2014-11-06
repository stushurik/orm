#!/usr/bin/pythonfields.items()

import switcher.switcher as ss
import utils.utils as _

sc = ss.SourceSwitcher()
dm = sc.set_model('json_sample.json')

# from data import relation

tn = dm['Table1'](integer_field=1).idtable1[0]

# tn = relation.Table1(int_field=1).filter(char_field="char2").idtable1[0]

print tn
# print dir(relation)

# with _.Timer() as t:
#     tn = relation.Table1(int_field=1)
# print('Request took %.03f sec.' % t.interval)

# with _.Timer() as t1:
#     tn1 = relation.Table1(int_field=1)
# print('Request took %.03f sec.' % t.interval)

# tn2 = relation.Table1(int_field=1)

# tn3 = relation.Table1(int_field=2)

# tn3 = relation.Table1(int_field=2)
# print next(tn.int_field())
# print next(tn.int_field())
# print next(tn.int_field())

# print next(tn.idtablen()).re
# print next(tn.idtablen())
# print next(tn.idtablen())
# print tn.idtablen[0]
# print tn.fk_field[0].idtable1[0]
# print tn.fk_field[0].char_field[0]

# print tn.idtablen.relation
# print tn.fk_field.relation

# tn.int_field[3] = 5
# tn.char_field[3] = "test_char"
# tn.save()