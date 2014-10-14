#!/usr/bin/python

import switcher.switcher as ss

sc = ss.SourceSwitcher()
sc.set_model('/home/olexandr/Desktop/json_sample')

from data import relation
# print dir(relation)
relation.Tablen()
