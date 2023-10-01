import matplotlib.pyplot as plt

# Data
hashtags = ['travel', 'fitness', 'food', 'art', 'fashion']
views = [5000, 7500, 10000, 6000, 8000]

# Create a pie chart
plt.figure(figsize=(8, 8))

# Define colors for each section
colors = ['skyblue', 'lightcoral', 'lightgreen', 'lightsalmon', 'lightseagreen']

# Explode a section if needed (e.g., 'travel')
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice (travel)

# Create the pie chart
plt.pie(views, labels=hashtags, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode)

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

# Add a title
plt.title('Distribution of Views by Hashtags')

# Show the pie chart
plt.show()
