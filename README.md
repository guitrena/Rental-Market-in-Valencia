# Rental Market in Valencia, Spain
***

## 0. Introduction
***
> This project presents an **analysis of the rental market in Valencia** to acknowledge what are the most important characteristics of the houses offered to take advantage on the strategies used to rent a house or invest in real estate. It might also help people on the looking for a new house in Valencia to better understand the idiosyncrasy of one of the most trendy cities in Spain.
>
> But that is not the only thing, a **model trained to estimate the renting price** was trained and it will give you a first estimation based on the overall environment of the real estate in Valencia. At the same time, if you want to invest in a new property to rent afterwards you can take profit of this model by comparing the price of the buy with the rental price estimation.
>
>
>> Before getting into detail, you have to understand that the data concerning this topic is very valuable and that is why the most important renting websites keep it very secured. Therefore, **the data used in this project is not as complete as we would like.** For example, not every district of Valencia has enough information to be reliable. That is why the model trained only takes into account the districts marked in green in the next map. The other zones will be aggregated in the same category and, therefore, they would not be as precise as expected. 
>> ![alt text](./Images/map_data_available.png)

> ![alt text](./Images/price_distribution.png) 

> ### Economic insights 
> ***

## 1. Data 
***


### 1.1.  Webscrapping

> As commented before, the data concerning this topic is very difficult to retrieve. The most important renting companies invest a lot of money in preventing others to obtain this information from their website. After trying to avoid the security levels of the top companies with no succes, we were able to webscrap a second tier website with less quantity of observations.
>
> The tools used to obtain this data where: 
>> **Selenium: to open and scroll the pages to avoid lazy loading and take the html file**
>>
>> **Beatiful Soup: to retrieve the information required**
>
> #### The webscraping codes and the datasets obtained are hidden for legal reasons
 

### 1.2. Data restructuring

> This part is just to present the _**Data_restructuring.ipynb**_ file. This file is specifically designed to help the interested parts the information retrieved from the website without sharing the webscraping codes and the datasets obtained. 

### 1.3 Nan values filling

> Commonly, when working with data not always every feature has all its values completed and this is no exception. Different strategies where used in this case to fill the missing values and they are presented in the **_Data_exploration.ipynb_** file. But, some of them are interesting enough to comment them. 
>
> At first sight, features like number of rooms and surface seem very important. That is why a simple imputer in this case does not work very well. More creative ways are needed that is why some ratios were calculated to estimate these missing values.
>> We focus on the filling of the surface as an example to better understand this concept. Using the observations where the data was complete, a **ratio between the surface and the different spaces** of the house was calculated. **These different spaces were weighted** to simulate the proportions of each one of them compared to a room. The following ecuation defines this constant.
>>
>> $$Ratio = \frac{1}{n} \times \sum_{k=1}^n  \frac{Surface_k [m^2]}{1 \times Rooms_k + 0,5 \times Bathrooms_k + 0,75 \times Terrace_k + 0,25 \times Balcony_k} $$ 
>>
>> After obtaining this ratio, for the offers that had the number of spaces complete but no surface, we were able to estimate it by multiplying their weighted values by this ratio.
>>
>> $$Surface Estimation_k = Ratio \times (Rooms_k + 0,5 \times Bathrooms_k + 0,75 \times Terrace_k + 0,25 \times Balcony_k)$$

### 1.4. Final features + number of observations
> **Number of observations: 711**
>
> **Features**
>
>    - **House_type:** Type of the house written in the offer. 
>    - **Location:** District of the city where the house is located. 
>    - **Furnished:** Whether the house is furnished or not. 
>    - **Elevator:** Whether the house has an elevator or not. 
>    - **Terrace:** Whether the house has a terrace or not. 
>    - **Balcony:** Whether the house has a balcony or not. 
>    - **Storage:** Whether the house has a storage or not. 
>    - **Rooms:** Nº of rooms. 
>    - **Bathrooms:** Nº of bathrooms. 
>    - **Surface:** Square meters of the house. 
>    - ***Agent_cat:** Type of real estate agent managing the offer (Variable added during model optimization). It can also be interpreted as Premium/No premium House.*
>    - **Price:** Target variable

## 2. Analysis
***
>
> A complete analysis of the different characteristics is elaborated in the **_Data_exploration.ipynb_** file while in this section the most relevant insights are presented.

### 2.1. Price per square meter by Location

> One of the most common metrics to better understand the real estate is the price per square meter. This variable was calculated and we present downstream the highest and lowest values by district in the next graph. This might seem very simplistic but it is very important to acknowledge the idiosyncrasy of the city. 
> ![alt text](./Images/highest_lowest_prices.png) <br><br><br>
> 
> It is even more significant to have a map of the city where you can find the price per square meter of each location. As we can see in this map there is a clear pattern, **the districts situated in the center of the city are more expensive** than the rest and the further you get the lower the price per square meter. Also, we can point that there are **some districts near to the center that might be market opportunities** due to its low price.
> ![alt text](./Images/map_price.png)



### 2.2. Price per square meter by nº of rooms

> Normally, you would think that the higher the number of rooms the more expensive the house but if we take into account the price per square meter this is not the case. As we can see in the graph below where the distributions of this variable by number of rooms are presented as boxplots, the lower the number of rooms the more expensive the square meter is. Trying to understand this behaviour two hypothesis were raised to perform a deeper analysis.
>> **<ins>Hypothesis 1:</ins> Houses with just one room are very small** that is why they have a higher €/m²** because there is also a minimum threshold for the price. <br>
>> **<ins>Hypothesis 2:</ins> Houses with more surface have more rooms but these ones are located in lower €/m² zones.** 
>
> ![alt text](./Images/price_distribution_rooms.png)

#### 2.2.1. Size by rooms

> To check the first hypothesis, the average surface for each number of rooms and the difference between consecutive categories are ploted. As we can see, **the average surface for houses with just one room is 50 m$^2$** and the maximum increase is between houses with 1 and 2 rooms with 33 m$^2$. This is an **increase in surface of 66%** and, for instance, the second highest increase is just of 28% (from 2 to 3 rooms). In relative terms we can then assume that houses with just one room are very small.
>
> ![alt text](./Images/average_surface_rooms.png)

#### 2.2.2. Nº of rooms by location

>To check the second hypothesis, the locations have been categorized by range of price per square meter using the following categories: ['<16 €/m²', '16-19 €/m²', '19-22 €/m²', '>22 €/m²']. Then, the average number of rooms for these categories have been calculated showing that **the higher the price per square meter the less number of rooms**. Parallelly, the same aggregation has been done to plot the map per districts to check the location of this categories. **The highest prices per square meter (where the number of rooms is lower) are located in the center of the city** where it seems logical that the houses are smaller.


'                          | '                         
:-------------------------:|:--------------------------: 
![alt text](./Images/map_price_range.png) | <img src="./Images/average_n_rooms.png" width="500" height="500" />



## 3. Modelling
***

> In this part, the process to train a model to estimate the price of a house according to its characteristics is explained. **The objective** marked at the beginning of the modelling **is to reach a lower RMSE than 300** which seems reasonable due to the low quantity of data. For a more detailed description check the ***Modelling.ipynb*** file.
### 3.1. First results 

>To start with the modelling and after doing all the preprocessing required several differente regression model were trained to check which ones were the most promising performance wise. Many metrics were calculated but the one chosen to compare the results was the Root Mean Square Error because it has the same dimension as the target (Price). 
>
>> **Results** (Most notable models): <br><br> - LinearRegression: _Decent performance in test (RMSE=499) despite its simplicity_ <br><br> - RandomForestRegresor: _Noteworthy performance in test (RMSE=460 // Best) and massive difference with training (RMSE=235) due to overfitting what might make it optimizable using specific hyperparameters_ <br><br> - GradientBoostingRegressor: _Best perfomance in test **(RMSE=460)**_
>
> ![alt text](./Images/First_models_results.png)


### 3.2. Optimization

> After obtaining the first results, an optimization process was carried out to reach the objective (RMSE<300). 
#### 3.2.1. Dropping extreme values

>> To understand the behaviour of the models, the difference between the preditions of the Random Forest model and the real values of the test set was calculated and then ploted in an histogram. As we can see, the highest differences were for highly underestimated observations.
>> ![alt text](./Images/histogram_extreme_values.png)
>
>> At the same time, a scatter plot was done to compare the predictions and the real values. In the graph below, we can see also three lines that mark the perfect estimation and the range of +/- 300 (RMSE objective). It is noticeable that the **extreme values (over 2925 euros) are always very underestimated** and represent a major part of those underestimations pointed in the histogram.
>>
>>
>> ![alt text](./Images/predvsreal_extreme_values.png)
>> **The approach was to drop many of these extreme values** to reduce the artificial error and to avoid overestimations in other observations. Not every extreme value was dropped to avoid, on one hand, dropping too many offers, and on another one, underestimations in offers around the threshold.
>>
>> This optimization step had as result a **reduction in the RMSE from 460 to 358 in the Gradient Boosting model.**
>> 


#### 3.2.2. Enriching the dataset with new feature

> When analysing the most underestimated offers in the website where the data was scrapped, an idea for a new feature came up. Many of these offers had the same real state agent: Engel & Volkers and, at the same time, the houses seemed very comfortable and aesthetic. This info was not retrieved in the first webscraping so a **new webscrapping was performed to get the agent name of the offer.**
>
> To check how the agent affected to the value of the offer, an histogram was plotted to check the distribution of agent in the price per square meter variable. As we can see, a gap defining two groups was found (around 23 €/m²) which helped to define a **new binary feature 'Agent_cat' that can be interpreted also as Premium/No premium house.**
>
> ![alt text](./Images/histogram_agents.png)
>
>When training the models an improvement in performance was achieved reaching, for example, **a test RMSE in Gradient Boosting of 305.**

#### 3.2.3. Searching best hyperparameters

> After point 3.2.2, the Random Forest had a RMSE in training of 148 and in test of 317. It was appealing to try to select the best hyperparameters to reduce overfitting and improve the performance. **The result was not good enough (RMSE=306) to select this model over the Gradient Boost one.**
> ![alt text](./Images/Final_models_results.png) <br> <br>
> **The model that will be used is the Gradient Boost regressor with a RMSE in test of 305.**



## 4. Next steps
>
> **Some tasks have remained undone** due to their high cost but it is necessary to mark them to understand that this project is just a start point and can have other beneficial endings. Some of these tasks are:
><br>
>> **- Obtain more data** and enrich this data with more features. <br>
>> **- Perform a similar analysis of the buying market to compare the results and underline the market opportunities.**<br>
>> **- Periodically retrieve the data and analyse it to obtain the dynamic behaviour of the market** 

![prediction example](./Images/prediction_example.gif)