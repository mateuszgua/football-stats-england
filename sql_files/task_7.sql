SELECT 
Season,
ROUND((AVG(HomeShots) + AVG(AwayShots)),2) AS AvgShots,
ROUND((AVG(HomeCorners) + AVG(AwayCorners)),2) AS AvgCorners,
ROUND((AVG(HomeFouls) + AVG(AwayFouls)),2) AS AvgFouls,
ROUND((AVG(HomeYellowCards) + AVG(AwayYellowCards)),2) AS AvgYellowCards,
ROUND((AVG(HomeRedCards) + AVG(AwayRedCards)),2) AS AvgResCards
FROM games
GROUP BY Season
HAVING Season != 'Ses1899/1900'
ORDER BY Season
;