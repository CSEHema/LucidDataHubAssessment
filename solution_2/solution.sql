WITH word_counts AS (
    SELECT
        word,
        COUNT(*) AS cnt
    FROM words_table
    GROUP BY word
),
ranked AS (
    SELECT
        word,
        cnt,
        DENSE_RANK() OVER (ORDER BY cnt DESC) AS rnk
    FROM word_counts
)
SELECT word, cnt
FROM ranked
WHERE rnk <= 10
ORDER BY rnk;
