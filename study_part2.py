import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

query1 = '''
SELECT
	CustomerId,
	SUM(Total)
FROM
	Invoice
GROUP BY
	CustomerId
LIMIT 5
'''
result1 = cursor.execute(query1).fetchall()
print('Q1----------------')
print(result1)

query2 = '''
SELECT
	*
FROM
	Customer
WHERE (Country = 'USA')
LIMIT 5
'''
result2 = cursor.execute(query2).fetchall()
print('Q2----------------')
print(result2)

query3 = '''
SELECT
	EmployeeId,
	LastName,
	FirstName,
	Title,
	ReportsTo
FROM
	Employee
WHERE
	ReportsTo IS NULL;
'''
result3 = cursor.execute(query3).fetchall()
print('Q3----------------')
print(result3)

query4 = '''
SELECT
	COUNT(CustomerId)
FROM
	Customer;
'''
result4 = cursor.execute(query4).fetchall()
print('Q4----------------')
print(f'There are {result4[0]} unique customers.')

query5 = '''
SELECT
	COUNT(DISTINCT Composer)
FROM
	Track;
'''
result5 = cursor.execute(query5).fetchall()
print('Q5----------------')
print(f'There are {result5[0]} unique composers.')

query6 = '''
SELECT
	COUNT(*)
FROM
	Track;
'''
result6 = cursor.execute(query6).fetchall()
print('Q6----------------')
print(f'There are {result6[0]} rows in the Track table.')

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
# result = cursor.execute(query6).fetchall()
# print(f'Get the name of all Black Sabbath tracks and the albums they came from: {result}')