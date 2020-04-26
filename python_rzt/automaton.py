import ahocorasick

A=ahocorasick.Automaton()

with open('sensitive.txt',encoding='utf-8') as f:
 	data=f.read()
for idx, key in enumerate(data.split()):
 	A.add_word(key,(idx,key))
 		


A.make_automaton()

def automaton(content):
	for end_index, (insert_order, original_value) in A.iter(content):
		start_index = end_index - len(original_value) + 1
		content=content[:start_index-1]+'*'*len(original_value)+content[end_index+1:]
	return content

