#Greetings

print("="*55)
print("WELCOME TO THE INVESTMENT ADVISOR")
print("="*55)
print(" ")

#asking question

#investment goal
investment_goal_options = {
    "A": "Preserve money",
    "B": "Generate income",
    "C": "Grow savings",
    "D": "Buy a house",
    "E": "Education",
    "F": "Retirement",
    "G": "Grow wealth"
}
while True:
        print("""1. What is your primary investment goal?
    A. Preserve money
    B. Generate income
    C. Grow savings
    D. Buy a house
    E. Education
    F. Retirement 
    G. Grow wealth""")
        choice = input("Enter your choice: ").upper()

        if choice in ["A", "B", "C", "D", "E", "F", "G"]:
            investment_goal = investment_goal_options[choice]
            break
        else:
            print("Invalid choice. Please try again.\n")

#Time horizon
time_horizon_options = {
    "A": "Less than 3 years",
    "B": "3-5 years",
    "C": "5-10 years",
    "D": "10+ years"
}
while True:
    print("""2. When will you need this money?
    A. Less than 3 years
    B. 3-5 years
    C. 5-10 years
    D. 10+ years""")

    time_horizon = input("Enter your choice: ").upper()

    if time_horizon in ["A", "B", "C", "D"]:
        time_horizon = time_horizon_options[time_horizon]
        break
    else:
        print("Invalid choice. Please try again.\n")

#Reaction to Market Drop
market_drop_options = {
    "A": "Sell everything",
    "B": "Sell some",
    "C": "Do nothing",
    "D": "Buy more"
}
while True:
    print("""3. If your portfolio fell 20% in one year, what would you do?
    A. Sell everything
    B. Sell some
    C. Do nothing
    D. Buy more""")

    market_drop = input("Enter your choice: ").upper()

    if market_drop in ["A", "B", "C", "D"]:
        market_drop = market_drop_options[market_drop]
        break
    else:
        print("Invalid choice. Please try again.\n")

#Experience
experience_options = {
    "A": "Never",
    "B": "Some experience",
    "C": "Very experienced"
}
while True:
    print("""4. Have you invested before?
    A. Never
    B. Some experience
    C. Very experienced""")

    experience = input("Enter your choice: ").upper()

    if experience in ["A", "B", "C"]:
        experience = experience_options[experience]
        break
    else:
        print("Invalid choice. Please try again.\n")

#Income stability
income_stability_options = {
    "A": "Unstable",
    "B": "Somewhat stable",
    "C": "Stable"
}
while True:
    print("""5. How stable is your income?
    A. Unstable
    B. Somewhat stable
    C. Stable""")

    income_stability = input("Enter your choice: ").upper()

    if income_stability in ["A", "B", "C"]:
        income_stability = income_stability_options[income_stability]
        break
    else:
        print("Invalid choice. Please try again.\n")

#Emergency fund
emergency_fund_options = {
    "A": "None",
    "B": "1-3 months",
    "C": "3-6 months",
    "D": "6+ months"
}
while True:
    print("""6. Do you have an emergency fund?
    A. None
    B. 1-3 months
    C. 3-6 months
    D. 6+ months""")

    emergency_fund = input("Enter your choice: ").upper()
    if emergency_fund in ["A", "B", "C", "D"]:
        emergency_fund = emergency_fund_options[emergency_fund]
        break
    else:
        print("Invalid choice. Please try again.\n")

#Acceptable Loss
acceptable_loss_options = {
    "A": "5%",
    "B": "10%",
    "C": "20%",
    "D": "30%+"
}
while True:
    print("""7. What percentage loss could you accept without panicking?
    A. 5%
    B. 10%
    C. 20%
    D. 30%+""")

    acceptable_loss = input("Enter your choice: ").upper()
    if acceptable_loss in ["A", "B", "C", "D"]:
        acceptable_loss = acceptable_loss_options[acceptable_loss]
        break
    else:
        print("Invalid choice. Please try again.\n")

#Age
age_options = {
    "A": "Under 30",
    "B": "30-45",
    "C": "45-60",
    "D": "60+"
}
while True:
    print("""8. What is your age?
    A. Under 30
    B. 30-45
    C. 45-60
    D. 60+""")

    age = input("Enter your choice: ").upper()
    if age in ["A", "B", "C", "D"]:
        age = age_options[age]
        break
    else:
        print("Invalid choice. Please try again.\n")

#Risk tolerance
risk_tolerance_options = {
    "A": "I avoid risk, guaranteed low return",
    "B": "Moderate return with some risk",
    "C": "I seek high returns even if risky"
}
while True:
    print("""9. Which statement best describes you?
    A. I avoid risk, guaranteed low return
    B. Moderate return with some risk
    C. I seek high returns even if risky"""
    )
    risk_tolerance = input("Enter your choice: ").upper()
    if risk_tolerance in ["A", "B", "C"]:
        risk_tolerance = risk_tolerance_options[risk_tolerance]
        break
    else:
        print("Invalid choice. Please try again.\n")

#Employment
employment_options = {
    "A": "Unemployed",
    "B": "Student",
    "C": "Part-time",
    "D": "Retired",
    "E": "Self-employed",
    "F": "Full-time"
}
while True:
    print("""10. What best describes your employment?
    A. Unemployed
    B. Student
    C. Part-time
    D. Retired
    E. Self-employed
    F. Full-time""")

    employment = input("Enter your choice: ").upper()
    if employment in ["A", "B", "C", "D", "E", "F"]:
        employment = employment_options[employment]
        break
    else:
        print("Invalid choice. Please try again.\n")

#income
yearly_income_options = {
    "A": "Low income",
    "B": "Median income",
    "C": "High income"
}
while True:
    print("""11. What is your yearly income?
    A. Low income
    B. Median income
    C. High income""")

    yearly_income = input("Enter your choice: ").upper()

    if yearly_income in ["A", "B", "C"]:
        yearly_income = yearly_income_options[yearly_income]
        break
    else:
        print("Invalid choice. Please try again.\n")
#Debt
current_debt_options = {
    "A": "None",
    "B": "Student loans",
    "C": "Mortgage",
    "D": "Car loan",
    "E": "Credit card debt"
}
while True:
    print("""12. Do you currently have debt?
    A. None
    B. Student loans
    C. Mortgage
    D. Car loan
    E. Credit card debt""")

    current_debt = input("Enter your choice: ").upper()
    if current_debt in ["A", "B", "C", "D", "E"]:
        current_debt = current_debt_options[current_debt]
        break
    else:
        print("Invalid choice. Please try again.\n")


#Calculating score for the investor profile
score = 0

if investment_goal == "Preserve money":
    score += 0
elif investment_goal == "Generate income":
    score += 2
elif investment_goal == "Grow savings":
    score += 3
elif investment_goal == "Buy a house":
    score += 4
elif investment_goal == "Education":
    score += 5
elif investment_goal == "Retirement":
    score += 6
elif investment_goal == "Grow wealth":
    score += 8

if time_horizon == "Less than 3 years":
    score += 0
elif time_horizon == "3–5 years":
    score += 5
elif time_horizon == "5–10 years":
    score += 10
elif time_horizon == "10+ years":
    score += 15

if market_drop == "Sell everything":
    score += 0
elif market_drop == "Sell some":
    score += 5
elif market_drop == "Do nothing":
    score += 10
elif market_drop == "Buy more":
    score += 15

if experience == "Never":
    score += 0
elif experience == "Some experience":
    score += 3
elif experience == "Very experienced":
    score += 6

if income_stability == "Unstable":
    score += 0
elif income_stability == "Somewhat stable":
    score += 4
elif income_stability == "Stable":
    score += 8

if emergency_fund == "None":
    score += 0
elif emergency_fund == "1–3 months":
     score += 3
elif emergency_fund == "3–6 months":
    score += 6
elif emergency_fund == "6+ months":
    score += 8

if acceptable_loss == "5%":
    score += 0
elif acceptable_loss == "10%":
    score += 4
elif acceptable_loss == "20%":
    score += 8
elif acceptable_loss == "30%+":
    score += 12

if age == "Under 30":
    score += 5
elif age == "30–45":
    score += 4
elif age == "45–60":
    score += 2
elif age == "60+":
    score += 0

if risk_tolerance == "I avoid risk, guaranteed low return  ":
    score += 0
elif risk_tolerance == "Moderate return with some risk":
    score += 8
elif risk_tolerance == "I seek high returns even if risky":
    score += 15

if employment == "Unemployed":
    score += 0
elif employment == "Student":
    score += 1
elif employment == "Part-time":
    score += 2
elif employment == "Retired":
    score += 2
elif employment == "Self-employed":
    score += 3
elif employment == "Full-time":
    score += 4

if yearly_income == "Low income":
    score += 1
elif yearly_income == "Median income":
    score += 3
elif yearly_income == "High income":
    score += 6

if current_debt == "None":
    score += 8
elif current_debt == "Student loan":
    score += 4
elif current_debt == "Mortgage":
    score += 6
elif current_debt == "Car loan":
    score += 2
elif current_debt == "Credit card":
    score += 0

#Determining investor profile based on score

     #incase any error
investor_profile = ""
bonds_percentage = ""
stocks_percentage = ""
risk_level = ""
profile_strategy = ""
project_objective = ""

if score >= 90:
    investor_profile = "Very Aggressive"
    bonds_percentage = "5%"
    stocks_percentage = "95%"
    risk_level = "81–100%"
    profile_strategy = "maximum growth investing"
    project_objective = "maximize long-term growth while accepting significant short-term volatility"
elif 69 <= score <= 89:
    investor_profile = "Aggressive"
    bonds_percentage = "20%"
    stocks_percentage = "80%"
    risk_level = "62–81%"
    profile_strategy = "growth-focused investment"
    project_objective = "maximize long-term growth while maintaining some portfolio stability"
elif 47 <= score <= 68:
    investor_profile = "Moderate"
    bonds_percentage = "40%"
    stocks_percentage = "60%"
    risk_level = "42–62%"
    profile_strategy = "balanced long-term investment"
    project_objective = "provide long-term growth while maintaining stability during market volatility"
elif 46 >= score >= 25:
    investor_profile = "Conservative"
    bonds_percentage = "60%"
    stocks_percentage = "40%"
    risk_level = "22–42%"
    profile_strategy = "capital-preserving investment"
    project_objective = "balance stability with steady long-term growth"
elif score <= 24:
    investor_profile = "Very Conservative"
    bonds_percentage = "80%"
    stocks_percentage = "20%"
    risk_level = "0–22%"
    profile_strategy = "cautious investment"
    project_objective = "preserve your capital while providing modest long-term growth"
#Determining Best Fund suggestion
fund_suggestion = ""

if emergency_fund == "a": #no emergency fund
    fund_suggestion = "Build an emergency fund before aggressive investing"
elif current_debt == "e": # creditcard debt
    fund_suggestion = "Consider paying off high-interest debt before increasing investments"
elif investment_goal == "b":
    fund_suggestion = "Bond Funds and Dividend ETFs" # generate income
elif investment_goal == "d" and time_horizon in ["a","b"]:
    fund_suggestion  = "Bond Funds and Money Market Funds"
elif time_horizon == "d" and risk_tolerance == "c": # Long Horizon High Risk
    fund_suggestion = "Stock Index Funds, Total Market ETFs and International ETFs"
elif time_horizon == "d" and risk_tolerance == "b": # Long Horizon Moderate Risk
    fund_suggestion = "Stock Index Funds and Bond Funds"
elif time_horizon == "d" and risk_tolerance == "a": # Long Horizon Low Risk
    fund_suggestion = "Balanced Funds and Bond Funds"
elif time_horizon == "c": # Medium Horizon
    fund_suggestion = "Balanced Funds and Bond Funds"
elif time_horizon in ["a","b"]: # Short Horizon
    fund_suggestion = "Bond Funds and Money Market Funds"
else:
    fund_suggestion ="Broad Market and Index Fund"

# Reason of recommendation based on financial situation
financial_situation_recommendation = ""
if emergency_fund == "a": #no emergency fund
    financial_situation_recommendation = "Build an emergency fund before aggressive investing"
elif current_debt == "e": # creditcard debt
    financial_situation_recommendation = "Consider paying off high-interest debt before increasing investments"
elif time_horizon == "a":
    financial_situation_recommendation = "you may need your money soon, so preserving your savings is more important than pursuing higher returns"
elif time_horizon == "b":
    financial_situation_recommendation = "your investment horizon is relatively short, so balancing growth with stability is important"
elif time_horizon == "c":
    financial_situation_recommendation = "your investment horizon provides enough time to pursue long-term growth while managing investment risk"
elif time_horizon == "d":
    financial_situation_recommendation = "you have many years before needing your money, allowing your investments time to recover from temporary market declines"
else:
    "your responses indicate that your investment strategy should match your goals and tolerance for risk"

#Comfortability based on Market drop
comfortability = ""
if market_drop == "Sell everything":
    comfortability = "less comfortable"
elif market_drop == "Sell some":
    comfortability = "somewhat comfortable"
elif market_drop == "Do nothing":
    comfortability = "comfortable"
elif market_drop == "Buy more":
    comfortability = "very comfortable"

#Investment goal advice
investment_goal_advice = ""

if investment_goal == "Preserve money":
    investment_goal_advice = "Preserving your savings appears to be your highest priority, so limiting investment risk may better support your objective."
elif investment_goal == "Generate income":
    investment_goal_advice = """Generating a reliable source of income is your primary objective. 
    Investments such as bond funds or dividend-focused ETFs may help provide regular income while reducing overall portfolio volatility."""
elif investment_goal == "Grow savings":
    investment_goal_advice = "A diversified investment strategy may help your savings grow while reducing unnecessary investment risk."
elif investment_goal == "Buy a house":
    investment_goal_advice = "Since you plan to use this money to purchase a house, protecting your savings becomes increasingly important as your purchase date approaches."
elif investment_goal == "Education":
    investment_goal_advice = "Investing consistently over time may help prepare for future education expenses while balancing growth and stability."
elif investment_goal == "Retirement":
    investment_goal_advice = "Retirement investing generally benefits from a long-term approach that allows compound growth to work over many years."
elif investment_goal == "Grow wealth":
    investment_goal_advice = "Growing your wealth usually requires accepting greater short-term market fluctuations in exchange for higher long-term return potential."

#Time horizon advice
time_horizon_advice = ""

if time_horizon == "Less than 3 years":
    time_horizon_advice = "Because you may need this money soon, preserving your capital is generally more important than pursuing higher investment returns."
elif time_horizon == "3–5 years":
    time_horizon_advice = "Your investment horizon is relatively short, so balancing growth with stability may help reduce the impact of market fluctuations."
elif time_horizon == "5–10 years":
    time_horizon_advice = "Your investment horizon allows you to pursue moderate long-term growth while still maintaining some portfolio stability."
elif time_horizon == "10+ years":
    time_horizon_advice = "Because you have many years before needing this money, your investments have more time to recover from temporary market declines."

#Advice based on experience
experience_advice = ""

if experience == "Never":
    experience_advice = "Since you are new to investing, beginning with diversified index funds rather than individual stocks may reduce unnecessary investment risk."
elif experience == "Some experience":
    experience_advice = "Your previous investing experience provides a useful foundation for building a diversified portfolio."
elif experience == "Very experienced":
    experience_advice = "Your investment experience may help you remain disciplined during periods of market volatility."

#Advice based on income
income_advice = ""

if income_stability == "Unstable":
    income_advice = "Because your income is less predictable, maintaining a larger emergency fund before increasing investment risk may improve your financial security."
elif income_stability == "Somewhat stable":
    income_advice = "Your income provides a reasonable foundation for investing consistently over time."
elif income_stability == "Stable":
    income_advice = "Your stable income supports regular investing and long-term financial planning."

#Emergency fund advice
emergency_fund_advice = ""

if emergency_fund == "None":
    emergency_fund_advice = "Building an emergency fund before taking significant investment risk may strengthen your financial foundation."
elif emergency_fund == "1–3 months":
     emergency_fund_advice = "Increasing your emergency savings toward three to six months of expenses may provide additional financial security."
elif emergency_fund == "3–6 months":
    emergency_fund_advice = "Your emergency savings provide a solid financial cushion for unexpected expenses."
elif emergency_fund == "6+ months":
    emergency_fund_advice = "A strong emergency fund supports long-term investing by reducing the need to sell investments during difficult periods."

#Advice based on current debt
debt_advice = ""

if current_debt == "None":
    debt_advice = "Being debt-free provides greater flexibility to pursue your long-term investment goals."
elif current_debt == "Student loan":
    debt_advice = "Continue balancing student loan repayments with consistent long-term investing."
elif current_debt == "Mortgage":
    debt_advice = "A mortgage can often be managed alongside long-term investing provided repayments remain affordable."
elif current_debt == "Car loan":
    debt_advice = "Consider balancing loan repayments with regular investing according to your financial priorities."
elif current_debt == "Credit card":
    debt_advice = "Paying off high-interest credit card debt before increasing investments is often financially beneficial."

#Market drop advice
market_drop_advice = ""

if market_drop == "Sell everything":
    market_drop_advice = "Your responses suggest that market declines may make you uncomfortable, indicating a lower tolerance for investment risk."
elif market_drop == "Sell some":
    market_drop_advice = "Your responses suggest that you prefer reducing risk during market declines while remaining partially invested."
elif market_drop == "Do nothing":
    market_drop_advice = "Remaining invested during market downturns is generally consistent with a long-term investment approach."
elif market_drop == "Buy more":
    market_drop_advice = "Viewing market declines as buying opportunities demonstrates a strong long-term investing mindset."

#Risk tolerance advice
risk_tolerance_advice = ""

if risk_tolerance == "I avoid risk, guaranteed low return  ":
    risk_tolerance_advice = "Your responses indicate that protecting your money is more important than maximizing investment returns."
elif risk_tolerance == "Moderate return with some risk":
    risk_tolerance_advice = "You appear comfortable balancing investment growth with manageable levels of market risk."
elif risk_tolerance == "I seek high returns even if risky":
    risk_tolerance_advice = "Your responses suggest you are willing to accept greater market volatility in pursuit of higher long-term returns."

#General tips
general_advice = """Invest consistently each month because regular investing (often called dollar-cost averaging) helps build wealth over time and reduces the impact of trying to time the market.
Stay diversified rather than relying on a single investment because diversification spreads risk across different investments, reducing the impact of any single investment performing poorly.
Avoid making emotional decisions during market declines because markets naturally rise and fall. Emotional reactions can lead to buying or selling at unfavorable times.
Review and rebalance your portfolio at least once a year because rebalancing helps keep your investments aligned with your intended stock/bond allocation.
Increase your investment contributions whenever your income grows because increasing contributions over time can have a significant effect on long-term investment growth.
Maintain an emergency fund for unexpected expenses because having emergency savings may reduce the need to sell investments during market downturns.
Continue learning about investing before making major financial decisions because understanding basic investment concepts can help you make more informed decisions.
Invest with a long-term perspective instead of focusing on short-term market movements because long-term investing allows more time for investments to recover from market fluctuations."""


#FINAL RESULTS
print(" ")
print("="*55)
print("             FINAL RESULTS/RECOMENDED PORTFOLIO  ")
print("="*55)
print(" ")

print("Risk score: " + str(score))
print("Investor Profile: " + str(investor_profile))
print("Suggested Allocation:")
print("Stocks: " + str(stocks_percentage))
print("Bonds: " + str(bonds_percentage) + "\n")

print("Suggested Investments:")
print(fund_suggestion + "\n")
print("Thank you for completing the questionnaire!")

#User's responses
print("\n------------------------------------------------")
print("YOUR RESPONSES")
print("------------------------------------------------")

print("Primary Goal: " + str(investment_goal))
print("Time horizon: " + str(time_horizon))
print("Investment experience: " + str(experience))
print("Income stability: " + str(income_stability))
print("Emergency fund: " + str(emergency_fund))
print("Debt: " + str(current_debt))
print("Risk tolerance: " + str(risk_tolerance) + "\n")
print("-"*50)

#Final paragraph
print("\n------------------------------------------------")
print("PERSONALIZED RECOMMENDATION")
print("------------------------------------------------")

print(f"""Based on your responses, you have an {investor_profile} investment profile with a {time_horizon} investment horizon, 
and your primary goal is {investment_goal}. You have {income_stability} income stability, a {emergency_fund} emergency fund, 
and are {comfortability} with temporary market declines. 
Because {financial_situation_recommendation}, your financial situation supports a {profile_strategy} strategy. 
A diversified portfolio consisting of approximately {stocks_percentage} stocks and {bonds_percentage} bonds 
may align with your profile. This allocation aims to {project_objective}. 
We recommend investing in {fund_suggestion}.""")

#Reason for recommendation
print("\n------------------------------------------------")
print("REASON FOR RECOMMENDATION")
print("-"*50)
print("------------------------------------------------")

print(f"""{investment_goal_advice}
{time_horizon_advice}
{experience_advice}
{income_advice}
{emergency_fund_advice}
{debt_advice}
{market_drop_advice}
{risk_tolerance_advice}
""")

#General investment advice
print("\n------------------------------------------------")
print("GENERAL INVESTING TIPS")
print("------------------------------------------------")
print(general_advice)

#End greeting and reminder
print("\n------------------------------------------------")
print("IMPORTANT REMINDER")
print("------------------------------------------------")

print("""This recommendation is intended for educational purposes only and should not be considered financial advice.
All investments involve risk, and the value of investments can rise or fall over time.
Past performance does not guarantee future results. You should review your investment
strategy regularly and consider seeking advice from a qualified financial professional
before making investment decisions.""")


print("\n")
print("="*70)
print("          THANK YOU FOR USING THE INVESTMENT ADVISOR")
print("="*70)






