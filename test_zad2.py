from zad2 import ostrougolniy_tr, tupougolniy_tr, pryamougolniy_tr

def test_ostrougolniy_tr():
    assert ostrougolniy_tr(5, 3, 4) == 6.0

def test_tupougolniy_tr():
    assert tupougolniy_tr(6, 5, 9) == 14.142135623730951

def test_pryamougolniy_tr():
    assert pryamougolniy_tr(3, 4, 5) == 6.0
