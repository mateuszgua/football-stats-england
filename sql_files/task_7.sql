SELECT
Season, 
ROUND((AVG(HomeShots) + AVG(AwayShots)),2) AS AvgShots,
ROUND((AVG(HomeCorners) + AVG(AwayCorners)),2) AS AvgCorners,
ROUND((AVG(HomeFouls) + AVG(AwayFouls)),2) AS AvgFouls,
ROUND((AVG(HomeYellowCards) + AVG(AwayYellowCards)),2) AS AvgYellowCards,
ROUND((AVG(HomeRedCards) + AVG(AwayRedCards)),2) AS AvgResCards
FROM games
WHERE HomeShots != 9999 AND HomeCorners != 9999 AND HomeFouls != 9999 
    AND HomeYellowCards != 9999 AND HomeRedCards != 9999
GROUP BY Season
HAVING Season != 'Ses1899/1900'
ORDER BY Season;