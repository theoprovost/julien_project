from app import etl
from app.Album import Album
from app.User import User

import argparse
import pprint
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('--i', required=False, action='store_true')
    args = parser.parse_args()

    scraper = etl.WebScraper()
    pp = pprint.PrettyPrinter(width=41, compact=True)

    # Interactive mode
    if args.i:
        N_ARTIST = 1
        print(f'Please choose {N_ARTIST} artist(s) : \n')

        i = 0
        while i < N_ARTIST:
            artist_input = input(f'Artist ({i + 1}/{N_ARTIST}) : ')
            if scraper.scrapAlbumListByArtistName(artist_input):
                i += 1

            if i:
                album = Album(artist_input)

                print_all_data_input = input(
                    'Would you like to print all albums data (y/n) ? ')
                if print_all_data_input == 'y':
                    data = album.getAllByArtist()
                    print('\n')
                    pp.pprint(data)

                add_one_input = input(
                    '\nWould you like to add your own data ? (y/n) ')
                if add_one_input == 'y':
                    def collectAlbumInfos():
                        return {
                            'artist_name': artist_input,
                            'album_title': input('What is the name of the album ? '),
                            'album_dor': input('When was released this album ? '),
                            'cover_src': input(
                                'Do you have any source for it\'s cover ? '),
                        }

                    data = collectAlbumInfos()
                    tmp_title = data['album_title']
                    res = album.addOne(data)
                    print(res['message'])

                    modify_one_input = input(
                        '\nWould you like to modify this album (y/n) ? ')
                    if modify_one_input == 'y':
                        data = collectAlbumInfos()
                        res = album.modifyOne(tmp_title, data)
                        tmp_title = data['album_title']
                        print(res['message'])

                    delete_one_input = input(
                        '\nIf there is any error at this step, you can still delete the newly added album. Would you like to processed ? (y/n) ')
                    if delete_one_input == 'y':
                        res = album.deleteOne(tmp_title)
                        print(res['message'])

                else:
                    username_input = input('What is your username ? ')
                    user = User(username_input)
                    artist_input = input('Please type the artist\'s name : ')
                    album = Album(artist_input)

                    if album.data:
                        albums = [a['album_title'] for a in album.data]
                        print(
                            f'A total of {len(albums)} album(s) are available.')
                        print_opts_input = input(
                            'Would you like to print your options (y/n) ? ')
                        if print_opts_input == 'y':
                            for a in albums:
                                print(f'- {a}')

                        album_input = input('Please type an album : ')
                        if album_input in albums:
                            album_data = album.getOne(album_input)
                            if user.borrowAlbum(album_data):
                                print(
                                    f'You just borrowed "{album_input}" from "{artist_input}".')
                                undo_input = input(
                                    'Would you like to undo the last action (y/n) ? ')
                                if undo_input == 'y':
                                    if user.returnAlbum(album_data):
                                        print(
                                            f'You just returned "{album_input}" from "{artist_input}".')
                                    else:
                                        print(
                                            f'You\'re not currently renting "{album_input}", you can\'t return it.')

                            else:
                                print(
                                    f'The album "{album_input}" is not available for now.')
                        else:
                            print(
                                f'The album "{album_input}" of "{artist_input}" is unknown.')

                    else:
                        print(
                            f'No artist named "{artist_input}" in our records.')

    else:
        print('Only the interactive mode is enabled for now. Please restart the command with the --i parameter.')
        sys.exit()
