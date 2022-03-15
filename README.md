# PDB_file_reader
Written in BioPython

Referenced from BioPython Documentation https://biopython.org/docs/dev/api/ and https://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ/

Reads all the residue numbers, atom numbers, residue names and chain name and exports all these fields to a tab delimited CSV file using the PDBParser object of BIO.PDB module.
Converts 3 letter amino acid sequences to 1 letter amino acids using seq1 object of BIO.SeqUtils module.

Required Dependencies:
Python 3+
BioPython