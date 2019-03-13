import xml.etree.ElementTree as ET
from content_management import easter, hauntedharvest, starryharvest, fishingcontent, sweettoothfestival, valentines, \
    summer, soltice, musicfestival, archaeology, hanami, patricks
from file_handler import decompress, compress

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


def itemcollection():
    collection = []
    for n in easter() + hauntedharvest() + sweettoothfestival() + starryharvest() + valentines() + fishingcontent() + summer() + soltice() + musicfestival() + archaeology() + hanami() + patricks():
        collection.append(n)
    return collection


if check_exists() is False:
    print "No <Rewards> Tag Found, Creating one for you!"
    root.append(ET.Element("Rewards"))
    for items in itemcollection():
        print add_reward(items)
else:
    for items in itemcollection():
        print add_reward(items)
save_file()

# test = tree.findall('Rewards/Reward')
#
# list = []
# for n in test:
#    p = n.attrib['id']
#    list.append(p)
# print len(list)