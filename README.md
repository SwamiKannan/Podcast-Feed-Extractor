# Podcast-Feed-Extractor
<p align="center">
  <img src="https://github.com/SwamiKannan/Podcast-Feed-Extractor/blob/main/cover.png" width=60%">
</p>

## Getting all your RSS feed addresses from your iTunes directory
This is a follow-up from my <a href="https://github.com/SwamiKannan/POD-IGY-for-Podcast-Summaries-using-Whisper-and-OpenAI"> POD-igy </a> repo.

I realized that there was no easy way to extract the RSS feeds from your podcast app. I use iTunes on my desktop for downloading my podcasts. So I created this repo that extracts the podcasts from your iTunes folder and provides you with the RSS feeds.

## Instructions:

1. Download this repo to your disk.
2. Open your command prompt and navigate to this repo
3. Enter the repo: <br />
   ```cd Podcast-Feed-Extractor```
   <br />
5. Install the requirements: <br />
  ```pip install -r requirements.txt```
6. Find the path to your iTunes folder. By default, on Windows, it is installed at <b>"C:\Users\<user>\Music\iTunes" </b>
7. Run this code: <br />
  ```python3 podcast.py <path of the iTunes folder as identified in step 5>```
8. The output files are as follows:
    1. A pickle file (podcast_feed.pkl) (if you want to load the dictionary { podcast_name : rss_feed} for further manipulation in python
    2. A text file (error_podcasts): A text file that contains the names of podcasts whose RSS feeds could not be identified
    3. A text file (rss_feeds): A text file that contains the name of podcasts and the RSS URL for each podcast

Sample output files are available in the <a href="https://github.com/SwamiKannan/Podcast-Feed-Extractor/tree/main/sample_output"> sample_outputs </a> folder
## Screenshots from command window
1. List of podcasts in the iTunes library
<img src="https://github.com/SwamiKannan/Podcast-Feed-Extractor/blob/main/sample_output/screenshots/podcast_list.png" align="center">
<br>
2. List of podcasts whose RSS feeds could not be extracted
<img src="https://github.com/SwamiKannan/Podcast-Feed-Extractor/blob/main/sample_output/screenshots/Errors_list.png" align="center">
<br>
3. List of podcasts with the url of the RSS feeds
<img src="https://github.com/SwamiKannan/Podcast-Feed-Extractor/blob/main/sample_output/screenshots/RSS-feeds.png" align="center">
<br>
