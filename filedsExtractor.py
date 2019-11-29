

fieldsMap = {}
with open("./DPDBT.Fields.txt", encoding="utf8") as inp:
    for line in inp:
        fields = line.strip().split('\t')
        while '' in fields:
            fields.remove('')
        if len(fields) == 2:
            fieldsMap[fields[0]] = fields[1]
        
    
names = []        
display =[]
for fName, fDisplayName in fieldsMap.items():
    names.append(fName)
    display.append(fDisplayName)
    
        
#print( fieldsMap )

with open("./DPDBT.FieldsNames.out.txt", encoding="utf8", mode="w") as outF:
    outF.writelines(["'%s', " % item  for item in names])

with open("./DPDBT.FieldsDisplayNames.out.txt", encoding="utf8", mode="w") as outF:
    outF.writelines(["'%s', " % item  for item in display])