amino_acid_mass_dalton = {
    'A': 71.08, 'R': 156.19, 'N': 114.10, 'D': 115.09,
    'C': 103.15, 'E': 129.12, 'Q': 128.13, 'G': 57.05,
    'H': 137.14, 'I': 113.16, 'L': 113.16, 'K': 128.17,
    'M': 131.19, 'F': 147.18, 'P': 97.12, 'S': 87.08,
    'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13,
}

def calculate_mol_mass(peptide_seq, amino_acid_mass_dict):
    """
    Calculate the molecular mass of a peptide sequence.

    Parameters
    ----------
    peptide_seq : str
        The peptide sequence (string of amino acid single-letter codes).
    amino_acid_mass_dict : dict
        A dictionary mapping amino acid single-letter codes to their masses.
    Returns
    -------
    dict
        A dictionary with the peptide sequence as the key and its molecular mass as the value.

    """
    

    mass = 0
    pepmass = {}
    for aa in peptide_seq:
        mass += amino_acid_mass_dict[aa]
    pepmass[peptide_seq] = mass
    return pepmass

def calculate_mol_mass_collection(peptides, amino_acid_mass_dict):
    """
    Calculate the molecular masses for a collection of peptide sequences.
    
    Parameters
    ----------
    peptides : list
        A list of peptide sequences (strings of amino acid single-letter codes).
    amino_acid_mass_dict : dict
        A dictionary mapping amino acid single-letter codes to their masses.

    Returns
    -------
    dict
        A dictionary with peptide sequences as keys and their molecular masses as values.
    """
    pepmass_collection = {}
    for peptide in peptides:
        mass = 0
        
        for aa in peptide:
            mass += amino_acid_mass_dict[aa]
        pepmass_collection[peptide] = mass
    return pepmass_collection

def calculate_mz_collection(peptide_mass_map, charge=2, proton_mass=1.007):
    """
    calculate the m/z values for a collection of peptides given their molecular masses.

    Parameters

    ----------
    peptide_mass_map : dict
        A dictionary mapping peptides to their molecular masses.
    charge : int, optional
        The charge state of the ions (default is 2).
    proton_mass : float, optional
        The mass of a proton (default is 1.007 Da).

    Returns
    -------
    dict
        A dictionary mapping peptides to their m/z values.
    """
    mz_map = {}
    for peptide, mass in peptide_mass_map.items():
        mz = (mass + (charge * proton_mass)) / charge
        mz_map[peptide] = mz
    return mz_map

import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(mz_values, random_count_range=(0, 30000), seed=42):
    """
    
    Plots a simulated mass spectrum based on given m/z values.
    
    Parameters
    ----------
    mz_values : dict
        A dictionary mapping peptides/fragments to their m/z values.
    random_count_range : tuple, optional
        A tuple specifying the range (min, max) for random intensity values (default is (0, 30000)).
    seed : int, optional
        Seed for the random number generator to ensure reproducibility (default is 42). 
    Returns
    -------
    plots the mass spectrum
    """
    
    np.random.seed(seed)  #reproducible

    #Zufällige Intensitäten erzeugen
    intensities = np.random.randint(random_count_range[0],random_count_range[1],size=len(mz_values))

    #Spektrum plotten
    plt.figure(figsize=(10, 6))
    plt.bar(mz_values.values(), intensities, width=1.0)

    plt.xlabel("m/z")
    plt.ylabel("Intensity")
    plt.title("Simulated Mass Spectrum")

    plt.show()

def fragment_peptide(peptide):
    """
    Generate peptide fragments (b-ions and y-ions) from a given peptide sequence.

    Parameters
    ----------
    peptide : str
        The peptide sequence to be fragmented.
    Returns
    -------
    list
        A list of peptide fragments.
    """
    fragments = []


    for i in range(1, len(peptide)):
        fragments.append(peptide[:i])
    for i in range(1,len(peptide)):
        fragments.append(peptide[-i:])

    return fragments