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
    8. make (*recommended)
    9. Firefox (*optional)(https://www.mozilla.org/en-US/firefox/new/)
    10. Geckodriver (*optional)(https://github.com/mozilla/geckodriver/releases)


### How to use (Steps)

    1. Clone the repository and install the required softwares.
    2. In the file, "consts_fxns.py", update the database details as per your system (ignore GECKO_PATH if Firefox isn't used).
    3. Add the queries you want to search for in the "query_list.py" file.
    4. Add the cities you to search the query in and the base city to which all other cities will be compared. (Complete canonical name as per https://developers.google.com/static/adwords/api/docs/appendix/geo/geotargets-2022-08-18.csv)
       1. NOTE: Do not add base city in the city_list as it is already added.
       2. NOTE: Do not add any city twice to avoid constraint issues in the database.
    5. To run the program:-
       1. If make is installed (highly recommended) then firstly update "Makefile" by adding the paths and enter command "make run" in the terminal opened at this folder.
       2. If make is not installed, then first run the file "scraper.py" and then "data_structure.py" sequentially. Do not start the second file before the first file is finished running (make ensures this for you).
    6. The results will be printed on the console and will also be available in the database.
       1. NOTE: Re-running the program erases the data that was stored in the database earlier.

---

### Log

    Created: 9 September 2022
    Last Edit : 27 November 2022
    
---

#### Additional Info (can be skipped)

There are totally 4 versions of the scraper code.\
    1. Firefox Same Window\
    2. Firefox New Window\
    3. *Chrome New Window\
    4. Chrome Same Window (default)

Here "Same Window" implies that all queries for all cities will be executed on the same browser instance whereas "New Window" implies that for every query a new browser window would be opened.
Each of this versions can be obtained through looking at the commit histories of the repository and copying the needed version of scraper.py accordingly

If Firefox codes are chosen, then additionally geckodriver would be needed and the path in "consts_fxns.py" needs to be updated accordingly.

Note: The code for scraper.py for Chrome New Window is erroneous and doesn't work, any help on the matter will be highly appreciated.


---

