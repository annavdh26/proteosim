import pyteomics
from pyteomics import achrom
import matplotlib.pyplot as plt

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


def plot_retention_time(retention_times, resolution=30):
    """
    Plot a histogram of retention times.

    Parameters
    ----------
    retention_times : list
        A list of retention times (floats).
    resolution : int, optional
        The number of bins in the histogram (default is 30).

    Returns
    -------
    histogram plot 
    """
    
    plt.hist(
        retention_times,
        bins=resolution,
        color='blue',
        alpha=0.7
    )
    plt.title('Predicted LC Retention Times')
    plt.xlabel('Retention Time (realtive)')
    plt.ylabel('Number of Peptides')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def select_retention_time_window(peptide_rt_map, lower_ret_time, upper_ret_time):
    """
    Select peptides within a specified retention time window.

    Parameters
    ----------
    peptide_rt_map : dict
        A dictionary mapping peptide sequences to their retention times (floats).
    lower_ret_time : float
        The lower bound of the retention time window.
    upper_ret_time : float
        The upper bound of the retention time window.
    Returns
    -------
    dict
        A dictionary of peptides and their retention times within the specified window.
    """
    selected_peptides = {}

    for peptide, rt in peptide_rt_map.items():
        if lower_ret_time <= rt <= upper_ret_time:
            selected_peptides[peptide] = rt

    return selected_peptides