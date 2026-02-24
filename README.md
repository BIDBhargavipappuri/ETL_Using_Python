# ETL_Using_Python
ETL Pipeline Implementation and API Data Handling

•	In the initial stages of the project, fetching data from the API endpoint was straightforward when the dataset was relatively small. However, as the data size increased, the API response time became significantly longer, leading to failures in data retrieval.

•	To mitigate this issue, Python code was leveraged to handle API requests efficiently and streamline the ETL process. Due to advancements in AI security, Dell implemented stricter controls through the High-Value Asset (HVA) model, transitioning all API sources to an Online Subscription API Gateway. This shift was aimed at preventing unauthorized access by third parties or internal users.

# 	Authentication and Data Retrieval- 

•Create a subscription group and get access to that group with which we can get client ID and Client secret Key.

•	With the subscription-based model in place, authentication required obtaining a Client ID and Client Secret Key, which were then converted into a 64-bit encoded format. 

•Python code was used to authenticate the API access, which posed some initial complexities. 

•The authentication process involved generating an access token, which was tested using postman using get method. enabling secure API interactions and ensuring successful data retrieval.

