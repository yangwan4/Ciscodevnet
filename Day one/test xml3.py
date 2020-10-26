import xml.etree.ElementTree as XEET

devnet_eTree = XEET.parse("interfaces.xml")
collection = devnet_eTree.getroot()
print(collection.attrib)
print(type(collection.attrib))

interfaces = collection.findall("./*/interface/name")

for interface in interfaces:
    print("Interface is:", interface.text)