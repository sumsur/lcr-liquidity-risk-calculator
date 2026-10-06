import pandas as pd

#Load imput data
df = pd.read_csv("LCRinputs.csv")

#Calculate HQLA
def calculate_hqla(df): 
    hqla = df[df["Category"] == "HQLA"].copy()
    hqla["Adjusted_HQLA"] = (hqla["Amount_EUR"] * (1 - hqla["Haircut"]))
    
    return hqla["Adjusted_HQLA"].sum()

#Calculate cash outflows
def calculate_outflows(df): 
    outflows = df[df["Run_Off_Rates"]> 0].copy()
    outflows["Cash_Outflows"] = (outflows["Amount_EUR"] * outflows["Run_Off_Rates"])
    return outflows["Cash_Outflows"].sum()

#Calculate cash inflows
def calculate_inflows(df):
    inflows = df[df["Inflow_Rates"]> 0].copy()
    inflows["Cash_Inflows"] = (inflows["Amount_EUR"] * inflows["Inflow_Rates"])
    return inflows["Cash_Inflows"].sum()

#Calculate LCR
def calculate_lcr(df):
    hqla = calculate_hqla(df)
    outflows = calculate_outflows(df)
    inflows = calculate_inflows(df)

    #75% inflow cap
    eligible_inflows = min(inflows, outflows * 0.75)

    net_cash_outflows = outflows - eligible_inflows


    lcr = hqla / net_cash_outflows * 100

    return  hqla, outflows, inflows, eligible_inflows, net_cash_outflows, lcr

def stress_test(df, deposit_shock=0,funding_shock=0):
    stress_df = df.copy()
    
    #Stress on deposits
    deposit_mask = stress_df["Category"] == "Deposits"
    
    stress_df.loc[deposit_mask,"Run_Off_Rates"] = (stress_df.loc[deposit_mask,"Run_Off_Rates"]*(1 + deposit_shock)).clip(upper=1)
    
    #Stress on wholesale
    funding_mask = stress_df["Category"] == "Funding"
    
    stress_df.loc[funding_mask,"Run_Off_Rates"] = (stress_df.loc[funding_mask,"Run_Off_Rates"]*(1 + funding_shock)).clip(upper=1)
    
    return calculate_lcr(stress_df)

# Stress scenarios

base = calculate_lcr(df)

deposit_stress = stress_test(df,deposit_shock=0.50)

funding_stress = stress_test(df,funding_shock=0.50)

combined_stress = stress_test(df,deposit_shock=0.50,funding_shock=0.50)
    
#Run calculation 
hqla, outflows, inflows, eligible_inflows, net_cash_outflows,lcr = calculate_lcr(df)

#Display results
results = {"Base case": lcr, "Deposit Stress": deposit_stress[5], "Funding Stress": funding_stress[5], "Combined stress": combined_stress[5]}

print("\nLCR Stress Testing")
print("---------------------------")

for scenario, lcr_value in results.items():
    if lcr_value>= 100:
        status = "PASS"
    else:
        status = "FAIL"
    print(f"{scenario:<20} {lcr_value:>8.2f}%  {status}")
    
#Adding Graphs
import matplotlib.pyplot as plt

scenarios = list(results.keys())
lcr_values = list(results.values())

plt.figure(figsize=(8, 5))

plt.bar(scenarios, lcr_values)

plt.axhline(y=100, linestyle="--")

plt.ylabel("LCR (%)")
plt.title("LCR Stress Testing")
plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("lcr_stress_testing.png", dpi=300, bbox_inches="tight")

plt.show()

