import os
import time
import requests
import pickle

podcast_path = 'F:\\iTunes\\iTunes Media\\Podcasts'


def get_feed(podcast_name: str):
    received = False
    title = podcast_name.replace(" ", "+")
    link = 'https://itunes.apple.com/search?media=podcast&term=' + title
    response = requests.get(link)
    if 200 <= response.status_code < 300:
        try:
            feed = response.json()['results'][0]['feedUrl']
            received = True
        except IndexError:
            print(f'No data received for {podcast_name}')
            feed = podcast_name
        except KeyError:
            print(f'No feed received for {podcast_name}')
            feed = podcast_name
    else:
        feed = podcast_name
    return feed, received


primary_dict = {}
error_feed = []

for file in os.listdir(podcast_path):
    time_stamp = time.ctime(max(os.stat(root).st_mtime for root, _, _ in os.walk(podcast_path + '\\' + file)))
    if time_stamp.split(" ")[-1] == '2023':
        url_feed, received_flag = get_feed(file)
        if received_flag:
            primary_dict[file] = url_feed
        else:
            error_feed.append(url_feed)

print(error_feed)
with open('podcast_feed.pkl','wb') as f:
    pickle.dump(primary_dict,f,pickle.HIGHEST_PROTOCOL)
with open('error_podcasts','w') as f:
    f.write('\n'.join(error_feed))
