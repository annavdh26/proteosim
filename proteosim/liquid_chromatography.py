

def predict_lc_retention_times(peptides):
    """
    Predict the liquid chromatography retention times for a list of peptides.

    Parameters
    ----------
    peptides : list
        A list of peptide sequences (strings).
    Returns
    -------
    dict
        A dictionary mapping peptide sequences to their predicted retention times (floats).
    """
    rt_map = {}   # leeres Dictionary

    for peptide in peptides:
        pep = peptide.strip()  # sicherstellen, dass keine Leerzeichen drin sind

        # RT berechnen (gibt EINEN float zurück)
        rt = achrom.calculate_RT(
            pep,
            achrom.RCs_guo_ph7_0,
            raise_no_mod=False
        )

        # Ab in das Dictionary
        rt_map[pep] = round(rt, 2)

    return rt_map

