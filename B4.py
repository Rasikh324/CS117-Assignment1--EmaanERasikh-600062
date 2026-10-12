# Finds the longest streak of strictly decreasing voltage readings

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

longest_streak = 1
starting_value = 0
ending_value = 0
current_streak = 1
current_start = voltages[0]



for i in range(1,len(voltages)):
    if voltages[i-1] > voltages[i]:
        current_streak += 1
    else:
        current_start = voltages[i]
        current_streak = 1

    if current_streak > longest_streak:
        longest_streak = current_streak
        starting_value = current_start
        ending_value = voltages[i]



print(f"Longest continuous drop: {longest_streak} minutes")
print(f"Started at: {starting_value} V")
print(f"Ended at: {ending_value} V")


