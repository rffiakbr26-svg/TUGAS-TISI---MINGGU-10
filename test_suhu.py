from suhu import konversi_celcius_ke_fahrenheit

# Test Case 1
def test_suhu_positif():
    assert konversi_celcius_ke_fahrenheit(17) == 62.6

# Test Case 2
def test_titik_beku():
    assert konversi_celcius_ke_fahrenheit(0) == 32.0

# Test Case 3
def test_suhu_negatif():
    assert konversi_celcius_ke_fahrenheit(-10) == 14.0
