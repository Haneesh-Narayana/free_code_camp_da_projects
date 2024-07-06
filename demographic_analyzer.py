import pandas as pd

def analyze_demographic_data(data_path):


  # Read data using pandas
  df = pd.read_csv(data_path)

  # 1. How many people of each race are represented?
  race_counts = df['race'].value_counts()

  # 2. What is the average age of men?
  average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

  # 3. What percentage of people have a Bachelor's degree?
  pct_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

  # 4. Percentage of advanced education earners making >50K
  advanced_degrees = ['Bachelors', 'Masters', 'Doctorate']
  df_filtered = df[df['education'].isin(advanced_degrees)]
  pct_advanced_over_50k = round((df_filtered['income'] == '>50K').mean() * 100, 1)

  # 5. Percentage of non-advanced education earners making >50K
  non_advanced_degrees = df[~df['education'].isin(advanced_degrees)]
  pct_non_advanced_over_50k = round((non_advanced_degrees['income'] == '>50K').mean() * 100, 1)

  # 6. Minimum number of hours worked per week
  min_hours_worked = df['hours.per.week'].min()

  # 7. Percentage of minimum-hour workers making >50K
  df_min_hours = df[df['hours.per.week'] == min_hours_worked]
  pct_min_hours_over_50k = round((df_min_hours['income'] == '>50K').mean() * 100, 1)

  # 8. Country with highest percentage earning >50K
  high_earn_countries = (df[df['income'] == '>50K']['native.country'].value_counts() / df['native.country'].value_counts()) * 100
  highest_earn_country = high_earn_countries.idxmax()
  highest_earn_pct = round(high_earn_countries.max(), 1)

  # 9. Most popular occupation for >50K earners in India
  india_over_50k = df[(df['income'] == '>50K') & (df['native.country'] == 'India')]
  most_pop_occupation_india = india_over_50k['occupation'].mode().iloc[0] if not india_over_50k.empty else None

  # Return results as a dictionary
  return {
      "race_counts": race_counts,
      "average_age_men": average_age_men,
      "pct_bachelors": pct_bachelors,
      "pct_advanced_over_50k": pct_advanced_over_50k,
      "pct_non_advanced_over_50k": pct_non_advanced_over_50k,
      "min_hours_worked": min_hours_worked,
      "pct_min_hours_over_50k": pct_min_hours_over_50k,
      "highest_earn_country": highest_earn_country,
      "highest_earn_pct": highest_earn_pct,
      "most_pop_occupation_india": most_pop_occupation_india
  }

# Example usage (replace 'path/to/your/data.csv' with your actual file path)
results = analyze_demographic_data('adult.csv')

# Print the results
for key, value in results.items():
  print(f"{key}: {value}")
