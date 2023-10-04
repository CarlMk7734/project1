# EDA and Prediction
Churn is a one of the biggest problem in the telecom industry. Research has shown that the average monthly churn rate among the top 4 wireless carriers in the US is 1.9% - 2%.

First we read the data file in the python notebook

Then we explore the data to see if there are any missing values.

After looking at the output, we can say that there are 11 missing values for Total Charges. Let us replace remove these 11 rows from our data set

Month to month contracts, absence of online security and tech support seem to be positively correlated with churn. While, tenure, two year contracts seem to be negatively correlated with churn.

Interestingly, services such as Online security, streaming TV, online backup, tech support, etc. without internet connection seem to be negatively related to churn.

We will explore the patterns for the above correlations below before we delve into modelling and identifying the important variables.

## Data Exploration 
Let us first start with exploring our data set, to better understand the patterns in the data and potentially form some hypothesis. First we will look at the distribution of individual variables and then slice and dice our data for any interesting trends.
### Demographics
Let us first understand the gender, age range, patner and dependent status of the customers
#### a)Gender Distribution
About half of the customers in our data set are male while the other half are female


#### b) % Senior Citizens -
There are only 16.2% of the customers who are senior citizens. Thus most of our customers in the data are younger people.

#### c) Partner and dependent status 
48% of the customers have a partner,while only 30% of the total customers have dependents.

### What would be interesting is to look at the % of customers, who have partners, also have dependents. We will explore this next.
Interestingly, among the customers who have a partner, only about half of them also have a dependent, while other half do not have any independents. Additionally, as expected, among the customers who do not have any partner, a majority (80%) of them do not have any dependents .

I also looked at any differences between the % of customers with/without dependents and partners by gender. There is no difference in their distribution by gender. Additionally, there is no difference in senior citizen status by gender.

**B.) Customer Account Information**
Let us now look at the tenure, contract


**1. Tenure**
After looking at the below histogram we can see that a lot of customers have been with the telecom company for just a month, while quite a many are there for about 72 months. This could be potentially because different customers have different contracts. Thus based on the contract they are into it could be more/less easier for the customers to stay/leave the telecom company.
**2. Contracts** 
To understand the above graph, lets first look at the number of customers by different contracts.
As we can see from this graph most of the customers are in the month to month contract. While there are equal number of customers in the 1 year and 2 year contracts.

Below we will understand the tenure of customers based on their contract type.
Interestingly most of the monthly contracts last for 1-2 months, while the 2 year contracts tend to last for about 70 months. This shows that the customers taking a longer contract are more loyal to the company and tend to stay with it for a longer period of time.

This is also what we saw in the earlier chart on correlation with the churn rate.

**C. Let us now look at the distribution of various services used by customers**

**D.) Now let's take a quick look at the relation between monthly and total charges**

**E.) Finally, let's take a look at out predictor variable (Churn) and understand its interaction with other important variables as was found out in the correlation plot.**

Lets first look at the churn rate in our data

In our data, 74% of the customers do not churn. Clearly the data is skewed as we would expect a large majority of the customers to not churn. This is important to keep in mind for our modelling as skeweness could lead to a lot of false negatives. We will see in the modelling section on how to avoid skewness in the data.

Lets now explore the churn rate by tenure, seniority, contract type, monthly charges and total charges to see how it varies by these variables.
i.) Churn vs Tenure: As we can see form the below plot, the customers who do not churn, they tend to stay for a longer tenure with the telecom company.

**ii.) Churn by Contract Type:** 
Similar to what we saw in the correlation plot, the customers who have a month to month contract have a very high churn rate.

**iii.) Churn by Seniority:** 
Senior Citizens have almost double the churn rate than younger population.
**iv.) Churn by Monthly Charges:** 
Higher % of customers churn when the monthly charges are high.
**v.) Churn by Total Charges:** 
It seems that there is higer churn when the total charges are lower.
After going through the above EDA we will develop some predictive models and compare them.
We will develop Logistic Regression, Random Forest, SVM, ADA Boost and XG Boost

1. Logistic Regression
It is important to scale the variables in logistic regression so that all of them are within a range of 0 to 1. This helped me improve the accuracy from 79.7% to 80.7%. Further, you will notice below that the importance of variables is also aligned with what we are seeing in Random Forest algorithm and the EDA we conducted above.

We will observe that the total charges increases as the monthly bill for a customer increases.

**Observations**

We can see that some variables have a negative relation to our predicted variable (Churn), while some have positive relation. Negative relation means that likeliness of churn decreases with that variable. Let us summarize some of the interesting features below:

As we saw in our EDA, having a 2 month contract reduces chances of churn. 2 month contract along with tenure have the most negative relation with Churn as predicted by logistic regressions
Having DSL internet service also reduces the proability of Churn
Lastly, total charges, monthly contracts, fibre optic internet services and seniority can lead to higher churn rates. This is interesting because although fibre optic services are faster, customers are likely to churn because of it. We need to explore more to better understad why this is happening.
Any hypothesis on the above would be really helpful!

**2. Random Forest**
**Observations:**

From random forest algorithm, monthly contract, tenure and total charges are the most important predictor variables to predict churn.
The results from random forest are very similar to that of the logistic regression and in line to what we had expected from our EDA

**3. Support Vecor Machine (SVM)**
Wth SVM the accuracy was able to be increased upto 82%. However, we need to take a deeper look at the true positive and true negative rates, including the Area Under the Curve (AUC) for a better prediction. I will explore this soon. 
Interestingly with XG Boost,  the accuracy on test data was increased to almost 83%. Clearly, XG Boost is a winner among all other techniques. XG Boost is a slow learning model and is based on the concept of Boosting
