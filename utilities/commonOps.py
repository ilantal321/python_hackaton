
import xml.etree.ElementTree as ET

def get_data(node_name):
    root = ET.parse('D:/python_hackaton2/utilities/configuration.xml').getroot()
    return root.find(".//" + node_name).text