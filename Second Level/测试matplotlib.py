import openpyxl, numpy as np, matplotlib.pyplot as plt

# 读取 Excel
wb = openpyxl.load_workbook("Spot_Speed_Raw_Edited.xlsx")
ws = wb.active

# 提取数据
mins, maxs, vehicles = [], [], []
for row in ws.iter_rows(min_row=2, values_only=True):  # 从第二行开始
    if row[0] is None: 
        continue
    mins.append(row[0])
    maxs.append(row[1])
    vehicles.append(row[2])

mins, maxs, vehicles = np.array(mins), np.array(maxs), np.array(vehicles)
avg_speed = (mins + maxs) / 2
N = vehicles.sum()
rel_freq = vehicles / N * 100
cum_freq = np.cumsum(vehicles) / N * 100

# 关键数值
mode_val, median_val = 22.00, 21.67
pace_low, pace_high = 16.67, 26.67
percent_in_pace = 69.0
p15, p85 = 16.67, 26.83

# Relative Frequency
plt.figure(figsize=(8,5))
plt.scatter(avg_speed, rel_freq, label="Data")
coeffs = np.polyfit(avg_speed, rel_freq, 3)
xs = np.linspace(avg_speed.min(), avg_speed.max(), 300)
plt.plot(xs, np.polyval(coeffs, xs), label="Smooth curve")
for val, label in [(mode_val,"Mode"), (median_val,"Median"), 
                   (pace_low,"Pace Low"), (pace_high,"Pace High")]:
    plt.axvline(val, color="red", linestyle="--")
    plt.text(val, max(rel_freq)+1, f"{label}={val:.2f}", rotation=90, ha="center")
plt.text(24, max(rel_freq)-2, f"Pace %={percent_in_pace}", color="blue")
plt.title("Relative Frequency"); plt.xlabel("Avg Speed"); plt.ylabel("%")
plt.legend(); plt.grid(True)
plt.savefig("relative_with_annotations.png", dpi=300)
plt.close()

# Cumulative Frequency
plt.figure(figsize=(8,5))
plt.scatter(maxs, cum_freq, label="Data")
coeffs2 = np.polyfit(maxs, cum_freq, 3)
xs2 = np.linspace(maxs.min(), maxs.max(), 300)
plt.plot(xs2, np.polyval(coeffs2, xs2), label="Smooth curve")
for val, label in [(p15,"15th"), (median_val,"50th"), (p85,"85th")]:
    plt.axvline(val, color="green", linestyle="--")
    plt.text(val, 50, f"{label}={val:.2f}", rotation=90, ha="center")
plt.title("Cumulative Frequency"); plt.xlabel("Max Speed"); plt.ylabel("%")
plt.legend(); plt.grid(True)
plt.savefig("cumulative_with_annotations.png", dpi=300)
plt.close()
