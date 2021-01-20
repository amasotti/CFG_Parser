__author__ = "Antonio Masotti"
__date__ = "Jan 2021"


"""
DOC: Main file of the CFG-Parser

"""



from classes.parser import  *
from pprint import pprint
import sys
import os


def ascii_logo():
    print("""                           _______  _______  _______ 
                          (  ____ \(  ____ \(  ____ \
                          | (    \/| (    \/| (    \/
                          | |      | (__    | |      
                          | |      |  __)   | | ____ 
                          | |      | (      | | \_  )
                          | (____/\| )      | (___) |
                          (_______/|/       (_______)
                                                     
              _______  _______  _______  _______  _______  _______ 
             (  ____ )(  ___  )(  ____ )(  ____ \(  ____ \(  ____ )
             | (    )|| (   ) || (    )|| (    \/| (    \/| (    )|
             | (____)|| (___) || (____)|| (_____ | (__    | (____)|
             |  _____)|  ___  ||     __)(_____  )|  __)   |     __)
             | (      | (   ) || (\ (         ) || (      | (\ (   
             | )      | )   ( || ) \ \__/\____) || (____/\| ) \ \__
             |/       |/     \||/   \__/\_______)(_______/|/   \__/
                                                                   \n\n Welcome!""")

if __name__ == '__main__':
    # Welcome
    ascii_logo()
    ARGUMENTS = sys.argv
    if len(ARGUMENTS) > 3 or len(ARGUMENTS) == 2:
        print("Usage: python3 Parser.py <grammar.file> <sentence.file>\n"
              "or: python3 Parser.py <grammar as string> <sentence as string>")
    elif len(ARGUMENTS) == 3:
        GRAMMAR = ARGUMENTS[1]
        SENTENCE = ARGUMENTS[2]
        GRAMMAR_TYPE = "as path for the grammar" if os.path.isfile(ARGUMENTS[1]) else "as grammar"
        SENTENCE_TYPE = "as path for the sentence" if os.path.isfile(ARGUMENTS[2]) else "as sentence"
        print(f"Using {GRAMMAR} {GRAMMAR_TYPE} and {SENTENCE} {SENTENCE_TYPE}.")

        PARSER = Parser(GRAMMAR,SENTENCE)
        PARSER.parse()
        PARSER.print_tree()
    ################## WORK IN PROGRESS #####################################
    ## The following lines define some parameters just for testing sake
    ########################################################################
    else:
        GRAMMAR =  os.path.abspath("data/rules.txt")
        SENTENCE = input('Give me a sentence: ').lower()
        print(f"Using {GRAMMAR} as testing path and '{SENTENCE}' as sentence.")
        PARSER = Parser(GRAMMAR, SENTENCE)
        PARSER.parse()
        PARSER.to_tree()
        #PARSER.print_tree()