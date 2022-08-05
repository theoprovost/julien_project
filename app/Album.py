from app import utils

import os


class Album():
    def __init__(self, artist: str = None) -> None:
        self.artist = artist
        self.DATA_STORAGE_PATH = self.getDataPath(self.artist)

        if os.path.exists(self.DATA_STORAGE_PATH):
            self.data = utils.loadData(self.DATA_STORAGE_PATH)
        else:
            self.data = None

    def getDataPath(self, artist: str):
        filename = artist + '.json' if artist else ''
        return os.path.join('./app/data/albums', filename)

    def getIndex(self, key, value):
        for i, data in enumerate(self.data):
            if data[key].lower() == value.lower():
                return i

    def getAllByArtist(self):
        ''' TO DO : add sorting order '''
        return {
            'message': '',
            'data': self.data if self.data else None,
            'n': len(self.data) if not isinstance(self.data, bool) > 0 else 0
        }

    def addOne(self, new_data: dict):
        ''' TO DO : enforce schema '''
        if self.data:
            self.data.append(new_data)
            new_data = self.data
        else:
            new_data = [new_data]

        utils.storeAsJson(new_data, self.DATA_STORAGE_PATH)

        return {
            'message': f'The album has been added.',
            'data': new_data,
            'n': len(new_data)
        }

    def getOne(self, album_name: str):
        index = self.getIndex('album_title', album_name)
        return self.data[index]

    def deleteOne(self, album_name: str):
        index = self.getIndex('album_title', album_name)
        if index:
            del self.data[index]
            utils.storeAsJson(self.data, self.DATA_STORAGE_PATH)
            message = f'The album "{album_name}" has been deleted.'
        else:
            message = f'No album "{album_name}" has been found in our records.'

        return {
            'message': message,
            'data': None,
            'n': 0,
        }

    def modifyOne(self, album_name: str, new_data: dict):
        index = self.getIndex('album_title', album_name)
        if index or index == 0:
            self.data[index] = new_data
            utils.storeAsJson(self.data, self.DATA_STORAGE_PATH)
            message = f'The album "{album_name}" has been modified.'

        else:
            message = f'No album "{album_name}" has been found in our records.'

        return {
            'message': message,
            'data': new_data,
            'n': len(new_data)
        }
