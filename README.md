<img alt="GitHub" src="https://img.shields.io/github/license/amasotti/CFG_Parser">

----
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
+ New rule file: `rules_usami.txt` from [usami/pcfg](https://github.com/usami/pcfg)
+ Minor code improvement (I hope)
+ Parser
    + The tree is printed with round parenthesis (for compatibility with some nltk tree tools)
    + *grammar_from_file* and *grammar_from_string* were collapsed into the new method *load_grammar*
    + Start symbol fixed as "S"
    + The parser searches (after the CYK-Algorithm) if there are alternative derivations. If you want only
    derivations starting from 'S', you can pass the bool param. `only_s` to the method `.to_tree`
+ Grammar class
    + Deleted option to give a single rule via string input *I think it makes things more complicated, and one can still test single rules using the text file*
    + Possibility to load previously normalized grammar from json

+ *work in progress*: Draw Tree as svg, see below:

![tree](./tree.svg)

+ *Added ASCII art - for fun ;)*
# How does it work:

+ Grammar from file, sentence (at the moment, only a single sentence) from file:
>python3 cfg.py <grammar path> <sentence path>

+ Grammar from file, sentence from input (stdin):
> python3 cfg.py <grammar path> <sentence>

+ Default grammar ("data/rules_usami.txt") and sentence from input
> python3 cfg.py 

The Parser has several boolean parameters:
   + output (default `True`) : prints the parsings
   + only_s (default `False`) : search only for parsings which begin with start symbol "S" 
   + draw  (default `True`) : use NLTK to draw trees (these can be saved as .ps files)


