import pandas as pd
import matplotlib.pyplot as plt

# Problem set 6: Getting, cleaning, and checking your data

# Part A. Getting your data.

# In this project I am importing three CSVs: salaries-us.csv, which was scraped from HackerRank in 2016, salaries-ar.csv, which is from 2023 in Argentina, eand salaries-india.csv, which was scraped from GlassDoor in 2022. The datasets include varying and detailed kinds of information like pay rates, geographical relevance, job titles and their categories, as well as categories less relevant to our analysis like ratings or comments. I am using pandas to read the CSVs into dataframes.

# Use pandas to read the CSV file into a DataFrame
us_eu_salaries = pd.read_csv('source/salaries-us.csv')
in_salaries = pd.read_csv('source/salaries-in.csv')
ar_salaries = pd.read_csv('source/salaries-ar.csv')

# RESEARCH QUESTIONS

# Questions for each country:
# How does compensation vary between countries depending on the following:
#   the job title? E.g. How much more do Android Devs make than Web Devs, etc.?
#   the company? E.g. Does Apple pay significantly more than Expedia for the same role?
#   location? E.g. What's the opportunity cost of working in Bangalore vs Delhi, or Miami vs New York?
#   other factors? E.g. Does having more experience mean you get paid more? Does having more experience at the same company mean you get paid more?

# TABLE PLAN

# TABLE 1: Tech Salaries:
#	[employer_name] [location_name] [location_state] [location_country] [job_title] [job_title_category] [job_title_rank] [total_experience_years] [employer_experience_years] [annual base pay] [signing bonus] [annual bonus] [stock_value_bonus] [total compensation]

# TABLE 2: Indian Salaries:
#	[employer_name] [location_name] [job_title] [annual base pay] [employment_status] [job_roles]
# All the currencies will be converted into USD for ease of comparison. I will be using the current conversion rate, which is 1 Indian Rupee equals 0.012 United States Dollar.

# TABLE 3: Both:
# From there, I will merge the two tables into a new table that has the following columns. I will be more strict about removing interns so that it will only be a comparison of full-time employees across India and western countries.
# [employer_name] [location_name] [job_title] [annual base pay] 

# 3.  Write the code needed to take the data you loaded in and produce the table or tables that you want for your preliminary analysis plan. By the end of this part of your script you should have a dataframe or a few dataframes that are appropriate for your analysis. (Again, most likely you will revisit and revise this code later when you are actually doing the analysis and realize you need to change the data cleaning “upstream.”)

# First, I need to clean both datasets so that they are more or less equivalent. I will do this by standardizing the column names, removing unnecessary columns, and converting the currencies into USD. I will also try to standardize the location format so that I can compare them more easily.

#So I can see it better
pd.set_option('display.max_columns', None)

# TECH SALARIES 

# To start, there were several vulgar/spam/unvalidated entries under category "Other", and some jobs that weren't tech related whatsoever that I wanted to remove. However, some "Other" entries were also real and valuable. I checked what would happen if I had a strict approach to data cleaning:

# Apply the query to get the new DataFrame
# strict_us_eu_salaries = us_eu_salaries.query('(job_title_category != "Other")' )
# print(strict_us_eu_salaries.head())
# print("Shape of the strict-Other-filtered DataFrame:", strict_us_eu_salaries.shape)

#That removed quite a lot of relevant entries (1655 -> 1366 entries), which means we should take a more careful approach. I noticed that many of the real "Other" jobs had a longitude and latitude, so I modified my query as follows:

query_string = (
    '(job_title_category != "Other") | ((job_title_category == "Other") & (location_latitude.notnull() & location_longitude.notnull()))'
)
# Apply the query to get the new DataFrame
filt_us_eu_salaries = us_eu_salaries.query(query_string)

#That cut things down to 1500 entries and removed most of the spam, which was a happy trade-off for me. 

# I then added the 13th column (total compensation, but only if there are valid values for it)
compensation = ['annual_base_pay', 'signing_bonus', 'annual_bonus', 'stock_value_bonus']
filt_us_eu_salaries = filt_us_eu_salaries.copy()  # Create a copy to avoid the warning
filt_us_eu_salaries['total'] = filt_us_eu_salaries[compensation].apply(lambda row: sum(val for val in row if pd.notna(val) and isinstance(val, (int, float))), axis=1)

# Added a column field to replace index
filt_us_eu_salaries['country'] = 'US/EU'
# Move the 'country' column to position 0
columns = ['country'] + [col for col in filt_us_eu_salaries.columns if col != 'country']
filt_us_eu_salaries = filt_us_eu_salaries[columns]

# I finished off cleaning this dataset by removing columns irrelevant to our analysis going forward.
columns_to_drop = ['index', 'job_title_category', 'job_title_rank', 'salary_id','location_latitude', 'location_longitude', 'comments', 'submitted_at']
us_eu_df = filt_us_eu_salaries.drop(columns=columns_to_drop)


# INDIA SALARIES
# There were basically no spam or errors in this dataset. The biggest thing to resolve for the Indian salary dataset was "Number of Salaries Reported" -- I wanted that to flatten out so that every salary reported had its own row. 

# Create a new DataFrame by repeating rows based on the "Salaries Reported" column
india_df = in_salaries.loc[in_salaries.index.repeat(in_salaries['Salaries Reported'])]

# Reset the index to get a new default integer index
india_df.reset_index(drop=True, inplace=True)

# Drop the "Salaries Reported" column
india_df.drop('Salaries Reported', axis=1, inplace=True)

# I also renamed columns to match the format the other dataframe:
india_df.rename(columns={
    'Company Name': 'employer_name',
    'Location': 'location_name',
    'Job Title': 'job_title',
    'Salary': 'annual_base_pay',
    'Employment Status': 'employment_status',
    'Job Roles': 'job_roles'
}, inplace=True)

#Convert the values in the "annual_base_pay" column to USD currency
# Conversion rate from Indian Rupee to USD
conversion_rate = 0.012

# Convert values in the "annual_base_pay" column to USD
india_df['annual_base_pay'] = india_df['annual_base_pay'] * conversion_rate

# Replace Ratings Column with India
india_df['country'] = 'India'
india_df = india_df.rename(columns={india_df.columns[0]: 'old_column_name'})

# Move the 'country' column to position 0
columns = ['country'] + [col for col in india_df.columns if col != 'country']
india_df = india_df[columns]

# Drop the original first column
india_df = india_df.drop(columns=['old_column_name'])

#And I was happy with that!

# ARGENTINA SALARIES
# This dataset needed to be translated, and for irrelevant text-based columns to be removed. 

# 1. Keep only selected columns
selected_columns = ar_salaries.iloc[:, [0, 1, 2, 3, 4, 17, 18, 19, 20, 21, 22, 30, 35, 36, 37, 45, 46, 48]]
ar_df = ar_salaries.iloc[:, [0, 1, 2, 3, 4, 17, 18, 19, 20, 21, 22, 30, 35, 36, 37, 45, 46, 48]]
#I'm using iloc here because it's way too hard to remember the spanish names, sorry

# 2. Rename columns to English equivalent
english_columns = [
    "employment_status",
    "location_name",
    "dedication",
    "contract_type",
    "monthly_salary_or_withdrawal",
    "satisfaction_with_income",
    "looking_for_job",
    "job_title",
    "years_of_experience",
    "seniority_in_company",
    "time_in_position",
    "work_modality",
    "state",
    "career",
    "university",
    "age",
    "gender_identity",
    "seniority"
]

ar_df.columns = english_columns

# 3. Loop through entries to roughly translate responses
translations = {
    'Ciudad Autónoma de Buenos Aires': 'Buenos Aires City',
    'Remoto (empresa de otro país)': 'Remote (foreign company)',
    'Tercerizado (trabajo a través de consultora o agencia)': 'Contract',
    'Staff (planta permanente)': 'Staff (permanent)',
    'Sí, estoy buscando activamente.': 'Yes, I am actively looking.',
    'No, estoy muy conforme.': 'No, I am very satisfied.',
    'No, pero escucho ofertas.': 'No, but I am open to offers.',
    'Híbrido (presencial y remoto)': 'Hybrid (in-person and remote)',
    'En curso': 'In progress',
    'Completo': 'Completed',
    'Incompleto': 'Incomplete',
    'Universitario': 'University degree',
    'Terciario': 'Tertiary degree',
    'Secundario': 'Secondary degree',
    'Varón Cis': 'Male',
    'Mujer Cis': 'Female',
}

# Create a copy of the DataFrame to avoid SettingWithCopyWarning
ar_df = ar_df.copy()

# Convert to USD and multiply by 12
exchange_rate = 0.0028
ar_df["annual_base_pay"] = ar_df["monthly_salary_or_withdrawal"] * exchange_rate * 12

# Drop the original column
ar_df.drop(columns=["monthly_salary_or_withdrawal"], inplace=True)
ar_df.rename(columns={"employment_status": "country"}, inplace=True)

# Loop through each entry to replace Spanish to English
for column in ar_df.columns:
    ar_df.loc[:, column] = ar_df[column].replace(translations)

# Make CSVs
ar_df.to_csv('cleaned/salaries-ar-cleaned.csv', index=False)
india_df.to_csv('cleaned/salaries-in-cleaned.csv', index=False)
us_eu_df.to_csv('cleaned/salaries-us-cleaned.csv', index=False)

# CHECKING DATA

# Distribution Histogram
def perform_data_checks(df, df_name):
    column = "annual_base_pay"
    plt.hist(df[column], bins=50)  # You can adjust the number of bins as needed
    plt.title(f"Annual Base Pay Distribution in {df_name}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

#After I ran the histograms, I found that there were several outlier values to remove which were distorting the data and making the scale go all the way from 0 to 1.0 in 1e7 (i.e. go up to the 10 millions), and concentrating everything on the left in a sharp spike. I will remove them here by using IQR to remove outliers (and I will also remove any rows with empty values that might still be hanging around).

def remove_empty_and_outliers_iqr(df, column, multiplier=6):

    # Calculate Q1, Q3, and IQR
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    # Define the lower and upper bounds for outlier detection
    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr

    # Remove outliers
    df_no_outliers = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    # Remove empty values
    df_cleaned = df_no_outliers[(df_no_outliers['annual_base_pay'].notna()) & (df_no_outliers['annual_base_pay'] != 0)]

    return df_cleaned

# # Remove outliers 
us_eu_df = remove_empty_and_outliers_iqr(us_eu_df, "annual_base_pay")
india_df = remove_empty_and_outliers_iqr(india_df, "annual_base_pay")
ar_df = remove_empty_and_outliers_iqr(ar_df, "annual_base_pay")

#I'm happy with this and will now proceed with my actual data analysis.

#DATA ANALYSIS

#1 Given the same role (Developer / Engineer), how much does each country pay on average?

# Concatenate the dataframes into one for easier processing
all_df = pd.concat([us_eu_df, india_df, ar_df])

# Filter rows containing 'Developer' or 'Engineer' in the job_title column (case-insensitive)
developer_engineer_df = all_df[all_df['job_title'].str.contains('developer|engineer', case=False, regex=True)]

# Group by country and compute the average pay, as well as the count of entries
average_pay_by_country = developer_engineer_df.groupby('country')['annual_base_pay'].agg(['mean', 'count']).reset_index()
average_pay_by_country.columns = ['country', 'annual_base_pay', 'entry_count']

print(average_pay_by_country.head())

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(average_pay_by_country['country'], average_pay_by_country['annual_base_pay'], color=['blue', 'orange', 'green'])
plt.xlabel('Country')
plt.ylabel('Average Annual Base Pay')
plt.title('Average Pay for Developer/Engineer Roles by Country')
plt.show()

#1.5 compared with cost of living

expenses_data = {
    'Country': ['US/EU', 'India', 'Argentina'],
    'Monthly Expenses (USD)': [3040.1, 596.8, 715.38],
    'Yearly Expenses (USD)': [36481.2, 7161.6, 8584.56]
}

expenses_df = pd.DataFrame(expenses_data)

# Merge average pay and expenses data
merged_df = pd.merge(average_pay_by_country, expenses_df, left_on='country', right_on='Country', how='left')
print(merged_df.head())

# Extract relevant data for plotting
countries = merged_df['country']
base_pay = merged_df['annual_base_pay']
yearly_expenses = merged_df['Yearly Expenses (USD)']

# Set up the bar positions
bar_width = 0.35
index = range(len(countries))

# Plot the bars
plt.bar(index, base_pay, bar_width, label='Annual Base Pay')
plt.bar([i + bar_width for i in index], yearly_expenses, bar_width, label='Yearly Expenses')

# Customize the plot
plt.xlabel('Country')
plt.ylabel('Amount (USD)')
plt.title('Annual Base Pay and Yearly Expenses by Country')
plt.xticks([i + bar_width/2 for i in index], countries)
plt.legend()

# Show the plot
plt.show()


#2-3 What are the top 5 highest paid positions and regions in each country?

def top_pivot(df, column_name):
    # Compute average annual base pay and count for each unique value in the specified column
    avg_pay_and_count_by_column = df.groupby(column_name)['annual_base_pay'].agg(['mean', 'count'])
    # Create a new dataframe with the computed averages and counts
    avg_pay_df = pd.DataFrame(avg_pay_and_count_by_column).reset_index()
    # Sort the dataframe by average pay in descending order
    avg_pay_df = avg_pay_df.sort_values(by='mean', ascending=False)
    # Take the top 5 highest paid positions
    top_5_positions = avg_pay_df.head(5)
    # Create a pivot table to rank the top 5 positions
    pivot_table = top_5_positions.pivot_table(index=column_name, values='mean', aggfunc=['mean', 'count'])
    # Sort the pivot table in descending order by average pay
    pivot_table = pivot_table.sort_values(by=('mean', 'mean'), ascending=False)
    return pivot_table
# Top 5 highest paid positions in each country

us_eu_top_paid_positions = top_pivot(us_eu_df, "job_title")
print("\nUS/EU Top 5 Highest Paid Positions:")
print(us_eu_top_paid_positions)

india_top_paid_positions = top_pivot(india_df, "job_title")
print("\nIndia Top 5 Highest Paid Positions:")
print(india_top_paid_positions)

ar_top_paid_positions = top_pivot(ar_df, "job_title")
print("\nArgentina Top 5 Highest Paid Positions:")
print(ar_top_paid_positions)

# Top 5 highest paid regions in each country

us_eu_top_regions = top_pivot(us_eu_df, "location_name")
print("\nUS/EU Top 5 Highest Paid Locations:")
print(us_eu_top_regions)

india_top_regions = top_pivot(india_df, "location_name")
print("\nIndia Top 5 Highest Paid Locations:")
print(india_top_regions)

ar_top_regions = top_pivot(ar_df, "location_name")
print("\nArgentina Top 5 Highest Paid Locations:")
print(ar_top_regions)

# Top 5 highest paid companies in each country

# us_eu_top_companies = top_pivot(us_eu_df, "employer_name")
# print("\nUS/EU Top 5 Highest Paying Companies:")
# print(us_eu_top_companies)

# india_top_companies = top_pivot(india_df, "employer_name")
# print("\nIndia Top 5 Highest Paying Companies:")
# print(india_top_companies)

#4 What is the difference between pay for different kinds of developers in India?

def plot_average_pay(df, country_name):
    # Get the most common job titles
    most_common_job_titles = df['job_title'].value_counts().head(10).index

    # Filter the DataFrame to include only the most common job titles
    filtered_df = df[df['job_title'].isin(most_common_job_titles)]

    # Group by job title and compute the average pay
    average_pay_by_job_title = filtered_df.groupby('job_title')['annual_base_pay'].mean().reset_index()

    # Sort the dataframe by average pay in descending order
    average_pay_by_job_title = average_pay_by_job_title.sort_values(by='annual_base_pay', ascending=False)

    # Plot the bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(average_pay_by_job_title['job_title'], average_pay_by_job_title['annual_base_pay'], color='skyblue')
    plt.xlabel('Job Title')
    plt.ylabel('Average Annual Base Pay')
    plt.title(f'Average Pay for Top 10 Most Common Job Titles in {country_name}')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.tight_layout()
    plt.show()

# Assuming you have DataFrames ar_df, us_eu_df, and india_df
plot_average_pay(ar_df, 'Argentina')
plot_average_pay(us_eu_df, 'US/EU')
plot_average_pay(india_df, 'India')

#5 What is the difference between pay for men and women developers in Argentina?

# Filter rows for the specified job titles and non-null gender identities
selected_job_titles = ['Developer', 'UX Designer', 'Data Engineer', 'Project Manager', 'Consultant', 'QA / Tester']

# Filter the dataframe for the specified job titles and valid gender identities
filtered_df = ar_df[
    (ar_df['job_title'].isin(selected_job_titles)) &  # Job title filter
    (ar_df['gender_identity'].isin(['Male', 'Female']))  # Gender filter
]

# Create a pivot table comparing compensation for job titles by gender
pivot_table = pd.pivot_table(filtered_df, values='annual_base_pay', index='job_title', columns='gender_identity', aggfunc='mean')


# Plot the bar graph
pivot_table.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Job Title')
plt.ylabel('Average Annual Base Pay')
plt.title('Comparison of Compensation by Job Title in Argentina (Male vs. Female)')
plt.legend(title='Gender', loc='upper right')
plt.tight_layout()  # Add space to the bottom
plt.show()

# Add a row showing the difference between men and women's salary
pivot_table['Salary_Difference'] = pivot_table['Male'] - pivot_table['Female']

print("\n")
# Display the pivot table
print(pivot_table)