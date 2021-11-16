curl --location --request POST 'https://catalog-query-ext.cp.api.test.godaddy.com/v2/catalog/offers' \
    --header 'Authorization: sso-jwt eyJhbGciOiAiUlMyNTYiLCAia2lkIjogIlFUbFFfdzZNdkEifQ.eyJqdGkiOiAiWndnc1JKMGlEMXJqSnplUWNPWThiUT09IiwgImlhdCI6IDE2MzI0MTg1NjUsICJhdXRoIjogImJhc2ljIiwgInR5cCI6ICJjZXJ0IiwgImZhY3RvcnMiOiB7InBfY2VydCI6IDE2MzI0MTg1NjV9LCAic2JqIjogeyJvIjogIkdvRGFkZHkgSU5DLiIsICJvdSI6ICJHb0RhZGR5IElOQy4iLCAiY24iOiAicWEudGVzdC1nb2RhZGR5LmNvbSJ9fQ.KuYmtB8s52uSbvCwoDF1kBjNdQjr1_PFrc8reFRo-hhvHc2nB4bsqflwyvnz6P0y6R-2A1A2LXnXlTpy1nZpvYD42V82bKwgs9Y_9o2hcNU212fp0wBrh-20_gAu1Ab_cpChi0TkehM6Wd2zPaNmE7U_F85IMdsNfkK0A-hJlITEXCQl7umvDXmkz2fPJFMuOUjr2CE1sYwoSC91MLpAbK99cmuayDfB0NVlMgXFXTylNShH8f0xoMf3aktIUNd-wNeaH4t7ZCqQBb-1WGJgEOIQbLhI1Shq9s-M7WJ6jxQKy8zdue9pFGjMTmydofIUeoTooQNdB0h5Yrd3T_PQ8Q' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "currency": "USD",
        "marketId": "en-US",
        "storefrontUri": "/customers/31430a42-6f4f-4646-9595-305f614957be/storefronts/134df2f0-2108-4a8c-86d5-b52abacd9836",
        "tags": ["payfac-free"]
    }'