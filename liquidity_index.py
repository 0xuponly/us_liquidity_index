import matplotlib.pyplot as plt
from fredapi import Fred
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
api_key = os.getenv('API_KEY')
fred = Fred(api_key=api_key)

fed_balance_sheet = fred.get_series('WALCL')
reverse_repo_bids = fred.get_series('WDTGAL')
tga_balance = fred.get_series('RRPONTSYD')

aligned_data = pd.concat([fed_balance_sheet, reverse_repo_bids, tga_balance], axis=1, keys=['fed_balance_sheet', 'reverse_repo_bids', 'tga_balance']).fillna(0)

fed_balance_sheet = aligned_data['fed_balance_sheet']
reverse_repo_bids = aligned_data['reverse_repo_bids']
tga_balance = aligned_data['tga_balance']

liquidity_index = fed_balance_sheet - reverse_repo_bids - tga_balance
print(liquidity_index)

plt.plot(liquidity_index)
plt.title('Liquidity Index')
plt.xlabel('Date')
plt.ylabel('Index Value')
plt.show()