# CYK-Parser for CFG Grammars

Almost the same parser as in [RobMcH/cyk_parser](https://github.com/RobMcH/CYK-Parser) and [phiSgr(CYK_parser)](https://github.com/phiSgr/CYK-Parser)
but more in Object oriented fashion.

This is a simple context-free grammar parser, in Python3.

My try to build a Parser for a PCF Grammar

#

The code isn't by any means perfect and isn't supposed to.
**Feel free to use any piece of the code in your own projects.**


## Rules
*Here example of rules*
    
    S -> VP NP
    VP -> V NP
    NP -> D N
    NP -> N PP
    ...

In this version of the Parser (other as in the original repos), also rules with double outputs
are accepted:

    V -> 'buy' | 'sell'
    S -> VP NP | VP
 
 
**N.B:** Non terminal nodes should be listed in single quotes in the grammar file.
The Parser will use this sign to distinguish terminal from non terminal nodes:

    V -> 'buy'
    
    **NOT**  V -> buy
    
# Main modifications

+ Grammar and Parser are now implemented as classes
+ Each class has some new methods:
    + save, load

# How does it work:

*Still in development*

## TO DO

+ Implement a function to draw parsed sentences as tree
+ Remove duplicates from `self.rules_dict`