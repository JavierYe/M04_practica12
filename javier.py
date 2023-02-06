import xml.etree.ElementTree as ET
#Construim estructura XML
#root
p = ET.Element("students")
#child de root
c = ET.SubElement(p,"student")
#child de student
s = ET.SubElement(c,"name")
#text de elemnet
s.text="Javier"
s1 = ET.SubElement(c,"surname")
s1.text="Ye"
s2 = ET.SubElement(c,"email")
s2.text="javier@gmail.com"
s3 = ET.SubElement(c,"dni")
s3.text="11111111y"
#para añadir el atrivut
element = p[0]
element.set("nom","javier")
c1 = ET.SubElement(p,"student")
ss = ET.SubElement(c1,"name")
ss.text="Boou"
ss1 = ET.SubElement(c1,"surname")
ss1.text="Ye"
ss2 = ET.SubElement(c1,"email")
ss2.text="Boou@gmail.com"
ss3 = ET.SubElement(c1,"dni")
ss3.text="22222222y"
element = p[1]
element.set("nom","Boou")
c2 = ET.SubElement(p,"student")
sss = ET.SubElement(c2,"name")
sss.text="Jordi"
sss1 = ET.SubElement(c2,"surname")
sss1.text="Ye"
sss2 = ET.SubElement(c2,"email")
sss2.text="Jordi@gmail.com"
sss3 = ET.SubElement(c2,"dni")
sss3.text="33333333y"
element = p[2]
element.set("nom","Jordi")
c3 = ET.SubElement(p,"student")
ssss = ET.SubElement(c3,"name")
ssss.text="Nico"
ssss1 = ET.SubElement(c3,"surname")
ssss1.text="Ye"
ssss2 = ET.SubElement(c3,"email")
ssss2.text="Nico@gmail.com"
ssss3 = ET.SubElement(c3,"dni")
ssss3.text="44444444y"
element = p[3]
element.set("nom","Nico")
c4 = ET.SubElement(p,"student")
sssss = ET.SubElement(c4,"name")
sssss.text="Raul"
sssss1 = ET.SubElement(c4,"surname")
sssss1.text="Ye"
sssss2 = ET.SubElement(c4,"email")
sssss2.text="Raul@gmail.com"
sssss3 = ET.SubElement(c4,"dni")
sssss3.text="55555555y"
element = p[4]
element.set("nom","Raul")
#Escriure com queda el ducument XML en un arxiu (o el mateix arxiu)
tree = ET.ElementTree(p)
tree.write("javier.xml")
#indentem
ET.indent(p)
#mostra console
ET.dump(p)
#indentacio dels elements
ET.indent(tree)
