# ============================================================
# INVESTMENT ADVISOR - PART 1 & 2
# Questions, Scoring, Investor Profile & Fund Suggestions
# ============================================================

# -----------------------------
# Helper Function
# -----------------------------
def ask_question(question, options):
    print("\n" + question)

    for letter, value in options.items():
        print(f"{letter}. {value['text']}")

    while True:
        answer = input("Enter your choice: ").upper()

        if answer in options:
            return answer

        print("Invalid choice. Please try again.")


# -----------------------------
# Store Questions
# -----------------------------

questions = [

{
"question":"1. What is your primary investment goal?",
"key":"goal",
"options":{

"A":{"text":"Preserve money","score":0},
"B":{"text":"Generate income","score":2},
"C":{"text":"Buy a house","score":5},
"D":{"text":"Retirement","score":8},
"E":{"text":"Grow wealth","score":10},
"F":{"text":"Education","score":6},
"G":{"text":"Grow savings","score":4}

}
},

{
"question":"2. When will you need this money?",
"key":"time",
"options":{

"A":{"text":"Less than 3 years","score":0},
"B":{"text":"3-5 years","score":3},
"C":{"text":"5-10 years","score":7},
"D":{"text":"10+ years","score":10}

}
},

{
"question":"3. If your portfolio fell 20% in one year, what would you do?",
"key":"drop20",
"options":{

"A":{"text":"Sell everything","score":0},
"B":{"text":"Sell some","score":3},
"C":{"text":"Do nothing","score":7},
"D":{"text":"Buy more","score":10}

}
},

{
"question":"4. Have you invested before?",
"key":"experience",
"options":{

"A":{"text":"Never","score":0},
"B":{"text":"Some experience","score":5},
"C":{"text":"Very experienced","score":10}

}
},

{
"question":"5. How stable is your income?",
"key":"income",
"options":{

"A":{"text":"Unstable","score":0},
"B":{"text":"Somewhat stable","score":5},
"C":{"text":"Very stable","score":10}

}
},

{
"question":"6. Do you have an emergency fund?",
"key":"emergency",
"options":{

"A":{"text":"No","score":0},
"B":{"text":"1-3 months","score":3},
"C":{"text":"3-6 months","score":7},
"D":{"text":"6+ months","score":10}

}
},

{
"question":"7. What percentage loss could you accept without panicking?",
"key":"loss",
"options":{

"A":{"text":"5%","score":0},
"B":{"text":"10%","score":3},
"C":{"text":"20%","score":7},
"D":{"text":"30%+","score":10}

}
},

{
"question":"8. What is your age?",
"key":"age",
"options":{

"A":{"text":"Under 30","score":10},
"B":{"text":"30-45","score":7},
"C":{"text":"45-60","score":3},
"D":{"text":"60+","score":0}

}
},

{
"question":"9. Which statement best describes you?",
"key":"risk",

"options":{

"A":{"text":"I avoid risk","score":0},
"B":{"text":"I accept some risk","score":5},
"C":{"text":"I seek high returns even if risky","score":10}

}
},

{
"question":"10. What would you do if the market dropped 40%?",
"key":"drop40",

"options":{

"A":{"text":"Sell immediately","score":0},
"B":{"text":"Wait","score":5},
"C":{"text":"Invest more","score":10}

}
},

{
"question":"11. What best describes your employment?",

"key":"employment",

"options":{

"A":{"text":"Student","score":2},
"B":{"text":"Full-time","score":8},
"C":{"text":"Part-time","score":4},
"D":{"text":"Self-employed","score":6},
"E":{"text":"Retired","score":4},
"F":{"text":"Unemployed","score":0}

}
},

{
"question":"12. What is your yearly income?",

"key":"salary",

"options":{

"A":{"text":"High income","score":10},
"B":{"text":"Median income","score":6},
"C":{"text":"Low income","score":2}

}
},

{
"question":"13. Do you currently have debt?",

"key":"debt",

"options":{

"A":{"text":"None","score":10},
"B":{"text":"Student loans","score":5},
"C":{"text":"Mortgage","score":7},
"D":{"text":"Car loan","score":3},
"E":{"text":"Credit card debt","score":0}

}
},

{
"question":"14. Which statement best describes you?",

"key":"return",

"options":{

"A":{"text":"Guaranteed low return","score":0},
"B":{"text":"Moderate return with some risk","score":5},
"C":{"text":"High return with significant risk","score":10}

}
}

]

# ============================================================
# ASK QUESTIONS
# ============================================================

answers = {}
score = 0

print("="*55)
print("WELCOME TO THE INVESTMENT ADVISOR")
print("="*55)

for q in questions:

    answer = ask_question(q["question"], q["options"])

    answers[q["key"]] = {
        "choice": answer,
        "text": q["options"][answer]["text"]
    }

    score += q["options"][answer]["score"]


# ============================================================
# DETERMINE INVESTOR PROFILE
# ============================================================

if score <= 30:

    profile = "Very Conservative"
    stocks = 20
    bonds = 80

elif score <= 60:

    profile = "Conservative"
    stocks = 40
    bonds = 60

elif score <= 90:

    profile = "Moderate"
    stocks = 60
    bonds = 40

elif score <= 115:

    profile = "Growth"
    stocks = 80
    bonds = 20

else:

    profile = "Aggressive Growth"
    stocks = 95
    bonds = 5


# ============================================================
# FUND SUGGESTION ENGINE
# ============================================================

goal = answers["goal"]["text"]
time = answers["time"]["text"]
risk = answers["risk"]["text"]
emergency = answers["emergency"]["text"]
debt = answers["debt"]["text"]

funds = []


# Emergency Fund

if emergency == "No":

    funds.append("Build an emergency fund before aggressive investing")


# Credit Card Debt

elif debt == "Credit card debt":

    funds.append("Consider paying off high-interest debt before increasing investments")


# Income Goal

elif goal == "Generate income":

    funds.append("Bond Funds")
    funds.append("Dividend ETFs")


# House Goal

elif goal == "Buy a house" and time in ["Less than 3 years","3-5 years"]:

    funds.append("Bond Funds")
    funds.append("Money Market Funds")


# Long Horizon High Risk

elif time == "10+ years" and risk == "I seek high returns even if risky":

    funds.append("Stock Index Funds")
    funds.append("Total Market ETFs")
    funds.append("International ETFs")


# Long Horizon Moderate Risk

elif time == "10+ years" and risk == "I accept some risk":

    funds.append("Stock Index Funds")
    funds.append("Bond Funds")


# Long Horizon Low Risk

elif time == "10+ years" and risk == "I avoid risk":

    funds.append("Balanced Funds")
    funds.append("Bond Funds")


# Medium Horizon

elif time == "5-10 years":

    funds.append("Balanced Funds")
    funds.append("Bond Funds")


# Short Horizon

elif time in ["Less than 3 years","3-5 years"]:

    funds.append("Bond Funds")
    funds.append("Money Market Funds")


# Default

else:

    funds.append("Broad Market Index Fund")


# ============================================================
# RESULTS OF PART 1 & 2
# ============================================================

print("\n")
print("="*55)
print("RESULTS")
print("="*55)

print(f"Risk Score: {score}/138")

print(f"Investor Profile: {profile}")

print(f"Suggested Allocation:")
print(f"Stocks : {stocks}%")
print(f"Bonds  : {bonds}%")

print("\nSuggested Investments:")

for fund in funds:
    print(f"• {fund}")

print("\nThank you for completing the questionnaire!")

# ============================================================
# PART 3 - ADVICE ENGINE
# ============================================================

# ------------------------------------------------------------
# GOAL ADVICE
# ------------------------------------------------------------

goal_advice = {

    "Preserve money":
    "Preserving your savings appears to be your highest priority, so limiting investment risk may better support your objective.",

    "Generate income":
    "Generating a reliable source of income is your primary objective. Investments such as bond funds or dividend-focused ETFs may help provide regular income while reducing overall portfolio volatility.",

    "Buy a house":
    "Since you plan to use this money to purchase a house, protecting your savings becomes increasingly important as your purchase date approaches.",

    "Retirement":
    "Retirement investing generally benefits from a long-term approach that allows compound growth to work over many years.",

    "Grow wealth":
    "Growing your wealth usually requires accepting greater short-term market fluctuations in exchange for higher long-term return potential.",

    "Education":
    "Investing consistently over time may help prepare for future education expenses while balancing growth and stability.",

    "Grow savings":
    "A diversified investment strategy may help your savings grow while reducing unnecessary investment risk."

}

# ------------------------------------------------------------
# TIME HORIZON ADVICE
# ------------------------------------------------------------

time_advice = {

    "Less than 3 years":
    "Because you may need this money soon, preserving your capital is generally more important than pursuing higher investment returns.",

    "3-5 years":
    "Your investment horizon is relatively short, so balancing growth with stability may help reduce the impact of market fluctuations.",

    "5-10 years":
    "Your investment horizon allows you to pursue moderate long-term growth while still maintaining some portfolio stability.",

    "10+ years":
    "Because you have many years before needing this money, your investments have more time to recover from temporary market declines."

}

# ------------------------------------------------------------
# EXPERIENCE ADVICE
# ------------------------------------------------------------

experience_advice = {

    "Never":
    "Since you are new to investing, beginning with diversified index funds rather than individual stocks may reduce unnecessary investment risk.",

    "Some experience":
    "Your previous investing experience provides a useful foundation for building a diversified portfolio.",

    "Very experienced":
    "Your investment experience may help you remain disciplined during periods of market volatility."

}

# ------------------------------------------------------------
# INCOME ADVICE
# ------------------------------------------------------------

income_advice = {

    "Unstable":
    "Because your income is less predictable, maintaining a larger emergency fund before increasing investment risk may improve your financial security.",

    "Somewhat stable":
    "Your income provides a reasonable foundation for investing consistently over time.",

    "Very stable":
    "Your stable income supports regular investing and long-term financial planning."

}

# ------------------------------------------------------------
# EMERGENCY FUND ADVICE
# ------------------------------------------------------------

emergency_advice = {

    "No":
    "Building an emergency fund before taking significant investment risk may strengthen your financial foundation.",

    "1-3 months":
    "Increasing your emergency savings toward three to six months of expenses may provide additional financial security.",

    "3-6 months":
    "Your emergency savings provide a solid financial cushion for unexpected expenses.",

    "6+ months":
    "A strong emergency fund supports long-term investing by reducing the need to sell investments during difficult periods."

}

# ------------------------------------------------------------
# DEBT ADVICE
# ------------------------------------------------------------

debt_advice = {

    "None":
    "Being debt-free provides greater flexibility to pursue your long-term investment goals.",

    "Student loans":
    "Continue balancing student loan repayments with consistent long-term investing.",

    "Mortgage":
    "A mortgage can often be managed alongside long-term investing provided repayments remain affordable.",

    "Car loan":
    "Consider balancing loan repayments with regular investing according to your financial priorities.",

    "Credit card debt":
    "Paying off high-interest credit card debt before increasing investments is often financially beneficial."

}

# ------------------------------------------------------------
# MARKET BEHAVIOUR
# ------------------------------------------------------------

market_advice = {

    "Sell immediately":
    "Your responses suggest that large market declines may make you uncomfortable, indicating a lower tolerance for investment risk.",

    "Wait":
    "Remaining invested during market downturns is generally consistent with long-term investing.",

    "Invest more":
    "Viewing market declines as opportunities demonstrates a strong long-term investing mindset."

}

# ------------------------------------------------------------
# RISK PERSONALITY
# ------------------------------------------------------------

risk_advice = {

    "I avoid risk":
    "Your responses indicate that protecting your money is more important than maximizing investment returns.",

    "I accept some risk":
    "You appear comfortable balancing investment growth with manageable levels of market risk.",

    "I seek high returns even if risky":
    "Your responses suggest you are willing to accept greater market volatility in pursuit of higher long-term returns."

}

# ============================================================
# PROFILE PARAGRAPHS
# ============================================================

profile_paragraph = {

"Very Conservative":
"""
Based on your responses, you have a Very Conservative investment profile with a {time} investment horizon and your primary goal is {goal}. You have {income} income stability, a {emergency} emergency fund, and are less comfortable with temporary market declines. Because your responses suggest that protecting your savings is more important than pursuing higher returns, a cautious investment strategy may better suit your needs. A diversified portfolio consisting of approximately {stocks}% stocks and {bonds}% bonds may align with your financial situation. This allocation aims to preserve your savings while still providing modest long-term growth. We recommend investing in {funds}.
""",

"Conservative":
"""
Based on your responses, you have a Conservative investment profile with a {time} investment horizon and your primary goal is {goal}. You have {income} income stability, a {emergency} emergency fund, and are somewhat cautious about temporary market declines. Because your investment horizon and financial situation suggest that stability is important, a portfolio balancing growth with lower volatility may be appropriate. A diversified portfolio consisting of approximately {stocks}% stocks and {bonds}% bonds may align with your profile. This allocation seeks moderate growth while reducing the impact of market fluctuations. We recommend investing in {funds}.
""",

"Moderate":
"""
Based on your responses, you have a Moderate investment profile with a {time} investment horizon and your primary goal is {goal}. You have {income} income stability, a {emergency} emergency fund, and are comfortable with temporary market declines. Because you have both the ability and willingness to accept a moderate level of investment risk, your financial situation supports a balanced long-term strategy. A diversified portfolio consisting of approximately {stocks}% stocks and {bonds}% bonds may align with your profile. This allocation aims to provide long-term growth while maintaining stability during periods of market volatility. We recommend investing in {funds}.
""",

"Growth":
"""
Based on your responses, you have a Growth investment profile with a {time} investment horizon and your primary goal is {goal}. You have {income} income stability, a {emergency} emergency fund, and are comfortable with temporary market declines. Because you indicated that you are willing to remain invested during market downturns and have sufficient time before needing your investments, your financial situation supports a growth-focused strategy. A diversified portfolio consisting of approximately {stocks}% stocks and {bonds}% bonds may align with your profile. This allocation aims to maximize long-term growth while maintaining some stability during market volatility. We recommend investing in {funds}.
""",

"Aggressive Growth":
"""
Based on your responses, you have an Aggressive Growth investment profile with a {time} investment horizon and your primary goal is {goal}. You have {income} income stability, a {emergency} emergency fund, and are very comfortable with temporary market declines. Because you indicated a high tolerance for market volatility and have sufficient time to recover from short-term market declines, your financial situation supports an aggressive growth strategy. A diversified portfolio consisting of approximately {stocks}% stocks and {bonds}% bonds may align with your profile. This allocation aims to maximize long-term growth, although it may experience substantial short-term fluctuations. We recommend investing in {funds}.
"""

}

# ============================================================
# UNIVERSAL ADVICE
# ============================================================

general_advice = [

"Continue investing consistently each month.",

"Stay diversified rather than relying on a single investment.",

"Avoid making emotional decisions during market declines.",

"Review and rebalance your portfolio at least once a year.",

"Increase your investment contributions whenever your income grows.",

"Continue learning about investing before making major financial decisions."

]

# ============================================================
# PART 4 - FINAL REPORT
# ============================================================

# ----------------------------
# Extract User Answers
# ----------------------------

goal = answers["goal"]["text"]
time = answers["time"]["text"]
experience = answers["experience"]["text"]
income = answers["income"]["text"]
emergency = answers["emergency"]["text"]
debt = answers["debt"]["text"]
risk = answers["risk"]["text"]
market = answers["drop40"]["text"]

# ----------------------------
# Convert fund list into text
# ----------------------------

fund_text = ", ".join(funds)

# ----------------------------
# Build Main Recommendation
# ----------------------------

main_paragraph = profile_paragraph[profile].format(
    goal=goal,
    time=time,
    income=income,
    emergency=emergency,
    stocks=stocks,
    bonds=bonds,
    funds=fund_text
)

# ----------------------------
# Build Personalized Advice
# ----------------------------

extra_advice = []

extra_advice.append(goal_advice[goal])
extra_advice.append(time_advice[time])
extra_advice.append(experience_advice[experience])
extra_advice.append(income_advice[income])
extra_advice.append(emergency_advice[emergency])
extra_advice.append(debt_advice[debt])
extra_advice.append(risk_advice[risk])
extra_advice.append(market_advice[market])

# ----------------------------
# Display Final Report
# ----------------------------

print("\n")
print("="*70)
print("                 PERSONAL INVESTMENT REPORT")
print("="*70)

print(f"\nRisk Score: {score}/138")
print(f"Investor Profile: {profile}")

print("\n------------------------------------------------")
print("YOUR RESPONSES")
print("------------------------------------------------")

print(f"Primary Goal: {goal}")
print(f"Time Horizon: {time}")
print(f"Investment Experience: {experience}")
print(f"Income Stability: {income}")
print(f"Emergency Fund: {emergency}")
print(f"Debt: {debt}")
print(f"Risk Tolerance: {risk}")

print("\n------------------------------------------------")
print("RECOMMENDED PORTFOLIO")
print("------------------------------------------------")

print(f"Stocks : {stocks}%")
print(f"Bonds  : {bonds}%")

print("\nSuggested Investments:")

for fund in funds:
    print(f"• {fund}")

print("\n------------------------------------------------")
print("PERSONALIZED RECOMMENDATION")
print("------------------------------------------------")

print(main_paragraph)

print("\n------------------------------------------------")
print("WHY THIS RECOMMENDATION?")
print("------------------------------------------------")

for advice in extra_advice:
    print("•", advice)

print("\n------------------------------------------------")
print("GENERAL INVESTING TIPS")
print("------------------------------------------------")

for tip in general_advice:
    print("•", tip)

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