import pickle
import csv

import re
from excel_util import XlToList


def prune_phone_numbers(token_list):
    """ Prunes out phone numbers from the given token
    list and replaces it with the word "phone_number """
    pruned_tokens = []
    regex_phone_number = re.compile("\d{10}")
    for token in token_list:
        pruned_tokens.append(regex_phone_number.sub("phone_number", token))
    return pruned_tokens


def load_from_file(file_path):
    return pickle.load(open(file_path, "rb"))


def save_to_file(obj, file_path):
    pickle.dump(obj, open(file_path, "wb"))


def read_and_save_token_from_excel(xl_file_path):
    sentences = all_sentences(xl_file_path)
    print "sentences length: ", len(sentences)
    all_words = reduce(lambda a_word_ist, another_word_list: a_word_ist + another_word_list,
                       [sentence.split() for sentence in all_sentences])
    print "words length: ", len(all_words)
    save_to_file(all_words, "words.dat")


def all_tokens(xl_file_path):
    converter = XlToList()
    test_sentences = converter.convert(xl_file_path)
    print "sentences length: ", len(test_sentences)
    all_words = reduce(lambda a_word_ist, another_word_list: a_word_ist + another_word_list,
                       [sentence.split() for sentence in test_sentences])
    return all_words


def all_sentences(xl_file_path):
    converter = XlToList()
    sentences = converter.convert(xl_file_path)
    return sentences


def _read_lines(filename):
    with open(filename) as f:
        ads = f.readlines()
    return ads


def _write_to_csv(filename, results):
    with open(filename, "w") as output_file:
        ad_writer = csv.writer(output_file)
        for key in results:
            ad_writer.writerow(key)
