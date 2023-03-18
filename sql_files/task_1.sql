WITH result as (
    WITH g1 as (
    SELECT g.id, g.date, g.HomeTeam, g.AwayTeam, g.FullTimeResult, c.name
    FROM games g
    LEFT JOIN clubs c ON g.HomeTeam = c.id)
    SELECT g1.id, g1.date, g1.name as HomeTeam, c1.name as AwayTeam, g1.FullTimeResult, 
    CASE WHEN g1.FullTimeResult in ('H') THEN g1.name
    WHEN g1.FullTimeResult in ('A') THEN c1.name
    ELSE 'empty' END as Winner
    FROM g1
    LEFT JOIN
    clubs c1 ON g1.AwayTeam = c1.id
    )
SELECT r.Winner, COUNT(*) as win_games
FROM result r
WHERE r.Winner != 'empty'
GROUP BY r.Winner
ORDER BY win_games DESC
LIMIT 10;
