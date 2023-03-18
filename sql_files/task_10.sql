SELECT r.name, (SUM(g.HomeYellowCards) + SUM(g.AwayYellowCards)) as YellowCards 
FROM games g
LEFT JOIN referee r ON g.Referee = r.id
GROUP BY r.name
HAVING r.name != 9999
ORDER BY YellowCards DESC
LIMIT 15;