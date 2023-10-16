import os
import argparse
from utils import get_all_feeds


parser = argparse.ArgumentParser()
parser.add_argument("path")

if 'output' in os.listdir():
    output_dir = True
else:
    try:
        os.makedirs('output')
    except Exception as e:
        output_dir = False
        print('Output directory not created. Created output documents will be stored in the main directory')
        print(e)

args = parser.parse_args()

if os.path.exists(args.path):
    podcast_path = args.path
else:
    print("The target directory doesn't exist")
    raise SystemExit(1)


def __main__():
    podcast_feeds = get_all_feeds(podcast_path, output_dir)
    for i, (k, v) in enumerate(podcast_feeds.items()):
        print(f'{i}.\t{k}:{v}')


if __name__ == "__main__":
    __main__()
