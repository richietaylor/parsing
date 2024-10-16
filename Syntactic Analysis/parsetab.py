
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A BINARY_LITERAL D EQUALS ID LPAREN M RPAREN Sprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : ID EQUALS expressionexpression : expression A termexpression : expression S termexpression : termterm : term M factorterm : term D factorterm : factorfactor : LPAREN expression RPARENfactor : BINARY_LITERALfactor : ID'
    
_lr_action_items = {'ID':([0,2,3,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,],[4,4,-3,-2,7,-13,-4,-7,-10,7,-12,7,7,7,7,-5,-6,-8,-9,-11,]),'$end':([1,2,3,5,7,8,9,10,12,18,19,20,21,22,],[0,-1,-3,-2,-13,-4,-7,-10,-12,-5,-6,-8,-9,-11,]),'EQUALS':([4,],[6,]),'LPAREN':([6,11,13,14,15,16,],[11,11,11,11,11,11,]),'BINARY_LITERAL':([6,11,13,14,15,16,],[12,12,12,12,12,12,]),'M':([7,9,10,12,18,19,20,21,22,],[-13,15,-10,-12,15,15,-8,-9,-11,]),'D':([7,9,10,12,18,19,20,21,22,],[-13,16,-10,-12,16,16,-8,-9,-11,]),'A':([7,8,9,10,12,17,18,19,20,21,22,],[-13,13,-7,-10,-12,13,-5,-6,-8,-9,-11,]),'S':([7,8,9,10,12,17,18,19,20,21,22,],[-13,14,-7,-10,-12,14,-5,-6,-8,-9,-11,]),'RPAREN':([7,9,10,12,17,18,19,20,21,22,],[-13,-7,-10,-12,22,-5,-6,-8,-9,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,],[3,5,]),'expression':([6,11,],[8,17,]),'term':([6,11,13,14,],[9,9,18,19,]),'factor':([6,11,13,14,15,16,],[10,10,10,10,20,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parse_bla.py',386),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parse_bla.py',390),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parse_bla.py',391),
  ('statement -> ID EQUALS expression','statement',3,'p_statement','parse_bla.py',399),
  ('expression -> expression A term','expression',3,'p_expression_add','parse_bla.py',405),
  ('expression -> expression S term','expression',3,'p_expression_sub','parse_bla.py',409),
  ('expression -> term','expression',1,'p_expression_term','parse_bla.py',413),
  ('term -> term M factor','term',3,'p_term_mul','parse_bla.py',418),
  ('term -> term D factor','term',3,'p_term_div','parse_bla.py',422),
  ('term -> factor','term',1,'p_term_factor','parse_bla.py',426),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parse_bla.py',431),
  ('factor -> BINARY_LITERAL','factor',1,'p_factor_binary','parse_bla.py',435),
  ('factor -> ID','factor',1,'p_factor_id','parse_bla.py',439),
]
