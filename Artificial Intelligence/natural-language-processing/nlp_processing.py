import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def tokenizer_from_sentences(sentences, num_words=100, lower=True):
    tokenizer = keras.preprocessing.text.Tokenizer(num_words=num_words, lower=lower)
    tokenizer.fit_on_texts(sentences)
    return tokenizer

def text_to_sequence(sentences, tokenizer):
    return tokenizer.texts_to_sequences(sentences)

def seq_padding(sequences, max_length=-1, padding='post', truncating='post', value=0):
    if max_length == -1:
        max_length = max(len(seq) for seq in sequences)
    x = keras.preprocessing.sequence.pad_sequences(
        sequences,
        maxlen=max_length,
        padding=padding,
        truncating=truncating,
        value=value,
    )
    return x

def save_to_file(data, filepath):
    np.save(filepath, np.array(data, dtype=object))

"""
Usage example

sentences = [
    "I love Data Science",
    "I love Python",
    "I love NodeJS",
    "I love Java",
]

tokenizer = tokenizer_from_sentences(sentences)
sequences = text_to_sequence(sentences, tokenizer)
padded_sequences = seq_padding(sequences, max_length=10)

save_to_file(padded_sequences, "processed_data.npy")

"""
