import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Hashtags': ['travel', 'fitness', 'food', 'art', 'fashion'],
    'Views': [5000, 7500, 10000, 6000, 8000],
}

df = pd.DataFrame(data)

# Define a list of colors for each bar
colors = ['skyblue', 'lightcoral', 'lightgreen', 'lightsalmon', 'lightseagreen']

# Create a bar graph for 'Views' by 'Hashtags' with individual colors and background color
plt.figure(figsize=(10, 6), facecolor='whitesmoke')  # Set background color

# Customize the bar appearance and assign colors
bars = plt.bar(df['Hashtags'], df['Views'], color=colors)

# Add data labels above the bars
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords='offset points', ha='center', fontsize=12)

# Set labels and title
plt.xlabel('Hashtags', fontsize=14)
plt.ylabel('Views', fontsize=14)
plt.title('Views by Hashtags', fontsize=16)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, fontsize=12)

# Add a grid for better visualization
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust spacing and margins
plt.tight_layout()

# Show the graph
plt.show()
