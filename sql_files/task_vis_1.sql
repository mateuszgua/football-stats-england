
DROP PROCEDURE IF EXISTS GetTeamResultFromSeason;
CREATE PROCEDURE GetTeamResultFromSeason(
    IN in_rank INT, 
    IN in_season CHAR(15), 
    OUT out_season CHAR(15),
    OUT out_club CHAR(20), 
    OUT out_points INT)
BEGIN
    WITH total_result AS (
        WITH create_rank AS (
            WITH all_points AS (
                WITH games_points AS (SELECT g.Season, c.name as HomeTeamName, c1.name as AwayTeamName, 
                    CASE WHEN g.FullTimeResult IN ('H') THEN 3
                    WHEN g.FullTimeResult IN ('D') THEN 1
                    ELSE 0 END as HomePoints,
                    CASE WHEN g.FullTimeResult IN ('A') THEN 3
                    WHEN g.FullTimeResult IN ('D') THEN 1
                    ELSE 0 END as AwayPoints
                    FROM games g
                    LEFT JOIN clubs c ON g.HomeTeam = c.id
                    LEFT JOIN clubs c1 ON g.AwayTeam = c1.id)
                (SELECT gp.Season, gp.HomeTeamName as Club,
                SUM(gp.HomePoints) as Points
                FROM games_points as gp
                GROUP BY gp.Season, gp.HomeTeamName)
                UNION ALL 
                (SELECT gp.Season, gp.AwayTeamName as Club,
                SUM(gp.AwayPoints) as Points
                FROM games_points as gp
                GROUP BY gp.Season, gp.AwayTeamName))
            SELECT ap.Season, ap.Club, SUM(ap.Points) as Points
            FROM all_points ap
            GROUP BY ap.Season, ap.Club)
        SELECT *, 
        RANK() OVER(PARTITION BY cr.Season ORDER BY cr.Points DESC) AS SeasonRank  
        FROM create_rank cr
        WHERE cr.Season != 'Ses1899/1900')
    SELECT tr.Season, tr.Club, tr.Points INTO out_season, out_club, out_points
    FROM total_result tr
    WHERE tr.SeasonRank = in_rank AND tr.Season = in_season;
END;