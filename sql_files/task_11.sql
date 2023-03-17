WITH result as (
    WITH all_games as (
        SELECT g.Season, r.name, (SUM(HomeRedCards) + SUM(AwayRedCards)) as RedCards 
        FROM games g
        LEFT JOIN referee r ON g.Referee = r.id
        GROUP BY g.Season, r.name 
        HAVING r.name != 9999
        ORDER BY g.Season, RedCards DESC)
    SELECT * ,
    RANK () OVER(PARTITION BY ag.Season ORDER BY RedCards DESC) AS RedCardsRank 
    FROM all_games ag)
SELECT r.Season, r.name, r.RedCards
FROM result r
WHERE RedCardsRank = 1;