import requests
from secrets import SPOTIFY_TOKEN, USER_ID
import csv

class SpotifyFunctions:

    def __init__(self):
        self.SPOTIFY_TOKEN = SPOTIFY_TOKEN
        self.USER_ID = USER_ID

    def getPlaylists(self, limit=5):

        if(limit>50):
            print("Maximum playlist count is 50, please enter a number below it")
            return

        playlistDict = []
        getPlaylistUrl = 'https://api.spotify.com/v1/me/playlists?limit=' + str(limit)
        headers = {'Authorization' : 'Bearer ' + self.SPOTIFY_TOKEN}
        r = requests.get(getPlaylistUrl, headers=headers)
        print('Fetching Playlist and working magic'),
        for item in r.json()['items']:
            print('.'),
            #print('Playlist Name: ' + item['name'])
            trackList = self.getPlaylistsTracks(item['id'], item['name'])
            playlistDict.append({'name' : item['name'],
                                 'description': item['description'],
                                 'trackList' : trackList})
        print('Done')
        return playlistDict

    def writeToFile(self, playlistDict):
        f=open('backup.csv', "w+")
        print('Writing to CSV'),
        for item in playlistDict:
            print('.'),
            f.write(item['name'] + '|' + item['description'] + '|' + '%2C'.join(item['trackList']) + '\n')
        f.close()
        print('Done')



    def getPlaylistsTracks(self, playlistID, playlistName):
        tracklist = []
        getPlaylistTracksUrl = 'https://api.spotify.com/v1/playlists/' + playlistID + '/tracks'
        headers = {'Authorization' : 'Bearer ' + self.SPOTIFY_TOKEN}
        r = requests.get(getPlaylistTracksUrl, headers=headers)
        for i, item in enumerate(r.json()['items']):
            tracklist.append('spotify:track:' + item['track']['id'].encode("utf-8"))
        return tracklist

    def createPlaylist(self, name, description):
        print('Creating Playlist...'),
        createPlaylistUrl = 'https://api.spotify.com/v1/users/' + self.USER_ID + '/playlists'
        headers = {'Authorization' : 'Bearer ' + self.SPOTIFY_TOKEN}
        data = {'name': name, 'description': description}
        r = requests.post(createPlaylistUrl, json=data, headers=headers)
        print('Done')
        return r.json()['id']

    def addSongsToPlaylist(self, playlistID, tracklist):
        print('Adding Songs to Playlist...'),
        addTrackPlaylistUrl = 'https://api.spotify.com/v1/playlists/' + playlistID + '/tracks?uris=' + tracklist
        headers = {'Authorization' : 'Bearer ' + self.SPOTIFY_TOKEN}
        r = requests.post(addTrackPlaylistUrl, json='', headers=headers)
        print('Done')

    def parseCSVAndCreatePlaylist(self):
        with open('backup.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')
            for row in csv_reader:
                playlistID = self.createPlaylist(row[0], row[1])
                self.addSongsToPlaylist(playlistID=playlistID, tracklist=row[2])

if __name__ == '__main__':
    print('Backing up Playlists')
    cp = SpotifyFunctions()
    dict = cp.getPlaylists(32323)
    if(dict):
        cp.writeToFile(dict)

    #uncomment below if you want to create playlists from csv file
    #cp.parseCSVAndCreatePlaylist()
