import proteosim as ps
import pyteomics
import matplotlib as plt

def test_predict_lc_retention_times():
    peps = ['DDDDD','ANANAN']
    expected = {'DDDDD': -13, 'ANANAN': 4.2}
    actual = ps.predict_lc_retention_times(peps)
    assert actual == expected
def test_select_retention_time_window():
    peptide_rt_map = {'AAAA': 1, 'BBBB': 7, 'CCCC': 13, 'DDDD': 25}
    selected = ps.select_retention_time_window(peptide_rt_map, lower_ret_time=5, upper_ret_time=10)

    assert selected == {'BBBB': 7}