#!/usr/bin/env python3
import string
import sys
import json
import os
import itertools
from distutils.util import strtobool

class Checker():
    """
    This class is a simple plagiarism checker for case insensitive matching.
    """
    def __init__(self, input_text, master_text, check_synonyms=True, chck_len=6):
        """
        Feed two strings of text into this class. The second string
        is the text to check against for plagiarism.
        """
        self.input_text = input_text
        self.master_text = master_text
        self.check_synonyms = bool(strtobool(check_synonyms))
        self.chck_len = chck_len
        self.synonyms = json.load(open(os.path.dirname(os.path.abspath(__file__)) +'/support/src.json', 'r'))
        self.prep()
        self.check()

    def prep(self):
        translator = str.maketrans('', '', string.punctuation)
        #remove punctuation
        self.input_list = self.input_text.translate(translator)

        #put the input text into a list
        self.input_list = self.input_list.split()

        # make a master list
        self.mlist = self.master_text.translate(translator)
        self.mlist = self.mlist.split()
        
    def check_syns(self):
        self.mutator_list = []
        for pos, word in enumerate(self.check_str):
            
            if word in self.synonyms.keys():
                temp_syns = []

                for key, value in self.synonyms[word].items():
                    temp_syns += value

                self.mutator_list.append(list(set(temp_syns)))
                    
            else:
                self.mutator_list.append([word])
            
        # iterate all possible combos           
        self.master_list = list(itertools.product(*self.mutator_list))
        
        for some_list in self.master_list:
            # check for plagiarism
            result = any(list(some_list) == self.mlist[k:self.chck_len+k] for k in range(len(self.mlist) -1))
            if result:
                print ("[!] Found plagiarism:", list(some_list))
                print ("=" * 50)

    def check(self):
        # take the chck_len width, make a subset and check in master iterate
        print ("[*] Processing...")
        if self.check_synonyms is True:
            print("[*] Checking Synonyms")
        
        result =''
        
        for i,j in enumerate(self.input_list):
            self.master_list = []
            self.check_str = self.input_list[i:self.chck_len+i]
            if len(self.check_str) < self.chck_len:
                continue
            #print(" [*] Block:", self.check_str)
            if self.check_str not in self.master_list:
                self.master_list.append(self.check_str)
            
            # capture each of the synonyms and assign them on location
            # Example [[1, A, B, C, D],[2],[3, A, B], [4, A, B , C]]
            if self.check_synonyms is True:
                self.check_syns()
            else:
                result = any(list(self.check_str) == self.mlist[k:self.chck_len+k] for k in range(len(self.mlist) -1))
    
                if result:
                    print ("[!] Found plagiarism:", list(self.check_str))
                    print ("=" * 50)        


if __name__ == "__main__":
    # This is meant to be used as an imported class so you must provide files and check_length here 
    # FYI, this is just for author testing.. feel free to use this, but no support...

    quick = Checker(open(sys.argv[1], 'r').read(), open(sys.argv[2], 'r').read(), sys.argv[3], int(sys.argv[4]))
