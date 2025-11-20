def read_fasta(filepath):
    """
    Read a FASTA file and return a dictionary mapping protein IDs to their amino-acid sequences.
    
    Parameters
    ----------
    filepath : str
        Path to the FASTA file to be read.
    Returns
    -------
    dict
        A dictionary mapping protein IDs to their amino-acid sequences.
    """
    protein_map = {}
    current_id = None
    current_sequence = []

    with open(filepath, 'r', encoding='utf-8') as fasta_handle:
        for line in fasta_handle:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('>'):
                if current_id is not None:
                    protein_map[current_id] = ''.join(current_sequence)
                    current_sequence = []
                current_id = stripped.split('|')[1]
            else:
                current_sequence.append(stripped)

    if current_id is not None:
        protein_map[current_id] = ''.join(current_sequence)
        print(current_id)

    n_proteins = len(protein_map)
    print(f'Total proteins: {n_proteins}')

    # Print: protein_id: length of amino-acid sequence
    for prot_id, seq in protein_map.items():
        print(f'{prot_id}: {len(seq)}')

    # Check if any IDs repeat
    if len(protein_map) == len(set(protein_map.keys())):
        print("All IDs are unique.")
    else:
        print("Some IDs are duplicated.")

    return protein_map


    