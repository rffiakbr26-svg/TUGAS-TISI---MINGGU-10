from calculator import hitung

# Test Case 1
def test_penambahan():
    assert hitung('penambahan', 20, 10) == 30

# Test Case 2
def test_pengurangan():
    assert hitung('pengurangan', 3, 5) == -2

# Test Case 3
def test_pembagian():
    assert hitung('pembagian', 5, 2) == 2.5
