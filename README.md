# Research_SOE

Software Enginnering Research Project

In this research project we have devised an algorithm to predict the relationship (any kind of relationship) between any pair of given bugs. This algorithm takes input from all the previous relationships between the bugs and predicts the extent of any new relationship between any new pairs of bugs.


First run pip install -r requirements.txt

How to Create Merged Table of metapaths

=====================================

    Bullet list:
    
        * First insert data in temp_author.csv , temp_component.csv , temp_file.csv

            * Format of inserting data in these three files :

                * First line issue_id,(author|component|file) (comma separated (**ALERT** : no comma in issue_id or (author|component|file)))
                    **(this is necessary line)**
                * subsequent lines are obviously similar to  the first line actual_data is inserted here

        * Insert summary+description of all bugs in corpse1.csv remember to remove all **\n** characters from summary + description 
        * Insert data into sample.csv 

            * Format of inserting data in sample.csv :

                * First line issue_id~combined (comma separated (**ALERT** : no **~** in issue_id or combine))
                    **(this is necessary line)**
                * subsequent lines are obviously similar to  the first line actual_data is inserted here.
        * Then Run sh final.sh
