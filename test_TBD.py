import json
import os
import xml.etree.ElementTree as ET

podcast_path='F:/iTunes'

library_path=podcast_path+'/iTunes Music Library.xml'
podcast_names_list=[]
tree = ET.parse(library_path)
root = tree.getroot()
main_dict=root.findall('dict')

podcast_names=[]
for item in list(main_dict[0]):    
    if item.tag=="dict":
        tracks_dict=item
        break
tracklist=list(tracks_dict.findall('dict'))
itunes_u_count=0
for track in tracklist:
    x=list(track)
    content=[y.text for y in x]
    if 'Podcast' in content:
        if 'Album' in content:
            index_album=content.index('Album')
            name=content[index_album+1]
            podcast_names.append(name)
        elif 'Location' in content:
            index_loc=content.index('Location')
            name=content[index_loc+1]
            if 'https://itunesu.itunes.apple.com' in name:
                itunes_u_count+=1
                print('iTunes university')
            else:
                print('Album not found')
        else:
            print('Album not found\n')           

final_content=list(set(podcast_names))
if itunes_u_count>0:
    print(f'{itunes_u_count} {"entries" if itunes_u_count>1 else "entry"} pertaining to iTunes University found. iTunes university is no longer functional\n\n')
print(f'{len(final_content)} valid podcasts found')     
for i,name in enumerate(final_content):
    print(f'{i+1}.\t{name}')

#         if x[i].text=='Album':
#             podcast_names_list.append(x[i+1].text)
# print(set(podcast_names_list))


# podcast=[]
# for item in tracklist:
#     x=list(item)
#     for i in range(len(x)):
#         if x[i].text=="Genre" and x[i+1].text=="Podcast": #          
#             podcast.append(list(item))
# print('Podcast',podcast)