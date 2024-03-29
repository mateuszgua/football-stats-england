WITH all_goals as (
    SELECT Season, AVG(FullTimeHomeGoals) as HomeGoals, AVG(FullTimeAwayGoals) as AwayGoals 
    FROM games
    WHERE Season != 'Ses1899/1900'
    GROUP BY Season)
SELECT ag.Season, SUM(ag.HomeGoals + ag.AwayGoals) as AvgGoals
FROM all_goals ag
GROUP BY ag.Season
ORDER BY ag.Season;