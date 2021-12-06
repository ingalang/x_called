import json
import pandas as pd
from collections import defaultdict
import numpy as np
import re

with open('ners_1990.txt', 'r') as file:
    ners_1990 = [line.strip('\n\r') for line in file]

with open('ners_2019.txt', 'r') as file:
    ners_2019 = [line.strip('\n\r') for line in file]

#print(ners_2019)
ners = ners_1990 + ners_2019

print(len(ners))

ners_set = set(ners)

print(len(ners_set))
print(ners_set)

entity_dict = defaultdict(set)

split_reg = re.compile(r'[\'\"], [\'\"]')

for line in ners_set:
    entity_tuple = re.split('[\'\"], [\'\"]', line)
    entity = entity_tuple[0].strip('(\'')
    category = entity_tuple[1].strip('\')')
    entity_dict[category].add(entity)

print(len(entity_dict))
print(entity_dict.keys())

entity_dict = {category : [e for e in entities] for category, entities in entity_dict.items()}
print(len(entity_dict))

with open('NER_dict.json', 'w') as outfile:
    json.dump(entity_dict, outfile)