import app.utils as utils

from bs4 import BeautifulSoup

import datetime
import os


class WebScraper():
    def __init__(self) -> None:
        self.BASE_URL = 'https://www.allformusic.fr'
        self.DATA_STORAGE_PATHS = {
            'albums': './app/data/albums',
            'repositories': './app/data/repositories'
        }

    def makeSoup(self, url: str):
        ''' Generic function to retrieve the BS parsed response (HTML) of a given URL. '''
        html = utils.fetch(url)
        if html:
            return BeautifulSoup(html, 'html.parser')
        else:
            return False

    def scrapAlbumListByArtistName(self, artist_name: str):
        ''' Scraps and store albums infos based on provided artist name.

        NB :
        - implies that the given name exists, otherwise nothing will be returned (no checks atm). '''
        URL = os.path.join(self.BASE_URL, artist_name, 'discographie')
        soup = self.makeSoup(URL)

        if soup:
            html_body = soup.body
            parent_el = html_body.find('article', {'id': 'disco-album'})
            album_els = parent_el.find_all('li')

            # NB : not robust, may need to catch DOM's related not found
            data = [{
                'artist_name': artist_name,
                # HTTP URL pointing to the album's cover
                'cover_src': album_el.find('img')['src'],
                # The album title
                'album_title': album_el.find('strong').text,
                # The album's date of released
                'album_dor': album_el.find('span').text,
                'status': {
                    'available': True,
                    'infos': {
                        'borrower_name': None,
                        'borrower_dt': None
                    },
                    'history': []
                },
                'metadata': {
                    'created_at': str(datetime.datetime.now()),
                    'updated_at': None
                }
            } for album_el in album_els]

            if len(data) > 0:
                filename = artist_name + '.json'
                path = os.path.join(
                    self.DATA_STORAGE_PATHS['albums'], filename)
                utils.storeAsJson(data, path)
                print(
                    f'- A total of {len(data)} album(s) have been found for : "{artist_name.capitalize()}".')
                return data
            else:
                return False

        else:
            print(f'- No album found for "{artist_name.capitalize()}".')
            return False
