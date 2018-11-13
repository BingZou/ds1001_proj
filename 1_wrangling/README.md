## Data Wrangling

Data wrangling is broken into two major components, the first is constructing the universe and the second is feature extraction. Both will be documented below.


## Universe Construction

**Step 1**: narrowing down the yelp dataset to just businesses in the Greater Toronto Area
- Filtering by city name to cities in GTA such as (toronto, north york, etobicoke, etc...)
- Filtering by long/lat to the square area where the 1-99th percentile of long and lats fall respectively
- Filtering by business tags that represent restaurants: (restaurant, bars, bakeries)

After step 1, we have a total of 10914 restaurants, this is stored in **tor_rest.p** available on google drive


**Step 2**: narrowing down the yelp review universe to the reviews that correspond to the restaurant universe
- iterate through the review universe and only keep those with business_id in the above dataset

After step 2, we have 422,790 reviews, stored in **tor_reviews.p** available on google drive

**Step 3**: narrowing down the user universe to the users that correpond to the above review universe
- iterate through the users and only keep those who have written a review that appeared in the above dataset

After step 3, we have 93,075 users, stored in **tor_users.p** available on google drive

**Step 4**: joining to dinesafe universe
- using the address and the business name in the restaurant universe, we use fuzzy string matching to join to the public dataset on restaurant health scores from Dinesafe. The approximate match rate was 50%

After step 4, 5040 of the restuaruants in our universe was mapped to the health dataset. The mapping file is stored in **mapped_dinesafe.p** available on google drive 


## Feature Extraction

The work is split into notebooks:
- Feat_Business: extracts the business features **(Joe/Josh)**
- Feat_User: extracts the user features **(Joe/Josh)**
- Feat_Review_Num: extracts the numerical features of reviews **(Yunan)**
- Feat_Review_Text: extracts the text features of reviews **(Rong)**
- Feat_Dinesafe: extracts the features from the dinesafe dataset (on restaurant level) **(Rong)**

Each of these feature extractors will save a extracted feature df to the features/ directory