# ETL_Using_Python
ETL Pipeline Implementation and API Data Handling

•	In the initial stages of the project, fetching data from the API endpoint was straightforward when the dataset was relatively small. However, as the data size increased, the API response time became significantly longer, leading to failures in data retrieval.

•	To mitigate this issue, Python code was leveraged to handle API requests efficiently and streamline the ETL process. Due to advancements in AI security, Dell implemented stricter controls through the High-Value Asset (HVA) model, transitioning all API sources to an Online Subscription API Gateway. This shift was aimed at preventing unauthorized access by third parties or internal users.

# Authentication and Data Retrieval- 

•Create a subscription group and get access to that group with which we can get client ID and Client secret Key.

•	With the subscription-based model in place, authentication required obtaining a Client ID and Client Secret Key, which were then converted into a 64-bit encoded format. 

•Python code was used to authenticate the API access, which posed some initial complexities. 

•The authentication process involved generating an access token, which was tested using postman using get method. enabling secure API interactions and ensuring successful data retrieval.

•	Once authenticated, the extracted data—formatted in JSON—needed to be stored efficiently in an SQL database.

# Data Transformation and Error Handling -

•	To accommodate the nested JSON structure within an SQL database, a dedicated table was created to store the data. 

• However, direct insertion posed challenges due to the hierarchical nature of JSON objects, leading to incomplete data population across table columns.

•	To overcome this, Python scripts were used to parse and transform the nested JSON, converting selected columns into the required data formats for seamless integration.

•Additional transformations ensured structured storage(implicitly define data type of each extracted JSON column), while error-handling mechanisms were incorporated to manage inconsistencies and API failures.

•	By implementing these strategies, the ETL pipeline successfully handled API authentication, data retrieval, transformation, and structured storage in SQL, ensuring efficiency and compliance with enhanced security measures.
