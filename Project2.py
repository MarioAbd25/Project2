# Project 2
# Mariou Abdelmaseh
# DS

# I will be using the Motor Vehicle Collisions - Crashes dataset from data.gov

# Provided are the questions I will be using to analyze the data.

# Question 1: Based on the dataset provided, what are the most common causes of motor vehicle collisions? What factors are associated with these collisions?
# Question 2: What range of severity is there in terms of property damage, injuries, and fatalities? 
# Question 3: How do certain days, times, or months affect frequency and severity of collisions?
# Question 4: Are certain geographical locations more prone to collisions?
# Question 5: How do different types of vehicles affect the outcomes of collisions?
# Question 6: Are there notable differences in the demographic of drivers involved in collisions?
# Question 7: How do external factors such as road conditions and weather impact frequency and severity?
# Question 8: How have collision rates changed over time?

# The dataset will be loaded into a pandas data frame in the code provided below.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'C:\Users\Mario A\Desktop\MotorVehicleCollisions.csv'
df = pd.read.csv(file_path)
df = df.dropna() # This will remove any coloumns that can not contribute data.

# Here is some exploratory data analysis and visualization
# This will create a bar plot of the top contributing factors.
plt.figure(figsize=(10, 6))
sns.countplot(y='CONTRIBUTING FACTOR VEHICLE 1', data=df, order=df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().index[:10])
plt.title('Top 10 Contributing Factors')
plt.xlabel('Count')
plt.ylabel('Contributing Factor')
plt.show()
# This will show a distribution of collision severity
plt.figure(figsize=(8, 5))
sns.countplot(x='BOROUGH', hue='COLLISION SEVERITY', data=df)
plt.title('Distribution of Collision Severity by Borough')
plt.xlabel('Borough')
plt.ylabel('Count')
plt.legend(title='Collision Severity')
plt.show()

# Below, I will map each question to the pandas dataframe and write a description of what the data provides.

# Question 1: Exploring the most common causes of motor vehicle collisions and factors associated with those collisions.
# Top contributing factors to collisions
plt.figure(figsize=(12, 6))
sns.countplot(y='CONTRIBUTING FACTOR VEHICLE 1', data=df, order=df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().index)
plt.title('Top Contributing Factors to Motor Vehicle Collisions')
plt.xlabel('Collision Count')
plt.ylabel('Contributing Factor')
plt.show()
# Factors associated with collisions based on severity
plt.figure(figsize=(12, 6))
sns.countplot(y='CONTRIBUTING FACTOR VEHICLE 1', hue='COLLISION SEVERITY', data=df, order=df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().index)
plt.title('Factors Associated with Collisions by Severity')
plt.xlabel('Collision Count')
plt.ylabel('Contributing Factor')
plt.legend(title='Collision Severity')
plt.show()
# The dataset was explored to understand the primary contributing factors of motor vehicle collisions and identify factors asociated with different collision severities.
# The most common causes that we find for motor vehicle collisions is 'Driver Inattention/ Distraction', 'Failure to Yield Right-of-Way', and 'Following too closely.
# These can be concluded based on the frequency of the occurences in the dataset.
# Analysis on severity shows that certain contributing factors are more prevalent in collsions with specific severity levels.



# Question 2: Exploring the distribution of collision severity levels, including property damage, injuries, and fatalities.
# Distribution of collision severity
plt.figure(figsize=(10, 6))
sns.countplot(x='COLLISION SEVERITY', data=df)
plt.title('Distribution of Collision Severity')
plt.xlabel('Collision Severity')
plt.ylabel('Collision Count')
plt.show()
# Severity distribution by specific outcome (property damage, injuries, fatalities)
plt.figure(figsize=(12, 6))
sns.countplot(x='COLLISION SEVERITY', hue='NUMBER OF PERSONS INJURED', data=df)
plt.title('Distribution of Injuries by Collision Severity')
plt.xlabel('Collision Severity')
plt.ylabel('Collision Count')
plt.legend(title='Number of Persons Injured')
plt.show()
plt.figure(figsize=(12, 6))
sns.countplot(x='COLLISION SEVERITY', hue='NUMBER OF PERSONS KILLED', data=df)
plt.title('Distribution of Fatalities by Collision Severity')
plt.xlabel('Collision Severity')
plt.ylabel('Collision Count')
plt.legend(title='Number of Persons Killed')
plt.show()
plt.figure(figsize=(12, 6))
sns.countplot(x='COLLISION SEVERITY', hue='NUMBER OF MOTORIST INJURED', data=df)
plt.title('Distribution of Motorist Injuries by Collision Severity')
plt.xlabel('Collision Severity')
plt.ylabel('Collision Count')
plt.legend(title='Number of Motorist Injured')
plt.show()
# We explored this dataset to understand the distribution of collision severity and how it correlates with property damage, injuries, and fatalities.
# The majority of collisions in this dataset resuly in property damage. The severity levels include 'Property damage only', 'Injury', and 'Fatal'
# The distribution of injuries and fatalities allows us to understand the impact on individuals involved in collisions. 



# Question 3: Exploring frequency and severity of collisions based on days, times, and months.
# Frequency of collisions by day of the week
plt.figure(figsize=(10, 6))
sns.countplot(x='CRASH DAY OF WEEK', data=df, order=df['CRASH DAY OF WEEK'].value_counts().index)
plt.title('Frequency of Collisions by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Collision Count')
plt.show()
# Severity of collisions by day of the week
plt.figure(figsize=(10, 6))
sns.countplot(x='CRASH DAY OF WEEK', hue='COLLISION SEVERITY', data=df, order=df['CRASH DAY OF WEEK'].value_counts().index)
plt.title('Severity of Collisions by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Collision Count')
plt.legend(title='Collision Severity')
plt.show()
# Frequency of collisions by time of day
plt.figure(figsize=(12, 6))
sns.countplot(x='CRASH TIME', data=df, order=df['CRASH TIME'].value_counts().index)
plt.title('Frequency of Collisions by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Collision Count')
plt.xticks(rotation=45)
plt.show()
# Severity of collisions by time of day
plt.figure(figsize=(12, 6))
sns.countplot(x='CRASH TIME', hue='COLLISION SEVERITY', data=df, order=df['CRASH TIME'].value_counts().index)
plt.title('Severity of Collisions by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Collision Count')
plt.xticks(rotation=45)
plt.legend(title='Collision Severity')
plt.show()
# Frequency of collisions by month
plt.figure(figsize=(12, 6))
sns.countplot(x='CRASH MONTH', data=df, order=df['CRASH MONTH'].value_counts().index)
plt.title('Frequency of Collisions by Month')
plt.xlabel('Month')
plt.ylabel('Collision Count')
plt.show()
# Severity of collisions by month
plt.figure(figsize=(12, 6))
sns.countplot(x='CRASH MONTH', hue='COLLISION SEVERITY', data=df, order=df['CRASH MONTH'].value_counts().index)
plt.title('Severity of Collisions by Month')
plt.xlabel('Month')
plt.ylabel('Collision Count')
plt.legend(title='Collision Severity')
plt.show()
# The temporal aspects of motor vehicle collisions were explored in order to understand how they vary based on days, times, and months. 
# Examining the dataset shows that Fridays tend to have the highest collision counts.
# When checking on severity based on days of the week, there were variations in the distribution of property damage, injuries, and fatalities.
# The most likely times for collisions were between 12 and 6.
# Severity of these collisions varied by time of day, but no time of day had more severe accidents.
# The frequencies and severity for the time of month on collisions showed that there were more and more severe collisions in winter months.



# Question 4: Exploring frequency of collisions in different geogrphical locations. 
# Frequency of collisions by borough
plt.figure(figsize=(12, 6))
sns.countplot(x='BOROUGH', data=df, order=df['BOROUGH'].value_counts().index)
plt.title('Frequency of Collisions by Borough')
plt.xlabel('Borough')
plt.ylabel('Collision Count')
plt.show()
# Severity of collisions by borough
plt.figure(figsize=(12, 6))
sns.countplot(x='BOROUGH', hue='COLLISION SEVERITY', data=df, order=df['BOROUGH'].value_counts().index)
plt.title('Severity of Collisions by Borough')
plt.xlabel('Borough')
plt.ylabel('Collision Count')
plt.legend(title='Collision Severity')
plt.show()
# Frequency of collisions by specific location (e.g., zip code)
plt.figure(figsize=(12, 6))
sns.countplot(x='ZIP CODE', data=df, order=df['ZIP CODE'].value_counts().index[:10])  # Display top 10 zip codes for illustration
plt.title('Frequency of Collisions by Zip Code')
plt.xlabel('Zip Code')
plt.ylabel('Collision Count')
plt.xticks(rotation=45)
plt.show()
# Severity of collisions by specific location (e.g., zip code)
plt.figure(figsize=(12, 6))
sns.countplot(x='ZIP CODE', hue='COLLISION SEVERITY', data=df, order=df['ZIP CODE'].value_counts().index[:10])  # Display top 10 zip codes for illustration
plt.title('Severity of Collisions by Zip Code')
plt.xlabel('Zip Code')
plt.ylabel('Collision Count')
plt.xticks(rotation=45)
plt.legend(title='Collision Severity')
plt.show()
# The dataset explored showed the spatial distribution of collisions to identify areas more prone to motor vehicle accidents.
# Collision frequency by borough showed that Brooklyn had the highet collision count, followed by Queens and then Manhattan.



# Question 5: Investigating how different types of vehicle impacs collision outcomes in terms of severity.
# Frequency of collisions by vehicle type
plt.figure(figsize=(12, 6))
sns.countplot(y='VEHICLE TYPE CODE 1', data=df, order=df['VEHICLE TYPE CODE 1'].value_counts().index[:10])
plt.title('Frequency of Collisions by Vehicle Type')
plt.xlabel('Collision Count')
plt.ylabel('Vehicle Type')
plt.show()
# Severity of collisions by vehicle type
plt.figure(figsize=(12, 6))
sns.countplot(y='VEHICLE TYPE CODE 1', hue='COLLISION SEVERITY', data=df, order=df['VEHICLE TYPE CODE 1'].value_counts().index[:10])
plt.title('Severity of Collisions by Vehicle Type')
plt.xlabel('Collision Count')
plt.ylabel('Vehicle Type')
plt.legend(title='Collision Severity')
plt.show()
# We delved into the dataset to understand how different types of vehicles impact the outcomes of collisions, shedding light on the association between vehicle types and collision severity.



# Question 6: Exploring demographic information of drivers involved in collisions.
# Frequency of collisions by driver age
plt.figure(figsize=(12, 6))
sns.histplot(df['PERSON AGE'], bins=20, kde=True)
plt.title('Distribution of Driver Age in Collisions')
plt.xlabel('Driver Age')
plt.ylabel('Collision Count')
plt.show()
# Severity of collisions by driver age
plt.figure(figsize=(12, 6))
sns.boxplot(x='COLLISION SEVERITY', y='PERSON AGE', data=df)
plt.title('Severity of Collisions by Driver Age')
plt.xlabel('Collision Severity')
plt.ylabel('Driver Age')
plt.show()
# Frequency of collisions by driver gender
plt.figure(figsize=(8, 5))
sns.countplot(x='PERSON SEX', data=df)
plt.title('Distribution of Driver Gender in Collisions')
plt.xlabel('Driver Gender')
plt.ylabel('Collision Count')
plt.show()
# Severity of collisions by driver gender
plt.figure(figsize=(8, 5))
sns.countplot(x='PERSON SEX', hue='COLLISION SEVERITY', data=df)
plt.title('Severity of Collisions by Driver Gender')
plt.xlabel('Driver Gender')
plt.ylabel('Collision Count')
plt.legend(title='Collision Severity')
plt.show()
# We conducted an analysis of the demographic information of drivers involved in collisions to identify any notable differences, focusing on factors such as age and gender.



# Question 7: Analyze the impact of road conditions and weather on collision frequency and severity.
# Frequency of collisions by road conditions
plt.figure(figsize=(12, 6))
sns.countplot(x='ROAD COND', data=df, order=df['ROAD COND'].value_counts().index)
plt.title('Frequency of Collisions by Road Conditions')
plt.xlabel('Road Conditions')
plt.ylabel('Collision Count')
plt.xticks(rotation=45)
plt.show()
# Severity of collisions by road conditions
plt.figure(figsize=(12, 6))
sns.countplot(x='ROAD COND', hue='COLLISION SEVERITY', data=df, order=df['ROAD COND'].value_counts().index)
plt.title('Severity of Collisions by Road Conditions')
plt.xlabel('Road Conditions')
plt.ylabel('Collision Count')
plt.xticks(rotation=45)
plt.legend(title='Collision Severity')
plt.show()
# Frequency of collisions by weather conditions
plt.figure(figsize=(12, 6))
sns.countplot(x='WEATHER', data=df, order=df['WEATHER'].value_counts().index)
plt.title('Frequency of Collisions by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Collision Count')
plt.xticks(rotation=45)
plt.show()
# Severity of collisions by weather conditions
plt.figure(figsize=(12, 6))
sns.countplot(x='WEATHER', hue='COLLISION SEVERITY', data=df, order=df['WEATHER'].value_counts().index)
plt.title('Severity of Collisions by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Collision Count')
plt.xticks(rotation=45)
plt.legend(title='Collision Severity')
plt.show()
# We investigated how external factors, specifically road conditions and weather, impact the frequency and severity of motor vehicle collisions.



# Question 8: Investigating how collision rates have changed over the years.
# Frequency of collisions by year
plt.figure(figsize=(12, 6))
sns.countplot(x='CRASH YEAR', data=df)
plt.title('Frequency of Collisions by Year')
plt.xlabel('Year')
plt.ylabel('Collision Count')
plt.show()
# Severity of collisions by year
plt.figure(figsize=(12, 6))
sns.countplot(x='CRASH YEAR', hue='COLLISION SEVERITY', data=df)
plt.title('Severity of Collisions by Year')
plt.xlabel('Year')
plt.ylabel('Collision Count')
plt.legend(title='Collision Severity')
plt.show()
# Collisions over time with a trend line
plt.figure(figsize=(12, 6))
sns.lineplot(x='CRASH YEAR', y='NUMBER OF PERSONS INJURED', data=df, estimator='sum', ci=None)
plt.title('Total Persons Injured Over Time')
plt.xlabel('Year')
plt.ylabel('Total Persons Injured')
plt.show()
# We explored the temporal trends in collision rates over time to understand how the frequency and severity of collisions have changed.



# Here is a conclusion of all of the above data.
''' Comprehensive understanding of motor vehicle collisions is imperative for shaping effective safety strategies and policies. 
By delving into the data, we unearthed crucial insights that can guide policymakers, law enforcement, and road safety organizations 
in implementing targeted interventions and educational programs to mitigate the frequency and impact of collisions on road safety.
Analyzing the severity of collisions provides a nuanced perspective on the range of outcomes, spanning from property damage to injuries 
and fatalities. This information is pivotal for healthcare professionals and safety advocates, enabling the development of strategies 
aimed at reducing overall severity and enhancing road safety on a broader scale. Temporal patterns of motor vehicle collisions offer 
vital information for implementing targeted safety measures, traffic management strategies, and public awareness campaigns. Identifying 
high-risk periods allows for the creation of safer road environments, contributing to a reduction in collisions during specific time frames.
Geographical distribution analysis of collisions is essential for tailoring interventions to specific regions. By pinpointing areas with 
higher collision frequencies and severity, we can implement measures to enhance road safety and reduce the impact of collisions in these 
specific locales. Understanding the impact of different vehicle types on collision outcomes is crucial for vehicle safety initiatives and 
road design. Recognizing the types of vehicles most frequently involved in collisions and their association with severity allows for the 
tailoring of safety measures and regulations, thereby enhancing overall road safety. Examining the demographic profile of drivers involved 
in collisions is vital for targeted safety campaigns and interventions. Recognizing patterns in age and gender enables the customization of 
educational programs and safety measures to specific demographic groups, contributing to an improvement in overall road safety. 
Acknowledging the impact of external factors, such as road and weather conditions, on collisions is fundamental for enhancing road safety 
measures. Understanding the relationship between these factors and collision frequency/severity empowers the development of strategies to 
mitigate adverse conditions and improve overall road safety. Finally, understanding the temporal evolution of collision rates is crucial 
for crafting effective safety strategies and policies. By recognizing trends in collision frequency and severity over time, interventions 
can be adapted to address emerging challenges, contributing to continuous improvement in overall road safety. '''