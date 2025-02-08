import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Generating random weather data
np.random.seed(42)
days = pd.date_range(start='1/10/2025', end='1/10/2026', freq='D')
temperature = np.random.normal(loc=20, scale=5, size=len(days))  # Mean temperature 20°C, std 5°C
humidity = np.random.uniform(low=30, high=90, size=len(days))  # Humidity between 30% and 90%
wind_speed = np.random.uniform(low=0, high=15, size=len(days))  # Wind speed between 0 and 15 m/s

# Creating a DataFrame
weather_data = pd.DataFrame({'Day': days, 'Temperature': temperature, 'Humidity': humidity, 'Wind Speed': wind_speed})
print(weather_data.head())

'''
# Data Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(x='Day', y='Temperature', data=weather_data, label='Temperature (°C)')
plt.title('Temperature Variation Over Time')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.show()
'''

# Line chart for humidity trends
plt.figure(figsize=(14, 7))
sns.lineplot(x='Day', y='Humidity', data=weather_data, color='green')
plt.title('Humidity Trends Over a Year')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.show()

# Line chart for wind speed trends
plt.figure(figsize=(14, 7))
sns.lineplot(x='Day', y='Wind Speed', data=weather_data, color='red')
plt.title('Wind Speed Trends Over a Year')
plt.xlabel('Date')
plt.ylabel('Wind Speed (m/s)')
plt.show()