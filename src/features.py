import numpy as np
import pandas as pd

class TextMetricCalculator:
    """
    A class responsible for extracting statistical features from text.
    """
    
    def calculate(self, text: str) -> pd.Series:
        if not isinstance(text, str):
            text = str(text)
            
        words = text.split()
        sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 1]
        
        word_count = len(words)
        char_count = len(text.replace(" ", ""))
        avg_word_length = np.mean([len(w) for w in words]) if words else 0
        sentence_count = len(sentences)
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
        
        return pd.Series({
            'word_count': word_count,
            'char_count': char_count,
            'avg_word_length': avg_word_length,
            'sentence_count': sentence_count,
            'avg_sentence_length': avg_sentence_length
        })

    def process_dataframe(self, df: pd.DataFrame, text_column: str = 'explanation') -> pd.DataFrame:
        print(f"Extracting features from column: {text_column}...")
        metrics = df[text_column].apply(self.calculate)
        return pd.concat([df, metrics], axis=1)