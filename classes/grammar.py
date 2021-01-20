"""

The Grammar class

"""

from collections import defaultdict
import json
import os


class CFGGrammar(object):

    def __init__(self, raw_rules=None,json_backup=None):
        try:
            self.rules_dict = defaultdict(list)
            self.rules = list()
            if raw_rules is not None:
                self.from_txt(fp=raw_rules)
            elif json_backup is not None:
                self.from_json(fp=json_backup)
        except:
            raise("No rules were provided")

    def add_rule(self, rule):
        '''
        Add to dictionary

        :param rule:
        :return:
        '''
        self.rules_dict[rule[0]].append(rule[1:])


    def from_txt(self, fp):
        """
        Reads the input rules from a file and saves them as attribute of the class
        These will be further processed with .chomskyan_normal_form()
        :param fp: the path to the txt file with the rules
        :return: updates the attribute self.rules
        """
        # extract rules from file and process them
        with open(fp, 'r', encoding='utf-8') as grammar:
            rules = grammar.readlines()
        rules = [r.strip().replace("->", "").split() for r in rules]
        rules = [_ for _ in rules if _] # delete accidental white lines
        new_rules = []

        # Split double outputs
        for r in rules:
            if "|" in r:
                index = r.index("|")
                new_rules.append(r[:index])
                rule_2 = [r[0]]
                rule_2.extend(r[index+1:])
                new_rules.append(rule_2)
            else:
                new_rules.append(r)
        self.rules = new_rules

    def from_json(self,fp):
        with open(fp, 'r') as rules:
            self.rules_dict = json.load(rules)

    def chomskyan_normal_form(self) -> list:
        '''
        Main function, normalizes the grammar into the Chomsky normal form

        The scope is to convert the original rules into rules which  have either
        exactly one terminal symbol or exactly two non terminal symbols on its right hand side.

        '''
        production, result = [], []
        index = 0

        for r in self.rules:
            new_rule = []
            if len(r) == 2 and r[1][0] != "'": # this rule doesn't produce a terminal node
                production.append(r)
                self.add_rule(r)
                continue # the for loop
            elif len(r) > 2: # then we must normalize the rule
                terminals = [(item, i) for i, item in enumerate(r) if item[0] == "'"]
                if terminals: # shortcut for "if terminals is not empty"
                    for item in terminals:
                        #Create new rule in chomskyan form
                        r[item[1]] = f"{r[0]}{str(index)}"
                        new_rule += [f"{r[0]}{str(index)}", item[0]]
                    index += 1
                while len(r) > 3:
                    new_rule +=  [f"{r[0]}{str(index)}", r[1], r[2]]
                    r = [r[0]] + [f"{r[0]}{str(index)}"] + r[3:]
                    index += 1
            self.add_rule(r)
            result.append(r)
            if new_rule:
                result.append(new_rule)
            # Handle Production
            while production:
                rule = production.pop()
                if rule[1] in self.rules_dict:
                    for item in self.rules_dict[rule[1]]:
                        new_rule = [rule[0]] + item
                        if len(new_rule) > 2 or new_rule[1][0] == "'":
                            result.append(new_rule)
                        else:
                            production.append(new_rule)
                        self.add_rule(new_rule)

        # Last check and/or expansion
        # TODO Not so nice, but needed to prevent that something goes lost from self.rules to self.rules_dict
        for rule in result:
            if rule[0] not in self.rules_dict:
                self.add_rule(rule)
            else:
                if rule[1:] not in self.rules_dict[rule[0]]:
                    self.add_rule(rule)
        #for k,v in self.rules_dict.items():
            #print(str(k) +"\t" + str(v))
        return result

    def to_json(self,output_path):
        try:
            with open(output_path, 'w',encoding='UTF-8') as fp:
                json.dump(self.rules_dict,fp)
        except:
            print('You can save the CFG in the Chomskyan normal form, only if you previously transformed it using the .chomskyan_normal_form() method')

    def __repr__(self):
        return 'Context Free Grammar'

    def __len__(self):
        return len(self.rules_dict)
