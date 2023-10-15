import os
import time
import requests
import pickle
import argparse
import xmltodict
import json
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument("path")

args = parser.parse_args()

if os.path.exists(args.path):
    podcast_path=args.path
else:
    print("The target directory doesn't exist")
    raise SystemExit(1)

library_path=podcast_path+'/iTunes Music Library.xml'

tree = ET.parse(library_path)
root = tree.getroot()
main_dict=root.findall('dict')
for item in list(main_dict[0]):    
    if item.tag=="dict":
        tracks_dict=item
        break
tracklist=list(tracks_dict.findall('dict'))

print(tracklist[0])

#podcast_path = 'F:\\iTunes'

# with open(os.path.join(podcast_path,'iTunes Music Library.xml'),'r', encoding='utf-8') as f:
#     file_pod=f.read()



# dict_pod=xmltodict.parse(file_pod)

# with open("sample.json", "w") as outfile:   
#     json.dump(dict_pod, outfile)

# print('JSON dumped')
# library_data = BeautifulSoup(xml_file, "xml")    

# podcast_deets=library_data.find_all('dict')
# podcast_deets.

# print('Podcast names',len(podcast_deets))

# print(type(podcast_deets))
# print(podcast_deets[0])

# for n,f in zip(podcast_names,podcast_feeds):
#     print(f'Name:{n}\tFeed:{f}')


# def get_feed(podcast_name: str):
#     received = False
#     title = podcast_name.replace(" ", "+")
#     link = 'https://itunes.apple.com/search?media=podcast&term=' + title
#     response = requests.get(link)
#     if 200 <= response.status_code < 300:
#         try:
#             feed = response.json()['results'][0]['feedUrl']
#             received = True
#         except IndexError:
#             print(f'No data received for {podcast_name}')
#             feed = podcast_name
#         except KeyError:
#             print(f'No feed received for {podcast_name}')
#             feed = podcast_name
#     else:
#         feed = podcast_name
#     return feed, received


# primary_dict = {}
# error_feed = []

# for file in os.listdir(podcast_path):
#     time_stamp = time.ctime(max(os.stat(root).st_mtime for root, _, _ in os.walk(podcast_path + '\\' + file)))
#     if time_stamp.split(" ")[-1] == '2023':
#         url_feed, received_flag = get_feed(file)
#         if received_flag:
#             primary_dict[file] = url_feed
#         else:
#             error_feed.append(url_feed)

# print('\n\nThe RSS feeds are as follows:')
# for key, value in primary_dict.items():
#     print(f'{key}:\t{value}')
# print('\n\nThe following podcasts did not have any RSS feed')
# for error in error_feed:
#     print(error)
# with open('podcast_feed.pkl','wb') as f:
#     pickle.dump(primary_dict,f,pickle.HIGHEST_PROTOCOL)
# with open('error_podcasts','w') as f:
#     f.write('\n'.join(error_feed))
