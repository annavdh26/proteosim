# proteosim


Proteosim Course Package

with the functions in this package we can simulate a MS. It includes reading Fasta files with seqences, digesting them and calculating the m/z values and retention times.

installation instructions: 
pip install -r requirements.txt
pip install

input: FASTA file
processing steps: digestion, chromatography, MS simulation
outputs: mz tables, fragment spectra

overview functions:

protein digestion 
-digest_protein_sequence,
-digest_protein_collection,
-compute_sequence_coverage,

liquid_chromatography
-predict_lc_retention_times,
-plot_retention_time,
-select_retention_time_window

mass_spectra_simulation
-amino_acid_mass_dalton,
-calculate_mol_mass,
-calculate_mol_mass_collection,
-calculate_mz_collection,
-fragment_peptide,
-plot_spectrum

experimet notebook: ms_experiment_final.ipynb
