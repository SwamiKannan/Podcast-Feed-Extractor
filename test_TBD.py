import json
import os
import xml.etree.ElementTree as ET

podcast_path='F:/iTunes'

library_path=podcast_path+'/iTunes Music Library.xml'
podcast_names_list=[]
tree = ET.parse(library_path)
root = tree.getroot()
main_dict=root.findall('dict')
for item in list(main_dict[0]):    
    if item.tag=="dict":
        tracks_dict=item
        break
tracklist=list(tracks_dict.findall('dict'))
for track in tracklist:
    x=list(track)
    for i in range(len(x)):
        if x[i].text=='Album':
            podcast_names_list.append(x[i+1].text)
print(set(podcast_names_list))


# podcast=[]
# for item in tracklist:
#     x=list(item)
#     for i in range(len(x)):
#         if x[i].text=="Genre" and x[i+1].text=="Podcast": #          
#             podcast.append(list(item))
# print('Podcast',podcast)