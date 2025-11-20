
from proteosim.file_handling import read_fasta


def test_fasta_reader():
    tmp_fasta_path = 'data/dummy-proteins.fasta'
    # Read the file contents into a single string named `raw_fasta_text`.
    protein_mapg =read_fasta(tmp_fasta_path)
    # Replace the strings with your fasta content
    # which you expect to be now available as a dictionary
    assert protein_mapg['A123'] == "ABCDEFGHIJKLMN"
    assert protein_mapg['A456'] == "OPQRSTUVWXYZ"
