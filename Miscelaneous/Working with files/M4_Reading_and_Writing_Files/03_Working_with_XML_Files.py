import xml.etree.ElementTree as ET


def parse_xml_et(file_name: str):
    tree = ET.parse(file_name)
    root = tree.getroot()
    print(f"Domains for: {root.attrib["name"]}")
    for child in root:
        print(f"\t{child.attrib["name"]} {child.tag}")


def add_xml_element_et(file_name: str, el: str, attr: str, val: str) -> None:
    tree = ET.parse(file_name)
    root = tree.getroot()
    child = ET.Element(el)
    child.attrib[attr] = val
    root.append(child)
    tree.write(file_name)


def change_xml_element_et(file_name: str, el: str, attr: str, old_value: str, new_value: str) -> None:
    tree = ET.parse(file_name)
    root = tree.getroot()
    child = root.find(f"./{el}[@{attr}='{old_value}']")
    child.attrib[attr] = new_value
    tree.write(file_name)


parse_xml_et("../files_to_read/ef_author.xml")
# Domains for: Israel Mendoza
# 	Azure domain
# 	AWS domain
# 	.NET domain
# 	Python domain

add_xml_element_et("../files_to_read/ef_author.xml", "domain", "name", "Java")
parse_xml_et("../files_to_read/ef_author.xml")
# Domains for: Israel Mendoza
# 	Azure domain
# 	AWS domain
# 	.NET domain
# 	Python domain
# 	Java domain

change_xml_element_et("../files_to_read/ef_author.xml", "domain", "name", "Java", "Golang")
parse_xml_et("../files_to_read/ef_author.xml")
# Domains for: Israel Mendoza
# 	Azure domain
# 	AWS domain
# 	.NET domain
# 	Python domain
# 	Golang domain
