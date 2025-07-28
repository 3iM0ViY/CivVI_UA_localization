# н-на кількість рядків для перекладу 
l = """<Row Tag="LOC_READY_UNSUPPORTED">
			<Text>Unsupported.</Text>
		</Row>
		"""
 
import re
 
names = re.findall("<Text>.+</Text>", l)
# print(names)
names_2 = []
for i in names:
    i = i.replace("<Text>", "")
    i = i.replace("</Text>", "")
    names_2.append(i)
    
for i in names_2:
    print(i) # чстий текст для перекладу
    
# перекладений текст
tr = """

"""

tr_l = []
for line in tr.splitlines():
    if line != "":
        tr_l.append(line)

# print(tr_l)

for i in tr_l:
    print(f"<Text>{i}</Text>") # форматування перекладеного тексту