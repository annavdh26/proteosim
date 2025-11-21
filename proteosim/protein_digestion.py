import re
enzyme_cleavage_patterns = {
    'LysC': r'(?<=K)',
    'LysN': r'(?=K)',
    'ArgC': r'(?<=R)',
    'Trypsin': r'(?<=[KR])(?!P)',
}

def digest_protein_sequence(protein_seq, cleave_pattern):
    """
    Digest a protein sequence using the specified cleavage pattern.

    Parameters
    ----------
    protein_seq : str
        The amino-acid sequence of the protein to be digested.
    cleave_pattern : str
        The regex pattern defining the cleavage sites.
    Returns
    -------
    list
        A list of peptide sequences resulting from the digestion.

    """
    
    peptides = re.split(cleave_pattern, protein_seq)

    print(peptides)
    print(f'Nr. of digested peptides: {len(peptides)}')
    filtered = [pep for pep in peptides if min_length <= len(pep) <= max_length] # list comprehension for filtering

    filtered

def digest_protein_collection(protein_map, cleave_pattern, min_pep_len=5, max_pep_len=30):
    """
    Digest a collection of protein sequences using the specified cleavage pattern and filter peptides by length.

    Parameters
    ----------
    protein_map : dict
        A dictionary mapping protein IDs to their amino-acid sequences.
    cleave_pattern : str
        The regex pattern defining the cleavage sites.
    min_pep_len : int, optional
        Minimum peptide length to retain (default is 5).
    max_pep_len : int, optional
        Maximum peptide length to retain (default is 30).
    Returns
    -------
    dict
        A dictionary mapping protein IDs to lists of peptide sequences resulting from the digestion. (filtered by length)
    """
    digested = {}

    for protein_id, sequence in protein_map.items():

        # digest the sequence
        peptides = re.split(cleave_pattern, sequence) # mit re.split nach mustern trennen

        # filter by length
        filtered = [pep for pep in peptides if min_pep_len <= len(pep) <= max_pep_len]

        # store result
        digested[protein_id] = filtered

    return digested

def compute_sequence_coverage(protein_seq, peptides):
    """
    Compute the sequence coverage of a protein given a list of peptides.

    Parameters
    ----------
    protein_seq : str
        The amino-acid sequence of the protein.
    peptides : list
        A list of peptide sequences.
    Returns
    -------
    float
        The sequence coverage as a percentage.
    """
    covered= set() # eindeutig abgedeckte positionen
    
    for pep in peptides:
        posi= protein_seq.find(pep)
        if posi != -1:
            rangee = range(posi,posi+len(pep))
            for j in rangee:
                covered.add(j)
    n_covered_positions = len(covered)
    total_length=len(protein_seq)
    coverage = (n_covered_positions / total_length) * 100

    return coverage
    