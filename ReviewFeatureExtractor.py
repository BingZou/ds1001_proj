"""
base class for extracting review features, enforces methods
"""
from abc import ABC, abstractmethod


class ReviewFeatureExtractor(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def extract(self, reviewset):
        """ iterates through the reviewset and extract the desired dataframe """
        pass

