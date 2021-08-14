#!/usr/bin/python

# Sort Komplete Kontrol Templates (Keyboard layouts) by their name
import json, copy

# Load the file
with open("Komplete Kontrol MK2 Settings.dat") as f:
    data = json.load(f)
    sorted_data = copy.deepcopy(data)
    templates = data['templates']
    templates_keys = templates.keys()
    sorted_templates = sorted(templates_keys, key = lambda id: templates[id]['Name'], reverse=False)
    i = 0
    for id in sorted_templates:
        print(templates[id]['Name'])
        sorted_data['templates'][str(i)] = templates[id]
        i += 1
    
with open('Komplete Kontrol MK2 Settings-sorted.dat', 'w') as f2:
    json.dump(sorted_data, f2)
