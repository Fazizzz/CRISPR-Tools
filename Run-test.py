# Install dependencies 

pip install biopython

python3 -m pip install biopython

# Alternative if using conda: conda install -c conda-forge biopython

python -c "import Bio; print(Bio.__version__)"

from Bio import SeqIO
from Bio.Seq import Seq

seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(seq)
print(seq.translate())
