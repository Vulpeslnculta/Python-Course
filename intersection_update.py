from typing import Set, Any

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

words = set(text.split())
preps_used = words.intersection(prepositions)

print(preps_used)