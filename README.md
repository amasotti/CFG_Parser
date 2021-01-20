# CYK-Parser for CFG Grammars

Almost the same parser as in [RobMcH/cyk_parser](https://github.com/RobMcH/CYK-Parser) and [phiSgr(CYK_parser)](https://github.com/phiSgr/CYK-Parser)
but more in Object oriented fashion.

This is a simple context-free grammar parser, in Python3.

**Feel free to use any piece of the code in your own projects.**

## Structure

+ Main folder
    + cfg.py *main file*
    + README.md *this document*
    + data
        + rules.txt *the phrase structure grammar rules*
        + normalized.json *a backup of the grammar in json format, for future load*
    + classes
        + grammar.py *Implementation of the CFGGrammar class*
        + parser.py *Implementation of the Parser class + some other useful functions*

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
+ Each class has some new methods
+ Parser
    + The tree is printed with round parenthesis (for compatibility with some nltk tree tools)
    + *grammar_from_file* and *grammar_from_string* were collapsed into the new method *load_grammar*
    + Start symbol fixed as "S"
+ Grammar class
    + Deleted option to give a single rule via string input *I think it makes things more complicated, and one can still test single
rules using the text file*
    + Possibility to load previously normalized grammar from json


+ *Added ASCII art - for fun ;)*
# How does it work:

*Still in development*

## TO DO
+ <del>Class implementation for Grammar<del>
+ Implement a function to draw parsed sentences as tree
+ <del>Remove duplicates from `self.rules_dict`<del>
+ Allow self.input (Parser) to parse  more than one sentence in batch
+ Implement probabilistic CFG
+ <del>The Parsing should search for alternative paths<del>
+ Find nicer ways to check for duplicates in trees (Parser) and in self.rules_dict (Grammar)
