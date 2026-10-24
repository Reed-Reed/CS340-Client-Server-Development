# CS340-Client-Server-Development

About the Project/Project Title
The international rescue-animal training company Grazioso Salvare commissioned this software for the purpose of categorizing data provided by animal shelters. Users at Grazioso Salvare will access the database via a client-facing web application dashboard. 

Motivation
	Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. This software will use data provided by animal shelters to more easily identify those candidates. 

Getting Started
Set up the animal shelter database in Mongo. Copy a folder of datasets to your server environment. The following commands import the database to mongo and configure the service user. 
i.	cd ./datasets
ii.	mongoimport --type=csv --headerline --db aac --collection animals --drop ./aac_shelter_outcomes.csv
iii.	mongosh
iv.	use admin
v.	db.createUser( { user: "aacuser", pwd:  passwordPrompt(), roles: [ { role: "readWrite", db: "aac" } ] } )


Installation
Python – installed via local package manager or from python.org
MongoDB – install available at mongodb.com
Jupyter Notebook – install with ‘pip install notebook’
PyMongo driver – install with ‘pip install pymongo’
-	Selected because PyMongo is the official recommended Python driver for Mongo. It is fast, simple, and officially supported. 

Challenges and obstacles
-	I added the argument “selected_rows=[0]” to the data_table, and I noticed that was getting cleared after selecting a filter option. I resolved this by an output argument to the callback to update the table – setting the selected_rows to [0] on each update. 

-	 When first testing some edits to the data-table, I kept loading up the web-UI to an empty table. Debug statements were outputting correctly indicating no issue with database connection. I’m not exactly certain why this fixed it, but the issue was resolved after I added a ‘return {}’ to the update function instead of just having ‘return’.


-	I decided to add color and more style using inline CSS, which was challenging because I did not immediately grasp what style options can apply here and how to apply them. For example, I tried to color the background of the pie chart, but it wasn’t working and after some troubleshooting, I looked up the documentation on how to color the pie chart background properly, because I was only styling the graph object underneath. 

-	Another thing I realized is that some of the animals in the database have an outcome_type of “Euthanasia” for various reasons like aggression or sickness. It would be very unpleasant for users to use the filter and see animals of that outcome_type, so I removed those from the filter queries. 



Usage
Code Example:
<img width="496" height="233" alt="image" src="https://github.com/user-attachments/assets/9b5afd3b-a73c-480c-815b-f86f250e6177" />

 

Tests
Run tests against the pymongo CRUD methods by importing the module into a Jupyter Notebook, instantiating an instance of the CRUD class and calling those methods.
<img width="1240" height="615" alt="image" src="https://github.com/user-attachments/assets/7b4e6173-5a02-42de-981e-64d850cb5949" />


Beginning state of the APP
<img width="1161" height="720" alt="image" src="https://github.com/user-attachments/assets/749b60a2-b596-4589-bfe0-910a715d50f5" />






















