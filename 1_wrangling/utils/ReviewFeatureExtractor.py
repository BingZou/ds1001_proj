"""
base class for extracting review features, enforces methods
"""
from abc import ABC, abstractmethod
import io
import numpy as np
import nltk


class ReviewFeatureExtractor(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def extract(self, reviewset):
        """ iterates through the reviewset and extract the desired dataframe """
        pass


class ExtractBoW(ReviewFeatureExtractor):
    WORD_TYPE_ALL = 'all'
    WORD_TYPE_NOUN = 'N'
    WORD_TYPE_ADJ = 'J'
    WORD_TYPE_VERB = 'V'
    UNK_IDX = 0
    UNK_TOKEN = '<unk>'

    """ extracts the bag of words vector from each review and averages the vectors"""
    def __init__(self, voc_size):
        super().__init__()
        self.voc_size = voc_size

        # embeddings:
        self.token2id = None
        self.id2token = None
        self.loaded_embeddings = None

    def load_word_vecs(self, vec_path):
        """ loads the pretrained word vectors """
        fin = io.open(vec_path, 'r', encoding='utf-8', newline='\n', errors='ignore')
        n, d = map(int, fin.readline().split())
        loaded_embeddings = np.zeros((self.voc_size + 1, d))
        token2id = {self.UNK_TOKEN: self.UNK_IDX}
        id2token = [self.UNK_TOKEN]
        loaded_embeddings[0, :] = np.zeros(d)  # UNK

        for i, line in (enumerate(fin)):
            if i >= self.voc_size:
                break
            s = line.split()
            loaded_embeddings[i + 1, :] = np.asarray(s[1:])
            token2id[s[0]] = i + 1
            id2token.append(s[0])

        self.token2id = token2id
        self.id2token = id2token
        self.loaded_embeddings = loaded_embeddings

    def extract(self, review_text_set, word_type=WORD_TYPE_ALL):
        """ given a list of raw review texts, extract the relevant type of average word vector """
        assert self.loaded_embeddings is not None, "No embeddings found, cannot extract"
        cur_vec = np.zeros(self.loaded_embeddings.shape[1])

        cur_token_dict = {}
        # first count the words in the vocab
        for t in review_text_set:
            for token, tag in nltk.pos_tag(nltk.word_tokenize(t)):
                if word_type == self.WORD_TYPE_ALL or tag[0] == word_type:
                    if token in self.token2id:
                        if token in cur_token_dict:
                            cur_token_dict[token] += 1
                        else:
                            cur_token_dict[token] = 1

        # assemble the vector using log weights
        cur_vec_weight = 0
        for cur_token in cur_token_dict.keys():
            cur_id = self.token2id[cur_token]
            cur_vec += self.loaded_embeddings[cur_id] * np.log(cur_token_dict[cur_token])
            cur_vec_weight += np.log(cur_token_dict[cur_token])

        if cur_vec_weight > 0:
            return cur_vec / cur_vec_weight
        else:
            return np.zeros(self.loaded_embeddings.shape[1])

