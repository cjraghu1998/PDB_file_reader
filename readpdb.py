# From BioPython Documentation https://biopython.org/docs/dev/api/ and https://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ/



from Bio.PDB.PDBParser import PDBParser #import PDBParser from Bio.PDB module 
from Bio.SeqUtils import seq1 #seq1 part of SeqUtils object converts protein sequence from three-letter to one-letter code.
import pandas as pd #import pandas


#Create PDBParser object
pdb_reader = PDBParser(PERMISSIVE=1) #PERMISSIVE is a boolean flag, is set to 1 so that EXCEPTIONS to constructing SMCRA (Structure, Model, Chain, Residue, Atom) Model is not fatal, but missing atoms will still exist
structure_id="3eml"
filename="3eml.pdb"  #path_to_protein_file
structure = pdb_reader.get_structure(structure_id, filename)

model = structure[0]

for chain in model: 
    for residue in chain:
        for atom in residue:
            if atom.get_name() == 'CA': 
                df = print(atom.get_serial_number(), seq1(residue.get_resname()), residue.get_id()[1], chain.get_id())

                # Prints Atom Number, 1-letter-amino-acid converted Residue Name, Residue number, Chain Name
                
df.pd.to_csv('3eml.csv')
