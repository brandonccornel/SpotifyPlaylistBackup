# SpotifyPlaylistBackup

Made a thing to backup playlists (max num is 50) to a CSV file with a proprietary delimiter

Flow:
1. Fetch all playlists and their tracks
2. Write each playlist and it's tracks to a CSV

parseCSVAndCreatePlaylist actually creates playlist and adds songs to them using backup.csv
