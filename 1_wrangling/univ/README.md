## Feature Extraction Results

This folder includes all of the results of pre-processing the universe, this document contains information on how these results are arrived.

## rest_univ_filter.p:
This is the universe of 10914 restaurants in Toronto.
- Filtered yelp dataset by region and long-lat that matches GTA cities: Toronto, Mississagua, North York, Yorkdale, Etobicoke, Scarborough and any misspelt names by fuzzy string match. long-lat was restricted to be between the 1st and 99th percentile of the initial list to get rid of mislabeled restaurants from outside city bounds
- Filtered dataset by business tag: using common restaurant related tags: 'restaurant', 'bar', 'bakeries'. Businesses without these tags were excluded since they're not restaurants

Columns in this table:
['address', 'attributes', 'categories', 'city', 'hours', 'is_open', 'latitude', 'longitude', 'name', 'neighborhood', 'postal_code', 'review_count', 'stars', 'state', 'postal_prefix']

## tor_reviews.p:
subset of raw reviews for restaurants in our universe, collected by iterating through all 6mm reviews and pulling out the 0.4mm reviews that are relevant to our restaurants.

The files is on **Google Drive**

## tor_users.p:
subset of users in a dataframe with users who have only reviewed a restaurant in toronto

The file is on **Google Drive**

## bus_review_extracts.p:
This contains all of the extracted word vector and review counts / avg stars of each business in our universe
- vec_all = avg vector of all words in all of the reviews of each person
- vec_j = avg vector of all the adjectives
- vec_n = avg vector of all the nouns
- vec_v = avg vector of all the verbs

The file is on **Google Drive**

## user_review_extracts.p:
This contains all of the extracted word vector and review counts / avg stars of each user in our universe
- vec_all = avg vector of all words in all of the reviews of each person
- vec_j = avg vector of all the adjectives
- vec_n = avg vector of all the nouns
- vec_v = avg vector of all the verbs

The file is on **Google Drive**

## tor_attributes_features.p:
This contains all of attributes features in our universe
- Convert all features to numerical
- Alcohol column 'none': 0, 'full_bar': 1, 'beer_and_wine': 2
- RestaurantsAttire 'casual': 1, 'dressy': 2, 'formal': 3
- Replace Boolean to 1 and 0

The file is on **Google Drive**

## tor_users_features.p:
This contains all of users features in our universe
- Convert all features to numerical
- replace elite column with number of years having elite status
- replace friends column with number of friends
- drop name column
- replace yelping_since with membership time (days)

The file is on **Google Drive**
