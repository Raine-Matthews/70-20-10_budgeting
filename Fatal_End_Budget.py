# Budgeting 70/20/10 app. Also, calculating how many FATAL END pedals I can make.

from datetime import datetime

# ---------------------------------------------------------------

# 1. INPUT SELECTION

# ---------------------------------------------------------------
income_input = input("Enter your total income: £ " )
income = float(income_input)

# Bundle bills and credit card payments here.

subs_input = input("Enter your total monthly subscriptions (including credit card bills): £ " )

subscriptions = float(subs_input)

# ---------------------------------------------------------------

# 2. DATE & CALENDAR TRACKING LOGIC

today = datetime.now()

# Determine the month and year for the next payday.

if today.day < 28:
    next_payday = datetime(today.year, today.month, 28)
elif today.month == 12:
    next_payday = datetime(today.year + 1,1,28)
else:
    next_payday = datetime(today.year, today.month + 1, 28)

# Calculate exact days left in the cycle

days_left = (next_payday - today).days

# Guard against dividing by zero if exactly on the 28th.

if  days_left ==    0:
    days_left =     1
# ---------------------------------------------------------------

# 3. BUDGET SPLITS AND CALCULATIONS

needs = income          *       0.70
wants = income          *       0.20
savings = income        *       0.10

# FATAL END PRODUCTION

# FATAL END PRODUCTION FACTUAL PRODUCTION COSTS FOR THE ENTIRE BATCH:

total_units             =      10.00
electronics_paid        =      53.62
hardware_remaining      =      90.10
enclosures_remaining    =      160.00

# COMBINED MANUFACTURING COSTS:

total_batch_cost        =       electronics_paid + hardware_remaining + enclosures_remaining

# £303.72

# THE ACTUAL REMAINING CASH GAP MONZO NEEDS POT HAS TO CLEAR

money_needed_for_series  = total_batch_cost - wants

# BUSINESS PROJECTIONS (£50 EACH) :

gross_revenue             = total_units * 50.00
net_profit                = gross_revenue - total_batch_cost


# Calculate remaining needs after fixed bills/credit cards

remaining_needs = needs - subscriptions

# Faded Lights product details & manufacturing capacity

pedal_cost = 50.00
batch_production = wants // pedal_cost

# Only use the true leftover change for the daily allowance!!!


leftover_wants = wants - pedal_cost * batch_production
series_cost = 210.00
daily_treat = wants / 31


# ---------------------------------------------------------------

print("-" * 85)
print(f"{'Real World Banking':^85}")
print("-" * 85)

print(f"{f'{'CHASE CURRENT ACCOUNT (NEEDS):':<40} {f'£{needs:.2f}':>12}':^75}")
print(f"{f'{'Fixed Subscriptions:':<40} {f'£{subscriptions:.2f}':>12}':^75}")
print(f"{f'{'Leftover Needs:':<40} {f'£{remaining_needs:.2f}':>12}':^75}")


print(f"{f'{'MONZO CURRENT ACCOUNT (WANTS):':<40} {f'£{wants:.2f}':>12}':^75}")
print(f"{f'{'Wants:':<40} {f'£{wants:.2f}':>12}':^75}")
print(f"{f'{'Leftover Wants:':<40} {f'£{leftover_wants:.2f}':>12}':^75}")
print(f"{f'{'Fatal End Production Goal:':<40} {'10 Pedals':>12}':^75}")
print(f"{f'{'CASH NEEDED TO FUND BATCH:':<40} {f'£{money_needed_for_series:.2f}':>12}':^75}")


print(f"{f'{'CHASE CURRENT ACCOUNT (SAVINGS):':<40} {f'£{savings:.2f}':>12}':^75}")

# 4. DAILY TREAT MONEY

print(f"{f'{'DAILY TREAT MONEY:':<40} {f'£{daily_treat:.2f}':>12}':^75}")
print("-" * 75)
