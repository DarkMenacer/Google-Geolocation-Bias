# Google-Geolocation-Bias
## Selenium - Python Script to scrape web links

#### Technologies used:
    1. Python
    2. Selenium
    3. PostGreSQL

---

### Purpose

Google search results are personalised according to data collected from the users based on their geolocation, i.e , searching for the query "Hospitals near me" produces different results based on where the user is currently. 

This is a favourable outcome in most of the scenarios. But for certain queries, where results shouldn't be dependent on the geolocation, i.e. same set of links should be visible, regardless of where the user is. These include queries like "Solar System" and "Narendra Modi".

The purpose of this software is to measure whether there is any bias that is induced due to Google's Geolocation personalisation.

---
    
### Softwares Required to run

    1. Python 3 (https://www.python.org/downloads/)
    2. PostgreSQL (https://www.postgresql.org/download/)
    3. Chrome (https://www.google.com/intl/en_in/chrome/)
    4. selenium (pip install selenium)
    5. psycopg2 (pip install psycopg2)
    6. rbo (pip install rbo)
    7. undetected chromedriver (pip install undetected_chromedriver)
    8. numpy (pip install numpy)
    9. pandas (pip install pandas)
    10. matplotlib (pip install matplotlib)
    11. seaborn (pip install seaborn)
    12. geopandas (pip install geopandas)
    13. make (*recommended)


### How to use (Steps)

    1. Clone the repository and install the required softwares.
    2. Go to folder input
	    1. In the file, "db_details.py", update the database details as per your system.
	    2. Add the queries you want to search for in the "query_list.py" file.
	    3. Add the cities you to search the query in and the base city to which all other cities will be compared. 
		    1. NOTE: Add complete canonical name as per https://developers.google.com/static/adwords/api/docs/appendix/geo/geotargets-2022-08-18.csv
		    2. NOTE: Do not add base city in the city_list as it is already added.
		    3. NOTE: Do not add any city twice to avoid constraint issues in the database.
    3. To run the program:-
       1. If make is installed (highly recommended)
	       1. Update "Makefile" by adding the changing the paths of all of the mentioned files.
	       2. Enter command "make run" in the terminal opened at this folder.
       2. If make is not installed, then 
	       1. Run the file "1.scraper.py", "2.data_structure.py" and subsequent map plotters (plot_standard.py or plot_map.py) sequentially. 
		       1. NOTE: Do not start the second file before the first file is finished running (make ensures this for you).
		       2. NOTE: In case of any error, manual deletion of the database and re-creation would rectify the error.
    4. The results will be printed on the console and will also be available in the database.
       1. NOTE: Re-running the program erases the data that was stored in the database earlier.

---

### Log

    Created: 9 September 2022
    Last Edit : 13 July 2023
    
---