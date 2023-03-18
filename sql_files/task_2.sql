WITH result as (
    WITH points as (
        WITH g1 as
            (SELECT g.id, g.date, g.AwayTeam, g.FullTimeResult, c.name as HomeTeam
            FROM games g
            LEFT JOIN clubs c ON g.HomeTeam = c.id)
        SELECT g1.id, g1.date, g1.HomeTeam, c1.name as AwayTeam, g1.FullTimeResult,
        CASE WHEN g1.FullTimeResult in ('H') THEN 3
        WHEN g1.FullTimeResult in ('D') THEN 1
        ELSE 0 END as HomePoints,
        CASE WHEN g1.FullTimeResult in ('A') THEN 3
        WHEN g1.FullTimeResult in ('D') THEN 1
        ELSE 0 END as AwayPoints
        FROM g1
        LEFT JOIN clubs c1 ON g1.AwayTeam = c1.id
        WHERE g1.date > '1991-01-01'
        ORDER BY g1.date)
    (SELECT p.HomeTeam as Club, SUM(p.HomePoints) as Points
    FROM points p
    WHERE p.date > '2010-07-01' and p.date < '2011-07-01'
    GROUP BY p.HomeTeam)
    UNION ALL
    (SELECT p.AwayTeam as Club, SUM(p.AwayPoints) as Points
    FROM points p
    WHERE p.date > '2010-07-01' and p.date < '2011-07-01'
    GROUP BY p.AwayTeam))
SELECT r.Club, SUM(Points) as TotalPoints
FROM result r
GROUP BY r.Club
ORDER BY TotalPoints DESC
;