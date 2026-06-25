WITH scores AS (
    SELECT
        dataset,
        pipeline,
        subject,
        AVG(score) AS mean_session_score
    FROM results
    GROUP BY dataset, pipeline, subject
)

SELECT
    dataset AS study,
    REGEXP_REPLACE(pipeline, '[^A-Za-z0-9_]', '_', 'g') AS treatment,
    AVG(mean_session_score) AS mean,
    STDDEV_SAMP(mean_session_score) AS "std.dev", -- noqa: RF05
    COUNT(*) AS "sampleSize" -- noqa: RF06
FROM scores
GROUP BY dataset, pipeline
