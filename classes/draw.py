import svgling


test = ("S", ("NP+PRON", "I"), ("VP", ("VERB", "saw"), ("NP+PRON", "him")))


tree = svgling.draw_tree(test,leaf_nodes_align=True)

print(tree)

pict = tree.get_svg()

with open('tree.svg','w') as t:
    pict.write(t, pretty=True, indent=2)