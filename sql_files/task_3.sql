WITH total_games as 
    ((SELECT c.name, g.id as HomeGame, g.date as HomeGameDay
        FROM clubs c
        LEFT JOIN games g ON c.id = g.HomeTeam
        WHERE g.date > '1901-01-01'
        ORDER BY g.date)
    UNION
    (SELECT c.name, g.id as AwayGame, g.date as AwayGameDay 
        FROM clubs c
        LEFT JOIN games g ON c.id = g.AwayTeam
        WHERE g.date > '1901-01-01' 
        ORDER BY g.date))
SELECT tg.name, COUNT(*) as NumberGames
FROM total_games as tg
GROUP BY tg.name
ORDER BY NumberGames DESC
LIMIT 15;