print("☀️ Solar Panel Energy Estimator")

panel_count = int(input("Number of Solar Panels: "))
panel_power = float(input("Power of One Panel (W): "))
sun_hours = float(input("Daily Sunlight Hours: "))
efficiency = float(input("System Efficiency (%): "))

total_power_kw = (panel_count * panel_power) / 1000
daily_energy = total_power_kw * sun_hours * (efficiency / 100)
monthly_energy = daily_energy * 30
yearly_energy = daily_energy * 365

print("\n----- SOLAR ENERGY REPORT -----")
print(f"Installed Power: {total_power_kw:.2f} kW")
print(f"Daily Energy Production: {daily_energy:.2f} kWh")
print(f"Monthly Energy Production: {monthly_energy:.2f} kWh")
print(f"Yearly Energy Production: {yearly_energy:.2f} kWh")

if daily_energy >= 50:
    print("Production Level: HIGH ✅")
elif daily_energy >= 20:
    print("Production Level: MEDIUM ⚠️")
else:
    print("Production Level: LOW")