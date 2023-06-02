# ClickHouse Data Ingestion	


These scripts allow you to create and ingest data into ClickHouse using the provided Python script.
The first script is related to generating random data types and saving data as CSV files. It performs the following steps:
-	Imports the required libraries and modules.
-	Defines a string variable my_string that represents the data types and field names. If you have multiple tables, you need to define the field names and data types for each of them.
-	Parses the my_string variable to extract the field names and data types.
-	Sets the number of rows (N) and the start date.
-	Generates random data for each field based on its data type and stores it in a Pandas DataFrame.
-	Saves the DataFrame as a CSV file with a unique filename. The script will generate random data based on the provided configuration and save it as CSV files. Each CSV file will have a unique name based on the number of rows (N) and an iteration counter (itt).

Prerequisites :
-	Python 3.x
-	Required Python libraries: datetime, random, pandas, numpy, requests

Thanks to the second script we can ingest the data into ClickHouse. It performs the following steps:

-	Log in to the ClickHouse server using the provided account credentials.
-	Obtain an authentication token for subsequent API requests.
-	Initialize the ClickHouse module using a JSON configuration file.
-	Iterate over a range of dates and perform the following actions for each date:
-	Start a new transaction for the specified table and date.
-	Ingest CSV files into a zip table.
-	Ingest a CSV file into the main table using the generated transaction ID.
-	Close the transaction for the specified table and date.
-	Complete the ingestion process.



Before running the script, make sure to update the following variables in the script:
-	URL: Specify the URL of the ClickHouse server.
-	account: Provide the account username.
-	passwd: Provide the account password.
-	tableName: Specify the name of the main table.
-	ziptableName: Specify the name of the zip table.
-	comment: Add your comment. For example, in our case I defined it as "ingestion". 
-	branch: Specify the branch name.
-	LiquidityGAP14.json: Provide the name of the JSON configuration file.
-	13GapTimeBucket10_${j}.csv: Provide the names of the CSV files to ingest into the zip table.
-	13LiquidityGAP10_${j}.csv: Provide the names of the CSV files to ingest into the main table.


We have 2 loops: 
-	The first loop iterates over the values of i from 11 to 15, inclusively. This means that we are ingesting data for the days of the month from the 11th to the 15th. You can modify them according to the requirements.
-	The second loop iterates over the values of j from 0 to 2. This means that we retrieve files named 'LiquidityGap' with numbers ranging from 0 to 2 at the end of their names.
And finally, we close the transaction to view the data in the UI as well.

We can also ingest data from Insomnia. However, the advantages of this method are that we can create the module, generate and ingest large amounts of data in a single step by simply clicking the 'run' button in a Python file.

