import xml.etree.ElementTree as ET
import requests
import pickle
import os

podcast_path = 'F:/iTunes'


def get_names(podcast_path: str) -> list:
    '''
    Extracts the names of all the podcasts as per the "Album" name in the iTunes Music Library.xml file.
    Args:
        podcast_path: The path to the iTunes folder
    Returns:
        final_content (list): A list of all the podcasts that are/were not part of iTunes University (which has been stopped)
    '''
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
    '''
    Takes the podcast name, queries the iTunes server and returns the RSS feed address if available
    Args:
        podcast_name: Name of the podcast as per the iTunes Music Library.xml file
    Returns:
        received (bool): A flag that states whether the rss feed was retrieved or not
        feed (str): the RSS feed url if the received flag is True else the podcast_name itself
    '''
    received = False
    title = podcast_name.replace(" ", "+")
    link = 'https://itunes.apple.com/search?media=podcast&term=' + title
    response = requests.get(link)
    if 200 <= response.status_code < 300:
        try:
            feed = response.json()['results'][0]['feedUrl']
            received = True
        except IndexError:
            feed = podcast_name
        except KeyError:
            feed = podcast_name
    else:
        feed = podcast_name
    return feed, received


def get_all_feeds(podcast_path: str, output_dir_avail: bool):
    '''
    Calls get_names() to get the list of all podcast names
    For each podcast name, retrieves the url/podcast_name and status of retrieval
        if retrieval is a success, adds the data to a dictionary as {name of podcast: rss feed url}
        else appends podcast name to a list
    Writes the following to disk (if output folder is available, write files to output folder else writes to the main folder)
        podcast_feed.pkl: A pickle file that writes the dictionary created for successful retrieval
        error_podcasts: list of podcasts whose RSS file could not be extracted
        rss_feeds: Clear text version of podcast_feed.pkl
    Args:
        podcast_path: Path of the iTunes folder
        output_dir_available: if the 'output' folder has been created / exists or not
    Returns:
        primary_dict (dict): {name of podcast: rss feed url}
        feed (str): 
    '''
    primary_dict = {}
    error_feed = []
    pod_names = get_names(podcast_path)
    for name in pod_names:
        url_feed, received_flag = get_feed(name)
        if received_flag:
            primary_dict[name] = url_feed
        else:
            error_feed.append(url_feed)
    # print('\n\nThe RSS feeds are as follows:')
    # for key, value in primary_dict.items():
    #     print(f'{key}:\t{value}')
    print('\n\nThe following podcasts did not have any RSS feed')
    for error in error_feed:
        print(error)
    path = os.path.join('output') if output_dir_avail else os.getcwd()
    with open(os.path.join(path, 'podcast_feed.pkl'), 'wb') as f:
        pickle.dump(primary_dict, f, pickle.HIGHEST_PROTOCOL)
    with open(os.path.join(path, 'error_podcasts'), 'w') as f:
        f.write('\n'.join(error_feed))
    rss_list = []
    for k, v in primary_dict.items():
        rss_list.append(f'{k}:\t{v}')
    with open(os.path.join(path, 'rss_feeds'), 'w') as f:
        f.write('\n'.join(rss_list))

    return primary_dict
