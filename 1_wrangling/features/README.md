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