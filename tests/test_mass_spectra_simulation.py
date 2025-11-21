import proteosim as ps
def test_calculate_mol_mass():
    aa_mass_dict = {
    'A': 71.08, 'R': 156.19, 'N': 114.10, 'D': 115.09,
    'C': 103.15, 'E': 129.12, 'Q': 128.13, 'G': 57.05,
    'H': 137.14, 'I': 113.16, 'L': 113.16, 'K': 128.17,
    'M': 131.19, 'F': 147.18, 'P': 97.12, 'S': 87.08,
    'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13,
 }
    test_peptide = 'AAA'
    expected_mass =  {'AAA': 71.08 * 3}
    calculated_mass = ps.calculate_mol_mass(test_peptide, aa_mass_dict)
    assert calculated_mass == expected_mass

def test_calculate_mol_mass_collection():
    aa_mass_dict = {
    'A': 71.08, 'R': 156.19, 'N': 114.10, 'D': 115.09,
    'C': 103.15, 'E': 129.12, 'Q': 128.13, 'G': 57.05,
    'H': 137.14, 'I': 113.16, 'L': 113.16, 'K': 128.17,
    'M': 131.19, 'F': 147.18, 'P': 97.12, 'S': 87.08,
    'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13,
 }
    peptides = ['AA','PEP']
    expected = {'AA': 71.08 * 2, 'PEP': 97.12 + 129.12 + 97.12}
    actual = ps.calculate_mol_mass_collection(peptides,aa_mass_dict)

    assert actual == expected

def test_calculate_mz_collection():
    peptide_mass_map = {'AA': 142.16, 'PEP': 323.36}
    actual = ps.calculate_mz_collection(peptide_mass_map, charge=2)
    expected = {'AA': (142.16 + (2 * 1.007)) / 2, 'PEP': (323.36 + (2 * 1.007)) / 2}

    assert actual == expected

def test_fragment_peptide():
    peptide = 'PEPT'
    expected = ['P','PE','PEP','T','PT','EPT']
    actual = ps.fragment_peptide(peptide)

    assert set(actual) == set(expected)