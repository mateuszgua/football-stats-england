WITH result as (
    SELECT g.FullTimeResult, b.B365H, b.B365D, b.B365A,
    CASE WHEN (b.B365H > b.B365A AND b.B365D > b.B365A) THEN 'A'
    WHEN (b.B365H > b.B365D AND b.B365A > b.B365D) THEN 'D'
    WHEN (b.B365D > b.B365H AND b.B365A > b.B365H) THEN 'H'
    ELSE 'empty' END as BetType
    FROM games g
    LEFT JOIN bets b ON g.id = b.id)
SELECT COUNT(*) AS NumberMatches,
CASE WHEN (r.FullTimeResult = r.BetType) THEN 1
ELSE 0 END as CorrectTypes
FROM result r
GROUP BY CorrectTypes
ORDER BY CorrectTypes DESC;