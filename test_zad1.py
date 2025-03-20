from zad1 import raznostoronniy_tr, ravnobedrenniy_tr, ravnostoronniy_tr


def test_raznostoronniy_tr():
    assert raznostoronniy_tr(2, 4,5) == 3.799671038392666

def test_ravnobedrenniy_tr():
    assert ravnobedrenniy_tr(5, 5, 8) == 12.0

def test_ravnostoronniy_tr():
    assert ravnostoronniy_tr(7, 7, 7) == 21.21762239271875
