#!/usr/bin/env bash
# clustalAlign.sh

# perform multiple sequence alignmnet using clustalo
clustalo -i apoe_aa.fasta -o apoe_alignment.fasta --outfmt=fasta -v --thread=1
