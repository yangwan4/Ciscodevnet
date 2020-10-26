from xml.dom.minidom import parse

devnet_domTree = parse("interfaces02.xml")
collection = devnet_domTree.documentElement

ROW_intfs = collection.getElementsByTagName("ROW_intf")

for interface in ROW_intfs:
    print("Interface-name:" , interface.getElementsByTagName("intf-name")[0].firstChild.data)
    print("Layer2-Status:", interface.getElementsByTagName("proto-state")[0].firstChild.data, end=",")
    print("Layer1-Status:", interface.getElementsByTagName("link-state")[0].firstChild.data, end=",")
    print("Admin-Status", interface.getElementsByTagName("admin-state")[0].firstChild.data, end=",")
    print("IP-Address", interface.getElementsByTagName("prefix")[0].firstChild.data)