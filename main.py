#!/usr/bin/env python3

from lark import Lark

l = Lark(r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')

text = '''{"key": [
   "item0", 
   "item1", 
   3.14, 
   true
   ]
}'''

print(text)
print("".ljust(10, "="))
print(l.parse(text).pretty())
