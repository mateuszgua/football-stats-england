WITH total_rank as (
    WITH get_rank as (
        WITH result as (
            WITH part_points as(
                SELECT g.*,
                c.name as HomeTeamName, c1.name as AwayTeamName,
                CASE WHEN g.FullTimeResult in ('H') THEN 3
                WHEN g.FullTimeResult in ('D') THEN 1
                ELSE 0 END as HomePoints,
                CASE WHEN g.FullTimeResult in ('A') THEN 3
                WHEN g.FullTimeResult in ('D') THEN 1
                ELSE 0 END as AwayPoints   
                FROM games g
                LEFT JOIN clubs c ON g.HomeTeam = c.id
                LEFT JOIN clubs c1 ON g.AwayTeam = c1.id)
                (SELECT pp.Season, pp.HomeTeamName as Club, 
                SUM(pp.HomePoints) as Points,
                SUM(pp.FullTimeHomeGoals) as Goals,
                SUM(pp.HomeFouls) as Fouls,
                SUM(pp.HomeCorners) as Corners,
                SUM(pp.HomeYellowCards) as YellowCards,
                SUM(pp.HomeRedCards) as RedCards
                FROM part_points as pp
                GROUP BY pp.Season, pp.HomeTeamName)
                UNION ALL
            (SELECT pp.Season, pp.AwayTeamName as Club, 
            SUM(pp.AwayPoints) as Points,
            SUM(pp.FullTimeAwayGoals) as Goals,
            SUM(pp.AwayFouls) as Fouls,
            SUM(pp.AwayCorners) as Corners,
            SUM(pp.AwayYellowCards) as YellowCards,
            SUM(pp.AwayRedCards) as RedCards
            FROM part_points as pp
            GROUP BY pp.Season, pp.AwayTeamName))
        SELECT r.Season, r.Club, SUM(r.Points) as Points, SUM(r.Goals) as Goals, SUM(r.Fouls) as Fouls, 
            SUM(r.Corners) as Corners, SUM(r.YellowCards) as YellowCards, SUM(r.RedCards) as RedCards
        FROM result r
        GROUP BY r.Season, r.Club)
    SELECT *,
    RANK() OVER(PARTITION BY gr.Season ORDER BY gr.Points DESC) as PointsRank
    FROM get_rank gr
    WHERE gr.Season != 'Ses1899/1900')
SELECT tr.Season, tr.Club, tr.Points, tr.Goals, tr.Fouls, tr.Corners, tr.YellowCards, tr.RedCards
FROM total_rank tr
WHERE PointsRank = 1;