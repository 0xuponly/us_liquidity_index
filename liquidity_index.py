import nasdaqdatalink
import pandas as pd
import matplotlib.pyplot as plt

# gdp_usa = nasdaqdatalink.get("FRED/GDP")
# yields_ust = nasdaqdatalink.get("USTREASURY/YIELD")

def build_index():
    # import and clean data
    fed_balance_sheet = nasdaqdatalink.get("FRED/WALCL")     # millions, weekly, https://fred.stlouisfed.org/series/WALCL
    fed_balance_sheet['Value'] = fed_balance_sheet['Value']/1000
    fed_balance_sheet.rename(columns={'Value': 'fed_balance_sheet'}, inplace=True)
    reverse_repo_bids = nasdaqdatalink.get("FRED/WDTGAL")    # millions, weekly, https://fred.stlouisfed.org/series/WDTGAL
    reverse_repo_bids['Value'] = reverse_repo_bids['Value']/1000
    reverse_repo_bids.rename(columns={'Value': 'reverse_repo_bids'}, inplace=True)
    tga_balance = nasdaqdatalink.get("FRED/RRPONTSYD")       # billions, daily, https://fred.stlouisfed.org/series/RRPONTSYD
    tga_balance.rename(columns={'Value': 'tga_balance'}, inplace=True)

    # combine data and compute index value
    usd_liquidity = pd.concat([fed_balance_sheet, reverse_repo_bids, tga_balance], axis=1)
    #usd_liquidity.dropna(inplace=True)
    usd_liquidity.fillna(0, inplace=True)
    usd_liquidity['usd_liquidity_index'] = usd_liquidity['fed_balance_sheet'] - usd_liquidity['reverse_repo_bids'] - usd_liquidity['tga_balance']

    return usd_liquidity

def plot_index(index):
    # plot results
    index.plot(y='usd_liquidity_index', kind='line')
    plt.show()

def main():
    index = build_index()
    plot_index(index)

if __name__ == '__main__':
    main()