import collections

companies_Qty = int(input('Enter company qty please: '))
summary_data = {}
global_average_profit = 0

for i in range(companies_Qty):
    name = input("Enter name of company number " + str(i + 1) + ": ")
    annual_profit_list = input(
        "Please enter 4 quarters profit for '" + name + "' company, separated by ' ' - space: ").split()
    current_company_profit_counter = 0
    for quarter in annual_profit_list:
        current_company_profit_counter += float(quarter)

    summary_data[name] = current_company_profit_counter
    global_average_profit += current_company_profit_counter


global_average_profit /= companies_Qty
print("Global average profit for all " + str(companies_Qty) + " companies is: " + str(global_average_profit))
above_market = {}
below_market = {}
for one_company in summary_data:
    if summary_data.get(one_company) > global_average_profit:
        above_market.update({one_company: summary_data.get(one_company)})
    else:
        below_market.update({one_company: summary_data.get(one_company)})

print("We have these companies upper then average:")
print(above_market)

print("\nWe have these companies lower then average:")
print(below_market)



