import eyed3
import sys
import logging

NAME = 'mp3'


def filter_function(file_meta):
    if file_meta['mime'] == 'audio/mpeg':
        try:
            mp3_meta = _get_mp3_meta(file_meta)
            if mp3_meta:
                file_meta['name'] = '{}/{}/{}.mp3'.format(mp3_meta['album_artist'], mp3_meta['album'], mp3_meta['title'])
        except Exception as e:
            logging.error('Could not read meta {}: {} - {} '.format(file_meta['path'], sys.exc_info()[0].__name__, e))


def setup(app):
    app.register_plugin(NAME, filter_function)


def _get_mp3_meta(file_meta):
    try:
        mp3_file = eyed3.load(file_meta['path'])
    except Exception as e:
        logging.error('Could not read meta {}: {} - {} '.format(file_meta['path'], sys.exc_info()[0].__name__, e))
        return None
    else:
        meta = dict()
        meta['album_artist'] = mp3_file.tag.album_artist
        meta['album'] = mp3_file.tag.album
        meta['title'] = mp3_file.tag.title
        _set_none_existing_meta(meta, file_meta['name'])
        return meta


def _set_none_existing_meta(meta, original_name):
    if meta['album_artist'] is None:
        meta['album_artist'] = 'unknown'
    if meta['album'] is None:
        meta['album'] = 'unknown'
    if meta['title'] is None:
        meta['title'] = original_name.replace('.mp3', '')
