# Rule-Based Classification for Estimating Potential Customer Revenue

This project aims to segment customers using level-based classifications derived from sales data provided by **Gezinomi**, and to estimate the potential revenue that new customers might bring to the company. The project utilizes rule-based classification methods and data processing techniques.

## Project Purpose

Gezinomi aims to create level-based sales definitions using certain attributes of their sales, and segment these sales to estimate how much potential revenue new customers might generate. For example, the project estimates how much revenue a customer visiting an all-inclusive hotel in Antalya during a high-demand period could bring to the company.

## Dataset

The dataset used in this project contains details about sales made by the Gezinomi company. For each sale, information such as city, hotel concept, sales date, and price is provided. Key variables in the dataset include:

- **SaleId**: The ID of the sale
- **SaleCityName**: The city where the hotel is located
- **ConceptName**: The hotel's concept (e.g., All-Inclusive, Half-Board)
- **SaleDate**: The date when the sale was made
- **CheckInDate**: The date when the customer checks in to the hotel
- **Price**: The price of the sale
- **Season**: The season when the check-in occurs (High or Low Season)

## Project Tasks

1. **Data Exploration and Analysis**: A general exploration and analysis of the dataset was conducted. Grouping operations were performed on variables such as city, concept, and sales price to uncover insights.
   - Number of unique cities and concepts
   - Frequency of sales for each concept
   - Total and average revenue per city and concept

2. **Customer Segmentation Based on Booking Time**: The variable `SaleCheckInDayDiff`, which represents the difference in days between the check-in date and the booking date, was converted into categorical variables. This allowed for segmentation of customers based on their booking behavior:
   - **Last Minuters**: Customers who booked within 0-7 days of check-in
   - **Potential Planners**: Booked within 7-30 days
   - **Planners**: Booked within 30-90 days
   - **Early Bookers**: Booked more than 90 days in advance

3. **Revenue Estimation**: The project calculates average revenue based on city, concept, and booking behavior, then segments customers based on these categories.

4. **Creating Level-Based Customers (Personas)**: New level-based sales were defined and added as a variable `sales_level_based`. This was created by combining attributes such as city, hotel concept, and season.

5. **Segmenting Personas**: These new personas were segmented into 4 different segments (`A`, `B`, `C`, `D`) based on their potential revenue. This segmentation allowed us to describe each group by analyzing their mean, maximum, and total revenues.

6. **Predicting Revenue for New Customers**: The final task involved predicting how much revenue a new customer might bring to the company. For instance, we estimate the revenue for a customer visiting an all-inclusive hotel in Antalya during the high season.

## Code Implementation

The core of the project is implemented in the `main.py` file, which includes the following key steps:

- Reading and exploring the dataset
- Grouping and aggregating data based on cities, hotel concepts, and seasons
- Creating level-based sales personas
- Segmenting customers into different revenue groups
- Predicting the potential revenue for new customers

### Example Code Snippets

1. **Loading the Dataset and Initial Exploration**:
   ```python
   import pandas as pd
   df = pd.read_excel('miuul_gezinomi.xlsx')
   df.head()
   ```

2. **Grouping Data by City and Concept:**

```python
df.groupby(['SaleCityName', 'ConceptName'])['Price'].mean()
```

3. **Creating Categorical Segments for Booking Behavior:**

```python
bins = [-1, 7, 30, 90, df['SaleCheckInDayDiff'].max()]
labels = ['Last Minuters', 'Potential Planners', 'Planners', 'Early Bookers']
df['EB_Score'] = pd.cut(df['SaleCheckInDayDiff'], bins, labels=labels)
```

4. **Segmenting Customers:**

```python
df['SEGMENT'] = pd.qcut(df['Price'], 4, labels=['D', 'C', 'B', 'A'])
```

**Files in the Repository**
    - **main.py:** The main script that contains all the data processing, customer segmentation, and revenue estimation logic.
    - **miuul_gezinomi.xlsx:** The dataset used for the analysis (not included in the repository).
    - **segmentation.xlsx:** The output file where segmented data is saved.
    - **eb_scorew.xlsx:** The output file containing the booking behavior score (EB_Score).
## Conclusion
This project demonstrates how to segment customers using rule-based classifications and estimate the potential revenue for new customers based on historical sales data. By leveraging features such as booking behavior, city, and hotel concept, we can provide valuable insights into customer segments and their contributions to the business.