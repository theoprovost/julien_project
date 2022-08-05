import app.utils as utils
from app.Album import Album

import os
import datetime


class User():
    def __init__(self, username) -> None:
        self.data = self.getUserDetails(username)

    def getUserDetails(self, username: str):
        filename = username + '.json'
        path = os.path.join('./app/data/users', filename)

        data = utils.loadData(path)
        if not data:
            data = {
                'username': username,
                'metadata': {
                    'created_at': str(datetime.datetime.now()),
                    'updated_at': None
                }
            }
            utils.storeAsJson(data, path)

        return data

    def borrowAlbum(self, album: str):
        if album['status']['available']:
            album['status']['available'] = False
            album['status']['infos'] = {
                'borrower_name':  self.data['username'],
                'borrower_dt': str(
                    datetime.datetime.now())
            }
            Album(album['artist_name']).modifyOne(album['album_title'], album)
            return True
        else:
            return False

    def returnAlbum(self, album: str):
        if album['status']['infos']['borrower_name'] != self.data['username']:
            return False

        album['status']['available'] = True
        album['status']['history'].append(album['status']['infos'])
        album['status']['infos'] = {
            'borrower_name':  None,
            'borrower_dt': None
        }

        Album(album['artist_name']).modifyOne(album['album_title'], album)
        return True
