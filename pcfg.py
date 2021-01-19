__author__ = "Antonio Masotti"
__date__ = "Jan 2021"


"""
DOC: Main file of the CFG-Parser

"""



from classes.parser import  *
from pprint import pprint

if __name__ == '__main__':
    ARGUMENTS = sys.argv
    if len(ARGUMENTS) > 3 or len(ARGUMENTS) == 2:
        print("Usage: python3 Parser.py <grammar.file> <sentence.file>\n"
              "or: python3 Parser.py <grammar as string> <sentence as string>")
    ################## WORK IN PROGRESS #####################################
    ## The following lines define some parameters just for testing sake
    ########################################################################
    else: 
        GRAMMAR = "as path for the grammar"
        SENTENCE =  "as sentence"
        sentence = input('Give me a sentence: ') # insert sentence as input from user
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