import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('race_data.csv', parse_dates=['Date/Time (UTC)'])

df.sort_values('Date/Time (UTC)', inplace=True)

window_size = 500
df['WPM_Smooth'] = df['WPM'].rolling(window=window_size).mean()
df['Accuracy_Smooth'] = df['Accuracy'].rolling(window=window_size).mean()
formatted_date = datetime.now().strftime("%B %d, %Y")

plt.figure(figsize=(14, 7))
ax1 = plt.gca()  # WPM
ax2 = ax1.twinx()  # Accuracy

ax1.plot(df['Date/Time (UTC)'], df['WPM_Smooth'], linestyle='-', color='b', label='WPM (Smoothed)')
ax1.set_xlabel('Date/Time (UTC)')
ax1.set_ylabel('Words Per Minute (WPM)', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True)

ax2.plot(df['Date/Time (UTC)'], df['Accuracy_Smooth'], linestyle='-', color='r', label='Accuracy (Smoothed)')
ax2.set_ylabel('Accuracy', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title(f'Words Per Minute and Accuracy Over Time out of {len(df)} Races by {formatted_date}')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
