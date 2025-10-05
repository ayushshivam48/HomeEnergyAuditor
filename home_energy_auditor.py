def calculate_energy_usage(power_watts, hours_per_day, days_per_month):
    return (power_watts * hours_per_day * days_per_month) / 1000

def calculate_monthly_cost(kwh, cost_per_kwh=7.0):
    return kwh * cost_per_kwh

def calculate_emissions(kwh, emission_factor=0.82):
    return kwh * emission_factor

def energy_tips(appliance, kwh):
    if kwh > 150:
        return f"Consider using energy-efficient models or reducing usage time for your {appliance}."
    elif kwh > 50:
        return f"You can reduce {appliance} usage by turning it off when not in use."
    else:
        return f"Your {appliance} energy usage is efficient. Keep it up!"

def main():
    print("💡 Home Energy Efficiency Auditor 💡")
    print("------------------------------------")

    appliance = input("Enter the appliance name: ")
    power = float(input(f"Enter {appliance}'s power rating (in watts): "))
    hours = float(input(f"Enter hours used per day for {appliance}: "))
    days = int(input(f"Enter number of days used per month: "))

    kwh = calculate_energy_usage(power, hours, days)
    cost = calculate_monthly_cost(kwh)
    emissions = calculate_emissions(kwh)

    print(f"\nEstimated Monthly Energy Usage: {kwh:.2f} kWh")
    print(f"Estimated Monthly Cost: ₹{cost:.2f}")
    print(f"Estimated Monthly CO₂ Emissions: {emissions:.2f} kg")

    print("\nSuggestion:", energy_tips(appliance, kwh))
    print("\n🌍 Small energy savings lead to big environmental impact!")

if __name__ == "__main__":
    main()
