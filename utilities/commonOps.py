
import xml.etree.ElementTree as ET

def get_data(node_name):
    root = ET.parse('C:/Users/dolev/PycharmProjects/python_hackaton_project/utilities/configuration.xml').getroot()
    return root.find(".//" + node_name).text