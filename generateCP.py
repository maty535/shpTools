import xml.etree.ElementTree as ET
import uuid

tree = ET.parse("CPFields.Fmt.xml")
root = tree.getroot()
outF = open("./XXX-DPDBT.Fields.out.txt", encoding="utf8", mode="w")

seq1 = range(2,7)
for id in seq1:
    for fieldElement in list(root):
        fieldText =  ET.tostring(fieldElement ,encoding='unicode').format(id,str(uuid.uuid4()),id )
        outF.write(fieldText)
        outF.write('\n')
        
outF.close()        
 