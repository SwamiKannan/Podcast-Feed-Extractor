import xml.etree.ElementTree as ET
import requests
import pickle

podcast_path = 'F:/iTunes'


def get_names(podcast_path: str) -> list:
    library_path = podcast_path+'/iTunes Music Library.xml'
    tree = ET.parse(library_path)
    root = tree.getroot()
    main_dict = root.findall('dict')

    podcast_names = []
    for item in list(main_dict[0]):
        if item.tag == "dict":
            tracks_dict = item
            break
    tracklist = list(tracks_dict.findall('dict'))
    itunes_u_count = 0
    for track in tracklist:
        x = list(track)
        content = [y.text for y in x]
        if 'Podcast' in content:
            if 'Album' in content:
                index_album = content.index('Album')
                name = content[index_album+1]
                podcast_names.append(name)
            elif 'Location' in content:
                index_loc = content.index('Location')
                name = content[index_loc+1]
                if 'https://itunesu.itunes.apple.com' in name:
                    itunes_u_count += 1
                else:
                    print('Album not found')
            else:
                print('Album not found\n')

    final_content = list(set(podcast_names))
    if itunes_u_count > 0:
        print(f'{itunes_u_count} {"entries" if itunes_u_count>1 else "entry"} pertaining to iTunes University found. iTunes university is no longer functional\n\n')
    print(f'{len(final_content)} valid podcasts found:\n')
    for i, name in enumerate(final_content):
        print(f'{i+1}.\t{name}')
    return final_content


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


def get_all_feeds(podcast_path: str):
    primary_dict = {}
    error_feed = []
    pod_names = get_names(podcast_path)
    for name in pod_names:
        url_feed, received_flag = get_feed(name)
        if received_flag:
            primary_dict[name] = url_feed
    else:
        error_feed.append(url_feed)
    print('\n\nThe RSS feeds are as follows:')
    for key, value in primary_dict.items():
        print(f'{key}:\t{value}')
    print('\n\nThe following podcasts did not have any RSS feed')
    for error in error_feed:
        print(error)
    with open('podcast_feed.pkl', 'wb') as f:
        pickle.dump(primary_dict, f, pickle.HIGHEST_PROTOCOL)
    with open('error_podcasts', 'w') as f:
        f.write('\n'.join(error_feed))
    return primary_dict
