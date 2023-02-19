from __future__ import unicode_literals
import youtube_dl
import argparse
import time
import os

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', type=str,
                        help='path to audiofile')
    return parser.parse_args()

def download_video(title, url):
    ydl_opts = {'outtmpl': f'{title}.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    args = get_arguments()
    start = time.time()
    download_video('tmp',args.url)
    end = time.time()
    print(f'elapsed downloading time: {end - start}')