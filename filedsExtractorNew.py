import xml.etree.ElementTree as ET
import csv

tree = ET.parse("BusinessTrip.ContentType.xml")
root = tree.getroot()

fieldsMap = {}
for field in list(root[0][0]):
    name = field.attrib['Name']
    displayName = field.attrib['DisplayName']
    fieldsMap[name] = displayName
    

with open("./DPDBT.FieldsNames.out.txt", encoding="utf8", mode="w") as outF:
    outF.writelines(["'%s', " % item  for item in fieldsMap.keys()])

with open("./DPDBT.FieldsDisplayNames.out.txt", encoding="utf8", mode="w") as outF:
    outF.writelines(["'%s', " % item  for item in fieldsMap.values()])

with open("./DPDBT.Fields.out.csv", encoding="utf8", mode="w") as outF:
    outF.writelines(["'%s','%s'\n" % item  for item in fieldsMap.items()])    