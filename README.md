# PlagiarismChecker
Quick script to check for plagiarism between two documents. 

Supports variable length checking and synonyms (adds significant time).

Synonyms obtained from: https://github.com/FinNLP/synonyms

**Documents must be TEXT files!**

## How to use

This was made to be a class, but if you want to use it as is:

```
python3 ./check.py questionable_file.txt possible_source.txt check_synonyms(true/false) length_to_check

time python3 ../PlagiarismChecker/check.py test_output.txt input.txt true 6
[snip]

```

## Speed results

```
$ wc test_output.txt
2  202 1170 test_output.txt

$ cat data/fw/input.txt
4078  214831 1230725


$ time python3 ../PlagiarismChecker/check.py test_output.txt input.txt t 6

real    8m19.381s
user    8m19.288s
sys 0m0.028s

$ time python3 ../PlagiarismChecker/check.py test_output.txt input.txt f 6

real    0m21.929s
user    0m21.880s
sys 0m0.044s

```
