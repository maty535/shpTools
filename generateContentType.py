import xml.etree.ElementTree as ET
tree = ET.parse("Fields.Elements.xml")
root = tree.getroot()

fieldsMap = {}
outF = open("./DPDBT.FieldsRefs.out.txt", encoding="utf8", mode="w")
outF1 = open("./DPDBT.FieldsName.out.txt", encoding="utf8", mode="w")
outF2 = open("./DPDBT.FieldsDisplayName.out.txt", encoding="utf8", mode="w")
for field in list(root):
    required    = "FALSE"
    try:
        required = field.attrib['Required'] 
    except:
        required    = "FALSE"
    
    fieldRefFmt  = """<FieldRef ID="{}" Name="{}"   DisplayName="{}" Required="{}"/>\n"""
    fieldRef = fieldRefFmt.format( field.attrib['ID'], 
                                  field.attrib['Name'],
                                  field.attrib['DisplayName'],
                                  required)
    outF.write(fieldRef)    
    outF1.write("{}\n".format(field.attrib['Name']))
    outF2.write("{}\n".format(field.attrib['DisplayName']))

outF.close()
outF1.close()
outF2.close()