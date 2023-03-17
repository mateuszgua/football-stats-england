SELECT
Season, 
(AVG(HomeShots) + AVG(AwayShots)) AS AvgShots,
(AVG(HomeCorners) + AVG(AwayCorners)) AS AvgCorners,
(AVG(HomeFouls) + AVG(AwayFouls)) AS AvgFouls,
(AVG(HomeYellowCards) + AVG(AwayYellowCards)) AS AvgYellowCards,
(AVG(HomeRedCards) + AVG(AwayRedCards)) AS AvgResCards
FROM games
WHERE HomeShots != 9999 AND HomeCorners != 9999 AND HomeFouls != 9999 
    AND HomeYellowCards != 9999 AND HomeRedCards != 9999
GROUP BY Season
HAVING Season != 'Ses1899/1900'
;