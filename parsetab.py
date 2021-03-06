
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AEND AEND2 COST HEAD POSTRUNTIME POSTTITLE PREBOXOFFICE PREDIRECTOR PRELANGUAGE PREPRODUCER PRERUNTIME PRESTORYLINE PRETITLE PREWRITER STRINGstart : director \n                    | title\n                    | producer\n                    | writer\n                    | boxoffice\n                    | runtime\n                    | storyline\n                    | language\n        director : PREDIRECTOR nametitle : PRETITLE STRING POSTTITLE producer : PREPRODUCER namewriter : PREWRITER namestoryline : PRESTORYLINE STRINGboxoffice : PREBOXOFFICE COSTlanguage : PRELANGUAGE STRINGruntime : PRERUNTIME STRING POSTRUNTIMEname : HEAD STRING AENDname : HEAD STRING AEND2 name'
    
_lr_action_items = {'PREDIRECTOR':([0,],[10,]),'PRETITLE':([0,],[11,]),'PREPRODUCER':([0,],[12,]),'PREWRITER':([0,],[13,]),'PREBOXOFFICE':([0,],[14,]),'PRERUNTIME':([0,],[15,]),'PRESTORYLINE':([0,],[16,]),'PRELANGUAGE':([0,],[17,]),'$end':([1,2,3,4,5,6,7,8,9,18,21,22,23,25,26,28,29,30,32,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-11,-12,-14,-13,-15,-10,-16,-17,-18,]),'HEAD':([10,12,13,31,],[19,19,19,19,]),'STRING':([11,15,16,17,19,],[20,24,25,26,27,]),'COST':([14,],[23,]),'POSTTITLE':([20,],[28,]),'POSTRUNTIME':([24,],[29,]),'AEND':([27,],[30,]),'AEND2':([27,],[31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'director':([0,],[2,]),'title':([0,],[3,]),'producer':([0,],[4,]),'writer':([0,],[5,]),'boxoffice':([0,],[6,]),'runtime':([0,],[7,]),'storyline':([0,],[8,]),'language':([0,],[9,]),'name':([10,12,13,31,],[18,21,22,32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> director','start',1,'p_start','Task_2.py',78),
  ('start -> title','start',1,'p_start','Task_2.py',79),
  ('start -> producer','start',1,'p_start','Task_2.py',80),
  ('start -> writer','start',1,'p_start','Task_2.py',81),
  ('start -> boxoffice','start',1,'p_start','Task_2.py',82),
  ('start -> runtime','start',1,'p_start','Task_2.py',83),
  ('start -> storyline','start',1,'p_start','Task_2.py',84),
  ('start -> language','start',1,'p_start','Task_2.py',85),
  ('director -> PREDIRECTOR name','director',2,'p_director','Task_2.py',89),
  ('title -> PRETITLE STRING POSTTITLE','title',3,'p_title','Task_2.py',93),
  ('producer -> PREPRODUCER name','producer',2,'p_producer','Task_2.py',97),
  ('writer -> PREWRITER name','writer',2,'p_writer','Task_2.py',101),
  ('storyline -> PRESTORYLINE STRING','storyline',2,'p_storyline','Task_2.py',105),
  ('boxoffice -> PREBOXOFFICE COST','boxoffice',2,'p_boxoffice','Task_2.py',109),
  ('language -> PRELANGUAGE STRING','language',2,'p_language','Task_2.py',113),
  ('runtime -> PRERUNTIME STRING POSTRUNTIME','runtime',3,'p_runtime','Task_2.py',117),
  ('name -> HEAD STRING AEND','name',3,'p_name','Task_2.py',121),
  ('name -> HEAD STRING AEND2 name','name',4,'p_names','Task_2.py',125),
]
