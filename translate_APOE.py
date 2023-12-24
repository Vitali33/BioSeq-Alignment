import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Ensure the correct number of command-line arguments are provided
if len(sys.argv) < 3:
    raise Exception("Two arguments are required: input fasta file and output fasta file")

# assigns arguments to variables
infile = sys.argv[1]
outfile = sys.argv[2]

# create a file handle
records = SeqIO.parse(infile, "fasta")

# initiate an empty list
amino_acids = []

# iterate through sequence records
for record in records:
    # Translate the sequence of the record to the stop codon
    translated_seq = record.seq.translate()
    # Create a new SeqRecord with the translated sequence but retaining the metadata
    new_record = SeqRecord(translated_seq, id=record.id, description=record.description)
    # append the translated records to the list
    amino_acids.append(new_record)
# write the fasta output file.
SeqIO.write(amino_acids, outfile, "fasta")
