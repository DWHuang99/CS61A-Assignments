from lab06 import *
mint = Mint()
mint.year
2024
dime = mint.create(Dime)
dime.year
2024
Mint.present_year = 2104  # Time passes
nickel = mint.create(Nickel)
nickel.year     # The mint has not updated its stamp yet
2024
nickel.worth()  # 5 cents + (80 - 50 years)
35
mint.update()   # The mint's year is updated to 2104
Mint.present_year = 2179     # More time passes
mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
35
Mint().create(Dime).worth()  # A new mint has the current year
-40