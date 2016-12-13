# Sequence Alignment
Uses dynamic programming to handle the issue of pairwise alignment

example input (DNA bases A, C, G, T):

sequence one:  ACCGGGTACCGGGGAAAATTT

sequence two:  ACCGTACCGGAGGAAATT

output (aligned sequences) where D in sequence two is a predicted deletion from seqence one
and an I in sequence one is where an insertion may have happend in the aligned sequence two:

sequence one: ACCGGGTACCGGIGGAAAATTT

sequence two: ACCDDGTACCGGAGGDAAADTT


