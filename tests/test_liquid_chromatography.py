import proteosim as ps
import pyteomics

def test_predict_lc_retention_times():
    peps = ['DDDDD','ANANAN']
    expected = {'DDDDD': -13, 'ANANAN': 4.2}
    actual = ps.predict_lc_retention_times(peps)
    assert actual == expected
