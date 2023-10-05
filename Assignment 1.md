Assignment: You are asked by the municipality of Amsterdam to advise on the feasibility of hosting a 5km open water swimming event through the canals of Amsterdam. View the event through the perspective of the safety of the partaking athletes and an environmental perspective. The event is going to be hosted in May. 

Think of a few data sets that are of use for giving proper advice to the municipality:
1.	What type of data format is the information you found stored in? Are they human readable? Are they text files or binary?
2.	Is the data stored numerical?
3.	Try to find a suitable Python library than can read that format. 
4.	If you have geospatial data, can you figure out how the data is geometrically represented (points, lines, surfaces, hyperplanes)?
5.	If it is temporal data, what is the interval? 

Requirements
•	The event can’t have an impact on commercial water transport.

In our definition of (commercial) water transport, we include commercial deliveries and cargo, as well as construction boats, points of loaden and unloading, and the ferries.

-	Ferry’s operate on the IJ, which excludes this from the swimming route. https://reisinfo.gvb.nl/nl/lijnen?boat&show 
	This geodata is not downloadable. The geospatial data is represented through points and lines. 

-	The same is true for commercial transport by boat. However, besides the IJ, commercial water transport passes through the Amstel and from the Amstel through the Westerdok. https://www.pdok.nl/atom-downloadservices/-/article/vaarweg-informatie-nederland-vin- 
	The geodata can be downloaded in gpkg format. It is geospatial data, where the data is represented geometrically through lines. 
	There are different libraries to read this data type, such as geopandas and Fiona. 

-	The municipality of Amsterdam has spatial data of the boarding and disembarking points of water transport vessels. Because of this information, canals which less points can be included in the route, to avoid disruption. https://maps.amsterdam.nl/varen/  
	This data can be downloaded in json and csv. There are human readable text files. The csv data is stored alphanumerical, with words and numbers. The geospatial data is represented through points. 
	The csv data is readable in Python. Python also has a built-in package called json, which can be imported.  



•	It would be appreciated if the event has small impact on the routes of the canal boats. 

To make sure the impact on canal boats is being minimalized, their location and routs need to be analyzed. 

-	The municipality of Amsterdam has spatial data on the boarding and disembarking points of passenger shipping. https://maps.amsterdam.nl/varen/ 
	This data can be downloaded in json and csv. There are human readable text files. The csv data is stored alphanumerical, with words and numbers. The geospatial data is represented through points. 
	The csv data is readable in Python. Python also has a built-in package called json, which can be imported.  

-	There is no (accessible) spatial data on the routes of the canal boats. The boarding and disembarking points can give some indication. Additionally, the Grachtenmonitor 2022 (p.10, p. 13) gives insight in the locations with the most boat passings a day. 
	This geospatial data is only accessible through this map. Only the image can be used and analyzed, not the actual data. 

•	What is the pollution level of the canals and is there data from all the canals? Are the canals monitored and can you swim there safely?  

The route of the Amsterdam city swim is being monitored by Waternet during the year (Amsterdam City Swim, n.d.). However, only the quality of official swimming locations is being published regularly. 

-	There is a national database available with water quality results of official swimming locations. This can provides insights in the water quality of official swimming locations in Amsterdam. These locations can possibly be included in the route. https://www.pdok.nl/introductie/-/article/zwemwater-provinciaal-en-rijkswateren-  
	The geodata can be downloaded in gpkg format. It is geospatial data, where the data is represented geometrically through points. 
	There are different libraries to read this data such as pygml and geopython. 
	This is temporal data, with an interval of 14 days during the swimming season. 

-	The municipality of Amsterdam provides spatial data on the location of the official swimming location. https://maps.amsterdam.nl/zwemwater/ 
	This data can be downloaded in json and csv. There are human readable text files. The csv data is stored alphanumerical, with words and numbers. The geospatial data is represented through points. 
	The csv data is readable in Python. Python also has a built-in package called json, which can be imported.  

-	There is more specific data available of the water quality of some locations. This dates from 2019. https://onderzoek.amsterdam.nl/dataset/water-in-amsterdam 
	This alphanumerical data set is stored in an excel file. This is no geospatial nor temporal data. 
	The most used packages for working with excel files in Python is openpyxl. 

-	Since overall data on the water quality of the canals is not (publicly) available, looking at the sewage system might be helpful. Mixed sewers can overflow in times of heavy rainfall, leading to unsafe swimming water. The location of mixed sewage systems is shown on this map: https://data.amsterdam.nl/data/   
	This geospatial data is not downloadable through this website. This geospatial data is represented through lines. 

-	According to Waternet, they are monitoring the water quality of the canals using sensors. Maybe this data can be made available (Waternet, 2019). 

-	The Grachtenmonitor 2022 (p. 16) does show that the canals are getting cleaner. In 2022, the overall score was 8.2. 
