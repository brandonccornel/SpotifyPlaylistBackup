# SpotifyPlaylistBackup

Written in Python 2

Made a thing to backup playlists (max num is 50) to a CSV file with a proprietary delimiter

To get the OAUTH Token:
1. Create an application here https://developer.spotify.com/dashboard/
2. Request OAuth Token here by clicking "Get Token" with the below scopes https://developer.spotify.com/console/get-current-user/
  *user-read-private
  *user-read-email
  *playlist-read-private
  *playlist-read-collaborative
  *playist-modify-public
  *playlist-modify-private
3. Paste token in secrets.py SPOTIFY_TOKEN
4. While still on the same page "Get Current User's Profile", click "Try it". The response should give your user ID which will be in numeric form
5. Paste that number in the secrets.py USER_ID
