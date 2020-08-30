import argparse
import os
import re

from mutagen.easyid3 import EasyID3

import youtube_dl

parser = argparse.ArgumentParser(prog='download_songs', 
    usage='Please provide a link to a song or playlist with the --input-url flag e.g. python download_songs.py --url https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
    description='This script will download a song and convert it to mp3! It is recommended that the songs are removed from the downloaded_songs/ directory after they have been downloaded to prevent reprocessing.')

parser.add_argument('--url', required=True)

# TODO: Use https://github.com/willmcgugan/rich to add progress bars.

def hook(c):
    if c['status'] == 'finished':
        print('Finished downloading. Converting...')

if __name__ == '__main__':
    args = parser.parse_args()

    output_directory = 'downloaded_songs/'

    print('***')
    print(parser.description)
    print('***')

    output_name_template = output_directory + '%(title)s.%(ext)s'

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_name_template,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
            {
                'key': 'FFmpegMetadata'
            }
        ],
        'progress_hooks': [hook]
    }

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.url])

for file in os.listdir(output_directory):

    id3 = EasyID3(os.path.join(output_directory, file))

    title = id3['title'][0]

    groups = re.split('\s*[-|]\s*', title)

    artist = groups[0]

    if len(groups) == 1:
        print(f'Failed to extract proper metadata from {file} or it\'s already in the correct format. Skipping...')
        continue

    print(f'Updating metadata for {file}..')

    print(f'Current song title: {title}')

    print(f'Artist: {artist}')

    id3['artist'] = artist

    song_title = groups[1]

    title_groups = re.split('\s*[\(\[]\s*', song_title)

    if len(title_groups) > 1 and all(x not in str.lower(title_groups[1]) for x in['remix','mix','club','edit','version']):
        song_title = title_groups[0]

    id3['title'] = song_title

    print(f'Song Title: {song_title}')

    id3.save()

print('Finished.')
