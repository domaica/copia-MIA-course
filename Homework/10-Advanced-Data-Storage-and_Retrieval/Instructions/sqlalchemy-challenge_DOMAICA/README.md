# SQLAlchemy Homework - Surfs Up! - DOMAICA


## Solution 

Main folder for solution is called: sqlalchemy-challenge_DOMAICA

Inside that folder, we can find solution files which are contained in 4 different subfolders in proper sequence:

- 1_Data_Exploration_and_Engineering
- 2_Climate_Analysis
- 3_Climate_App
- 4_BONUS


## - 1_Data_Exploration_and_Engineering folder content

#### * 1_Data_engineering_FINAL.ipynb

Using jupyter, main tasks were inspecting .csv provided with temperature observations by date and data about weather stations 
Retrieved data inside the CSV files to see if it needed to be cleaned, reading the CSV files with pandas. 
After that moving records to sqlite cleaned db.


## - 2_Climate_Analysis folder content

#### * climate_analysis_v4.ipynb

Using jupyter, main tasks were opening sqlite database
Check tables inside db
Get dates, formats
Calculate precipitations within a specific year
Create dataframes plotting 
For precipitations and temperature observations as requested


## - 3_Climate_App folder content


#### * climate_app_v2.py
#### * screenshots of climate_app_v2.py running.pptx. This powerpoint contains screenshots of application outputs

'climate_app_v2.py' has been built with Visual Studio Code, is an app able to retrieve informations from sqlite database and publish it in internet
in JSON formats.

To do that created a Flask so we query the database data and as return we retrieve info published in different required routes
in JSON formats


## 4_BONUS folder content

#### * temp_analysis_bonus_1.ipynb

Build in Jupyter, importing data from .csv and creating dataframes. Main analysis is compare June and December temperatures across every year of the population samples and conclusion is a ttest.

My conclusions are:

We are using a paired sample t-test because we are comparing means from the same group at different times. Unpaired t-test are used to compare means of different groups.

Regarding results, we can see that t-test is very close to 0 and of course much less than the typical reference pvalue of 0.05. Then we can affirm that (for the sample values observed) there is no statistically significant difference between temperature means in June and December in Hawaii. 


#### * temp_analysis_bonus_2.ipynb

Made in Jupyter

After extracting queries from sqlite database create functions to calculate normal statistics for temperature observations within>
a date range and plot them.

Later there are calculations of precipitation values 

for a specific year grouped by station
for a specific date-month across all the years in the sample data, grouped by station and plot them

