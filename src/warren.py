import math

# For all lists, assume form of bounds such that:
# [lower, upper]

# Number of decimal places to round calculated values. Values are only
# rounded when printing.
SIG_FIGS = 2

# Percentage of account lost to halt trading.
BREAKER = 0.02

# Account exposure at any given time.
EXPOSURE_RATE = [0.02, 0.04]

# Percentage of account accrewed in transactions/each trading day.
GAIN_RATE = [0.01, 0.025]

# Compute total value after a discrete increase in a principle `p` by 
# rate `r` is applied.
discrete = lambda p, r: p + p * r

# Starting account value for the day.
principle = float(input("What is today's principle ($)? "))

# Goal account value for the day.
goal_day = [discrete(principle, r) for r in GAIN_RATE]

# Maximum risk per transaction. This is the maximum amount allowed to
# be exposed at any point in time.
exposure_risk = [principle * r for r in EXPOSURE_RATE]

buy = [e / 100 for e in exposure_risk]

# Sell point for a given exposure (based on daily acrewal rate)
sell_lower = [discrete(buy[0], r) for r in GAIN_RATE]
sell_upper = [discrete(buy[1], r) for r in GAIN_RATE]


def option():
    """Compute option statistics."""
    pass


def rates():
    """Display rates used in calculations."""
    print(f'Breaker: \t{BREAKER}')
    print(f'Gain: \t\t{GAIN_RATE}')
    print(f'Exposure: \t{EXPOSURE_RATE}')


def rules():
    """Display today's rules."""
    print(f'Breaker: \t\t{round(principle - principle * BREAKER, SIG_FIGS)}')
    print(f'Goal: \t\t\t{[round(g, SIG_FIGS) for g in goal_day]}')
    print(f'Exposure: \t\t{[round(e, SIG_FIGS) for e in exposure_risk]}')
    print(f'Option (buy): \t\t{[round(b, SIG_FIGS) for b in buy]}')
    print(f'Option (sell, lower): \t{[round(s, SIG_FIGS) for s in sell_lower]}')
    print(f'Option (sell, upper): \t{[round(s, SIG_FIGS) for s in sell_upper]}')


while True:
    user_input = input('>')

    match user_input:
        case 'option':
            option()
        case 'rates':
            rates()
        case 'rules':
            rules()
        case _:
            print(f'Command not recognized: {user_input}')