"""
base class for extracting review features, enforces methods
"""
from abc import ABC, abstractmethod
import io
import numpy as np


class ReviewFeatureExtractor(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def extract(self, reviewset):
        """ iterates through the reviewset and extract the desired dataframe """
        pass


class ExtractBoW(ReviewFeatureExtractor):
    WORD_TYPE_ALL = 'all'
    WORD_TYPE_NOUN = 'noun'
    WORD_TYPE_ADJ = 'adj'
    WORD_TYPE_VERB = 'verb'
    UNK_IDX = 0
    UNK_TOKEN = '<unk>'

    """ extracts the bag of words vector from each review and averages the vectors"""
    def __init__(self, voc_size, word_type=None):
        super().__init__()
        self.voc_size = voc_size
        if word_type:
            self.word_type = word_type
        else:
            self.word_type = self.WORD_TYPE_ALL

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

    def extract(self, reviewset):
        pass
