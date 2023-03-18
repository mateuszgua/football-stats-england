SELECT Season, COUNT(FullTimeResult) as Number
FROM games
WHERE FullTimeResult = 'D'
GROUP BY Season
ORDER BY Season;