# etl_project
etl project source code will go here- Kevin, Harsha and Divya


# Extract_Transform_Load_Project
Data integration Project
# Data Sources:
* For this project we gathered us job data on 2 famous web site. We used two different
CSV files to gathered the data:  
* https://www.kaggle.com/PromptCloudHQ/usbased-jobs-from-dicecom
* https://www.kaggle.com/PromptCloudHQ/us-jobs-on-monstercom

# We follow the guide line that learned from the class to perform 3 step 
# as following:

# Extraction

We load the data from above mentioned web side with csv files format.
* We took these two sources of job data and to see if there are similiar information so
we can compare the data in 2 major job board providers. We study the common
attributes on both boards. But before we profrom Transformation, we clean out the data eliminate 
all row with empty fields.

# Transformace.

We dccide to include the following attributes into our study:

date_added
job_title
job_type
location
organization/company name
sector

The data contain variance on the two sites. We have to make decision for how to rename the
attribute and make the two job boards as close as possible.
We do transformation using panda dataframe we learned from the class.

# Loading:

* We choose postgres Database and ORM model to prfrom loading part.
We use ORM to create one database and two tables. We did google search to learn how
to utilize ORM skill to create postgres database. The class show us perfome ORM
in a pre-existing sqlite; but we follow the same model to expand our knowledge.


# Challenges:
* The small project like this, it is not easy to have people with mix skill sets work together.
It hard to reach an agreement in term of what to do because team memebem came form different background.
Team members from technical background and members from project management background alway have different view point. 
some may want work more on ETL and expande knowledge on ORM; but others may have different focus.

I (kevin) suggest, in the future, this type of small project can be an individual assignment. OR, if it has to be in team work scale,
I suggest instructors define clearly like in the home work assignemt.


