## Extracted Features

### wip_vec_reviews.p
Each review had its text vectorized using fasttext 300d vectors by first tabulating words by count, and then weighting each word by the log of their count in the text

there are 4 vectors to represent 4 sets of words in the text:
- all: all words are counted
- noun: only nouns tagged by nltk are counted
- adj: only adjectives tagged by nltk are counted
- verb: only verbs tagged by nltk are counted

## vec_sim.p
For each review, the average vector of all reviews on the same business excluding that particular review is computed. The same is done for all reviews by the same user excluding that particular review. This is also done for noun, adj, and verb vectors.

For each of the vector types, a cosine similarity measure is taken between the business vectors and the user vectors.
- cos_sim_all: cos similarity between vectors of all words
- cos_sim_noun: cos similarity between vectors of nouns
- cos_sim_adj: cos similarity between vectors of adjectives
- cos_sim_verb: cos similarity between vectors of verbs

## dinesafe.p
For each business, when mapped to a dinesafe restaurant, the health categorizations are pulled into this file

Inspection Result Dummy Columns:
- dinesafe_rev_closed - the restaurant was closed as a result of failing inspection
- dinesafe_rev_condpass - the restaurant received a conditional pass, needs to work on some issues
- dinesafe_rev_pass - the restaurant passed

Issue Severity Columns:
- dinesafe_status_cruicial - the issues were critical
- dinesafe_status_minor - the issues were minor
- dinesafe_status_na - this field was not applicable
- dinesafe_status_significant - the issues were significant

## bus_rev_res_offset_hu.p
All values are based on data before current day.   
- count_review - total number of reviews
- avg_stars - average stars
- count_funny - total number of reviews marked as funny
- count_cool - total number of reviews marked as cool
- count_useful - total number of reviews marked as useful
- avg_sent_score_compound - average sentiment score using compound method
- avg_sent_score_net - average sentiment score ((# positive words - # negative words) / # of words)
- avg_review_length - average review length
- avg_punc_count - average number of punctuations (exclude .,)
- avg_word_len - average word length

## user_rev_res_offset_hu.p

- count_review - total number of reviews
- avg_stars - average stars
- count_funny - total number of reviews marked as funny
- count_cool - total number of reviews marked as cool
- count_useful - total number of reviews marked as useful
- avg_sent_score_compound - average sentiment score using compound method
- avg_sent_score_net - average sentiment score ((# positive words - # negative words) / # of words)
- avg_review_length - average review length
- avg_punc_count - average number of punctuations (exclude .,)
- avg_word_len - average word length

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
