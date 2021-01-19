__author__ = "Antonio Masotti"
__date__ = "Jan 2021"


"""
DOC:

"""



from classes.parser import  *
from pprint import pprint

"""
print('testing')

grammar = CFGGrammar(rules_as_file="./rules.txt",parser=None)
pprint(grammar.rules,compact=True)

res = grammar.chomskyan_normal_form()
print("\n"*4)
pprint(res)
print("\n"*4)

pprint(grammar.rules,compact=True)
pprint(grammar.rules_dict,compact=True)
grammar.to_json(output_path="./cfg_normalform.json")
"""


if __name__ == '__main__':
    ARGUMENTS = sys.argv
    if len(ARGUMENTS) > 3 or len(ARGUMENTS) == 2:
        print("Usage: python3 Parser.py <grammar.file> <sentence.file>\n"
              "or: python3 Parser.py <grammar as string> <sentence as string>")
    else:
        GRAMMAR = "as path for the grammar"
        SENTENCE =  "as sentence"
        gram = CFGGrammar(parser=None,rules_as_file="./rules.txt")
        sentence = input('Give me a sentence: ')
        sentence = sentence.lower()
        PARSER = Parser("rules.txt", sentence)
        PARSER.parse()
        PARSER.print_tree()

    '''elif len(ARGUMENTS) == 3:
        GRAMMAR = "as path for the grammar" if os.path.isfile(ARGUMENTS[1]) else "as grammar"
        SENTENCE = "as path for the sentence" if os.path.isfile(ARGUMENTS[2]) else "as sentence"
        print(f"Using {ARGUMENTS[1]} {GRAMMAR} and {ARGUMENTS[2]} {SENTENCE}.")
        PARSER = Parser(ARGUMENTS[1], ARGUMENTS[2])
        PARSER.parse()
        PARSER.print_tree()'''