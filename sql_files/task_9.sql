SELECT r.name, COUNT(*) as NumberGames
FROM games g
LEFT JOIN referee r ON g.Referee = r.id
GROUP BY r.name 
HAVING r.name != 9999 
ORDER BY NumberGames DESC
LIMIT 10;