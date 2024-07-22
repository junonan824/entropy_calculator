import pytest
from entropy_calculator import text_entropy, password_entropy

def test_text_entropy():
    text = "Information entropy is a concept from information theory."
    entropy = text_entropy(text)
    assert isinstance(entropy, float)
    assert entropy > 0

def test_password_entropy():
    password = "A1b2C3d4!"
    entropy = password_entropy(password)
    assert isinstance(entropy, float)
    assert entropy > 0

if __name__ == "__main__":
    pytest.main()
