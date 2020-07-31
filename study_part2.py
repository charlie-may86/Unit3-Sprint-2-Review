import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# 6. Get the name of all Black Sabbath tracks and the albums they came off of
query6 = '''
SELECT 
  alb.AlbumId,
  alb.Title AS AlbumTitle,
  art.Name AS ArtistName,
  trk.Name AS TrackName
FROM Album AS alb
JOIN Artist AS art ON alb.ArtistId = art.ArtistId
JOIN Track AS trk ON alb.AlbumId = trk.AlbumId
WHERE ArtistName LIKE 'Black Sabbath'
'''
result = cursor.execute(query6).fetchall()
print(f'Get the name of all Black Sabbath tracks and the albums they came from: {result}')