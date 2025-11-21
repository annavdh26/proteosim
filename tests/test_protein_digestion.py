import proteosim as ps
import re
def test_digest_protein_collection():
    dummy_proteins = {
        "A111":"ABCDEFG",
        "A222":"HIJKLMN",
        "B222":"OPQRSTU"
    }

    dummy_pattern = r'$^'  # regex that never matches => no cleavage

    protein_map2 = ps.digest_protein_collection(
        dummy_proteins,
        cleave_pattern=dummy_pattern
    )

   
    assert protein_map2['A111'] == ["ABCDEFG"] #eckige klammern wichig weil man sonst mit string vergleicht und bei der funktion kommt immer liste von peptiden raus
    assert protein_map2['A222'] == ["HIJKLMN"]
    assert protein_map2['B222'] == ["OPQRSTU"]

def test_compute_sequence_coverage():
    dummy_prot_seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZZZ"
    dummy_peps = ["DEF","XYZ"]

    coverage = ps.compute_sequence_coverage(dummy_prot_seq,dummy_peps)
    assert coverage == (6/len(dummy_prot_seq)) *100