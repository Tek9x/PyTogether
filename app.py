# import xml.etree.ElementTree as ET
# import json
#
#
# tree = ET.parse('farms.xml')
# root = tree.getroot()
#
# def load_database():
#     try:
#         with open('events.db') as f:
#             db = json.load(f)
#             return db['Events']
#     except IOError:
#         print 'Could not find events.db'
#
# def load_event(event):
#     lst = []
#     try:
#         for item in load_database()[event]['Rewards']:
#             lst.append(item)
#         return lst
#     except KeyError:
#         print "no such event as " + event
#
# # def parse_xml():
# #     try:
# #         tree = ET.parse("farms.xml")
# #         return tree
# #     except IOError:
# #         print 'farms.xml not found'
#
# def create_tag():
#     print "No <Rewards> Tag Found, Creating one for you!"
#     root = tree.getroot()
#     root.append(ET.Element("Rewards"))
#     print 'Rewards Section Created Sucussfully'
#     save_file()
#
#
# def add_reward(r):
#     element = tree.find('Rewards')
#     Reward = ET.SubElement(element, "Reward")
#     Reward.set('id', r)
#     print 'Adding ' + str(r)
#
# def save_file():
#     tree.write('farms.xml')
#     print 'Saved'
#
# # if tree.find('Rewards') is None:
# #     create_tag()
# # elif tree.find('Rewards') is not None:
# #     for item in load_event("FishingContest"):
# #         add_reward(item)
# # save_file()
import untangle

obj = untangle.parse('farms.xml')

print obj.Farms.Farms.Farm['name']