# BioSeq-Alignment

## Project Overview
This repository contains a collection of scripts developed for processing and aligning biological sequence data. The project involves translating nucleotide sequences into amino acids using Python and then performing multiple sequence alignments with Clustal Omega using Bash scripts on a high-performance computing (HPC) environment.

## Contents
**sequence_translate.py:** Python script for translating nucleotide sequences to amino acids.   
**clustalAlign.sh:** Bash script to perform sequence alignment using Clustal Omega.   
**sbatch_clustalAlign.sh:** Bash script for submitting the alignment job to an HPC cluster using SLURM. 

### Prerequisites
Python (version 3.x)
Biopython library
Clustal Omega
Access to an HPC cluster with SLURM scheduling (for sbatch_clustalAlign.sh)

## Installation
1. Clone this repository to your local machine or HPC environment:
in CDL type: git clone [URL to your repository] 
2. Ensure that Python 3 and Biopython are installed.
3. Install Clustal Omega if not already available on your system.
4. Download fasta file for translation and sequence alignment.
   
## Usage
### Sequence Translation
Run sequence_translate.py with input and output file paths:
in CDL type: python sequence_translate.py [input_fasta_file] [output_fasta_file]
### Multiple Sequence Alignment
Execute clustalAlign.sh directly if running locally:
in CDL type: bash clustalAlign.sh
For HPC clusters with SLURM, use sbatch_clustalAlign.sh:
in CDL type: sbatch sbatch_clustalAlign.sh [path_to_input_directory]

## Author
Vitali Bahatyrevich

## Date
12/26/2023
