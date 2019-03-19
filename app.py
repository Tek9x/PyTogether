import xml.etree.ElementTree as ET
import json

with open('events.db') as f:
    db = json.load(f)

Easter = db['Events']['Easter']['Rewards']

tree = ET.parse("farms.xml")
root = tree.getroot()
element = tree.find('Rewards')


def check_exists():
    if tree.find('Rewards') is None:
        return False


def add_reward(r):
    Reward = ET.SubElement(element, "Reward")
    Reward.set('id', r)
    return 'Adding ' + str(r)


def save_file():
    tree.write('farms.xml')
    return 'Saved'


if check_exists() is False:
    print "No <Rewards> Tag Found, Creating one for you!"
    root.append(ET.Element("Rewards"))
    for item in Easter:
        print add_reward(item)
else:
    for items in Easter:
        print add_reward(items)
save_file()




