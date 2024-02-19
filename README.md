# GURGAON-HOUSE-PRICE-PREDICTION
GURGAON HOUSE PRICE PREDICTION MODEL BASED ON 99ACRES.COM DATA.

GURGAON HOUSE PRICE PREDICTION

PROJECT FLOW :
    1. Web Scraping from "99Acres.com" for aprtments in Gurgaon.
    2. Data Cleaning and Feature Engineering.
    3. Perform in depth Exploratory Data Analysis.
    4. Outlier detection and missing value Imputtion.
    5. Feature Selection 
    6. Model selection and Productionalization.
    7. Devoloping the analytics module.
    8. Devoloping the Recommender System.
    9. Deploying the application on AWS.


### Web Scraping Real Estate Data from 99acres.com

This Python script is designed to scrape property data from the real estate website "99acres.com" for apartments in a specific city. It navigates through multiple pages, extracts details of each property, and saves the data to a CSV file. The script is robust, handling potential errors gracefully, and manages request pacing to avoid IP bans.

#### Features:

- **Initialization of Variables**: Defines variables such as start and end page numbers, and the path to the CSV file.
  
- **Page Navigation**: Iterates through each page within the specified range, making HTTP requests to retrieve property listings.

- **Property Extraction**: Navigates through individual property sections on each page, extracting details such as property name, link, society name, price, area, bedroom count, etc.

- **Request Management**: Introduces pauses between requests to prevent rapid-fire requests that could lead to IP bans.

- **Creating and Saving Data**: Stores extracted details in a DataFrame and appends it to the main DataFrame, saving it to a CSV file. Existing files are appended without rewriting headers.

#### Usage:

1. **Initialization**: Set the start and end page numbers, and define the folder structure for saving data.

2. **Scraping**: Execute the script, which navigates through pages, extracts data, and saves it to CSV.

3. **Combining CSV Files (Optional)**: Utilize the provided function `combine_csv_files` to combine multiple CSV files into one for easier analysis.

#### Handling Errors:

- The script gracefully handles errors such as missing attributes or potential IP blocks, providing instructions for resolution.



### Data Cleaning and Feature Engineering Pipeline

#### 1. Extracting Property Area Information
- Extracted Super Built up area, Built Up area, and Carpet area from the 'areaWithType' column.
- Converted area values to square feet if provided in square meters.
- For properties labeled as 'Plot', extracted plot area.

#### 2. Handling Additional Rooms
- Created new columns for study room, servant room, store room, pooja room, and others based on the 'additionalRoom' column.

#### 3. Categorizing Age of Possession
- Categorized properties based on age into New Property, Relatively New, Moderately Old, Old Property, or Under Construction.

#### 4. Extracting Furnishing Details
- Extracted unique furnishings from the 'furnishDetails' column.
- Created new columns for each unique furnishing and populated with counts.
- Clustered properties into unfurnished, semi-furnished, or furnished based on furnishing types.

#### 5. Handling Property Features
- Merged property features from an external dataset based on the society name.
- Converted features into a binary matrix using MultiLabelBinarizer.
- Conducted KMeans clustering on the binary matrix to cluster properties into feature groups.

#### 6. Final Cleanup and Saving
- Dropped unnecessary columns such as nearbyLocations, furnishDetails, features, and additionalRoom.
- Saved the cleaned dataset to 'gurgaon_properties_cleaned_v2.csv'.

This pipeline enhances the dataset for analysis and modeling, providing valuable insights into property characteristics and amenities, including feature clusters derived from KMeans clustering.


### Exploratory Data Analysis
    Here's a summary of the analysis and visualizations conducted on the Gurgaon properties dataset, along with key observations:

1. **Property Type Distribution:**
   - Flats constitute the majority (approximately 75%) of the properties, while houses make up the remaining 25%.
   - No missing values in the property type column.

2. **Society Analysis:**
   - There are a total of 675 societies in the dataset.
   - The top 75 societies encompass 50% of the properties, while the remaining 600 societies contain the other 50%.
   - Around 13% of properties are labeled as 'independent'.
   - One missing value in the society column.

3. **Sector Analysis:**
   - There are 104 unique sectors in the dataset.
   - Three sectors have more than 100 listings, while 25 sectors have between 50 to 100 listings.
   - No sectors have only one listing.

4. **Price Distribution:**
   - The price distribution is right-skewed, with a positive skewness of approximately 3.28.
   - The majority of properties are priced below 5 crores, with a few outliers exceeding 10 crores.
   - 17 missing values in the price column.

5. **Price per Sqft Distribution:**
   - Right-skewed distribution with potential outliers.
   - 17 missing values in the price_per_sqft column.

6. **Bedroom and Bathroom Distribution:**
   - Most properties have 2 or 3 bedrooms and bathrooms.
   - No missing values in the bedroom and bathroom columns.

7. **Balcony Distribution:**
   - Majority of properties have 1 or 2 balconies.
   - No missing values in the balcony column.

8. **Floor Number Analysis:**
   - Most properties are located between the ground floor and the 25th floor.
   - Potential outliers exist on the higher side of the floor number distribution.
   - No missing values in the floorNum column.

9. **Facing Analysis:**
   - 'NA' was filled in for missing values.
   - Majority of properties face 'North' or 'East'.

10. **Age of Possession Analysis:**
    - Majority of properties fall under the 'New Property' or 'Under Construction' categories.
    - No missing values in the agePossession column.

11. **Area Analysis (Super Built-up, Built-up, Carpet):**
    - Right-skewed distributions with potential outliers.
    - Missing values in super_built_up_area and carpet_area columns.

12. **Additional Rooms Distribution:**
    - Study rooms are the most common additional rooms, followed by servant rooms and store rooms.
    - No missing values in additional room columns.

13. **Furnishing Type Distribution:**
    - Majority of properties are semi-furnished.
    - No missing values in the furnishing_type column.

14. **Luxury Score Distribution:**
    - Multi-modal distribution with peaks around 0-50 and 110-130.
    - No missing values in the luxury_score column.

This summary provides an overview of the dataset's characteristics and highlights areas of interest for further analysis.


### Outlier Treatment

1. **Outlier Removal:**
   - Identified and removed outliers in the 'price' column using the Interquartile Range (IQR) method.
   - Addressed potential outliers in the 'price_per_sqft' column by adjusting the area values for properties with unusually high prices per square foot.

2. **Data Cleaning:**
   - Corrected area values for properties with exceptionally large or unrealistic values.
   - Adjusted bedroom and bathroom counts for properties with excessive values.
   - Handled anomalies in the 'super_built_up_area', 'built_up_area', and 'carpet_area' columns.

3. **Luxury Score Adjustment:**
   - Ensured consistency in luxury score representation.
   
4. **Derived Features:**
   - Calculated and updated the 'price_per_sqft' column based on corrected area and price values.

These preprocessing steps ensure data integrity and improve the quality of the dataset for further analysis and modeling.


### MODEL SELECTION 
Here's a summary of the model development process for predicting property prices using the Gurgaon properties dataset:

1. **Data Preprocessing:**
   - The dataset was preprocessed to handle outliers, categorical variables, and missing values.
   - Various encoding techniques such as Ordinal Encoding, OneHotEncoding, and Target Encoding were applied to categorical features.
   - Feature scaling and transformation were performed to normalize numerical features.

2. **Model Selection and Evaluation:**
   - Several regression models including Linear Regression, Support Vector Regressor, Decision Tree, Random Forest, Extra Trees, Gradient Boosting, AdaBoost, MLP, and XGBoost were evaluated.
   - Models were assessed using K-fold cross-validation and evaluated based on their mean absolute error (MAE) and R-squared (R2) score.

3. **Model Performance Comparison:**
   - Models were compared based on their MAE and R2 scores to select the best-performing model.
   - RandomForestRegressor with OneHotEncoding and hyperparameter tuning achieved the lowest MAE and highest R2 score.

4. **Hyperparameter Tuning:**
   - GridSearchCV was employed to tune hyperparameters for the RandomForestRegressor model.
   - Parameters like the number of estimators, maximum depth, maximum samples, and maximum features were optimized.

5. **Exporting the Model:**
   - The final model, along with the preprocessor, was exported using pickle for future use.

6. **Prediction Demonstration:**
   - The saved model was loaded to demonstrate predictions on new data, showcasing its usability in real-world scenarios.

This model development process provides insights into predicting property prices accurately and efficiently, contributing to decision-making in the real estate domain.

### ANALYTICS APP
Here's a summary of the Streamlit web application developed for visualizing analytics on property data:

1. **Location of Sectors:**
   - A scatter map displaying the geographical distribution of sectors based on their average built-up area and price per square foot. Larger and more expensive sectors are represented by larger and warmer-colored markers, respectively.

2. **Features Wordcloud:**
   - A word cloud representation of the most common features extracted from the dataset, providing insights into prevalent attributes associated with properties.

3. **Variation of Price with Property Type and Age of Property:**
   - Scatter plots depicting the relationship between built-up area and price for different property types (houses/flats) categorized by the age of the property.

4. **BHK Pie Chart based on Sectors:**
   - Interactive pie charts illustrating the distribution of the number of bedrooms (BHK) across sectors, enabling users to explore bedroom counts within specific sectors or the overall dataset.

5. **Price vs. BHK Comparison:**
   - Side-by-side box plots comparing the price distribution based on the number of bedrooms (BHK), offering insights into how prices vary with different bedroom configurations.

6. **Property Price Distribution:**
   - Kernel density estimation plots showing the distribution of property prices for houses and flats separately, allowing users to visualize the spread and central tendency of prices within each property type.

This Streamlit application provides an interactive and insightful platform for exploring various aspects of property data, aiding users in understanding geographical distributions, feature importance, price variations, and property type trends.


### RECOMMENDER APP

### Apartment Recommender System Summary

This repository contains a comprehensive apartment recommender system built using Python and various machine learning techniques. The recommender system is designed to assist users in finding suitable apartments based on their preferences and requirements. Here's a brief overview of the key components and functionalities of the recommender system:

#### Data Preparation and Feature Engineering
- The dataset used for the recommender system includes information about various apartments, such as property name, location advantages, price details, top facilities, etc.
- Data preprocessing techniques, such as parsing JSON strings and extracting relevant features, were applied to prepare the dataset for modeling.

#### Content-Based Filtering
- Content-based filtering techniques were employed to recommend apartments based on their textual features, such as nearby locations, location advantages, price details, and top facilities.
- The `TfidfVectorizer` from scikit-learn was used to transform textual features into numerical vectors, and cosine similarity was calculated to measure the similarity between apartments.

#### Location-Based Filtering
- Location-based filtering was implemented to recommend apartments based on their proximity to a selected location.
- Distance metrics were calculated between each apartment and various nearby locations to quantify their proximity.

#### Integration of Multiple Recommendation Models
- To enhance recommendation accuracy and diversity, three different recommendation models were integrated:
  - Content-based filtering using textual features (cosine_sim1)
  - Content-based filtering using price and area details (cosine_sim2)
  - Location-based filtering using distance metrics (cosine_sim3)
- The final recommendation scores were obtained by combining the outputs of these models with weighted coefficients.

#### Streamlit Web Application
- The recommender system was deployed as a user-friendly web application using Streamlit.
- Users can interact with the application to search for nearby apartments, explore detailed information about specific properties, and receive personalized recommendations based on their preferences.
- The application provides clickable links to external property listings for further exploration.

***DEPLOYMENT***

The web application was deployed via aws ec2.
