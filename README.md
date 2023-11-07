# us_liquidity_index
This script pulls and visualizes 3 key metric to approximate net liquidity in the US financial system.
The formula used (fed_balance_sheet - reverse_repo_bids - tga_balance) was pulled from an essay written by Arthur Hayes.
Data is pulled from the St. Louis Federal Reserve's FRED (Federal Reserve Economic Data) database via API call.

fed_balance_sheet: https://fred.stlouisfed.org/series/WALCL
reverse_repo_bids: https://fred.stlouisfed.org/series/WDTGAL
tga_balance: https://fred.stlouisfed.org/series/RRPONTSYD
