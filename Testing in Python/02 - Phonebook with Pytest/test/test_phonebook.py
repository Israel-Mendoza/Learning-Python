import pytest

from src.phonebook import Phonebook


# SETTING UP THE FIXTURES:


@pytest.fixture
def phonebook(tmpdir: str) -> Phonebook:  # The name of the resource must match the name of the argument in the tests
    """Provides an empty Phonebook"""
    phonebook = Phonebook(tmpdir)
    yield phonebook
    # Clearing code goes here...
    phonebook.clear()


def test_lookup_by_name(phonebook: Phonebook) -> None:
    phonebook.add("Israel", "12345")
    number: str = phonebook.lookup("Israel")
    assert number == "12345"


def test_contains_all_names(phonebook: Phonebook) -> None:
    phonebook.add("Israel", "12345")
    phonebook.add("Arthur", "98765")
    phonebook.add("Mago", "45612")
    assert phonebook.all_names == {"Israel", "Arthur", "Mago"}


def test_missing_name(phonebook: Phonebook) -> None:
    with pytest.raises(KeyError):
        phonebook.lookup("Roberto")


def test_empty_phonebook_is_consistent(phonebook: Phonebook) -> None:
    assert phonebook.is_consistent is True


def test_is_consistent_with_one_entry(phonebook: Phonebook) -> None:
    phonebook.add("Israel", "12345")
    assert phonebook.is_consistent is True


def test_is_consistent_with_different_entries(phonebook: Phonebook) -> None:
    phonebook.add("Israel", "12345")
    phonebook.add("Mago", "32145")
    phonebook.add("Arthur", "22233")
    assert phonebook.is_consistent


def test_is_inconsistent_with_equal_phone_number(phonebook: Phonebook) -> None:
    phonebook.add("Israel", "12345")
    phonebook.add("Mago", "12345")
    assert not phonebook.is_consistent


def test_is_inconsistent_when_new_phone_is_prefix(phonebook: Phonebook) -> None:
    phonebook.add("Israel", "12345")
    phonebook.add("Margarita", "123")  # Is prefix of existing phone number
    assert not phonebook.is_consistent


def test_is_inconsistent_when_old_phone_is_prefix(phonebook: Phonebook) -> None:
    phonebook.add("Israel", "123")
    phonebook.add("Margarita", "12345")  # Previous phone number is prefix of this one
    assert not phonebook.is_consistent


# Using a parameterized decorator to test several cases in one test:
@pytest.mark.parametrize(
    ("first_contact", "second_contact", "is_consistent"), [
        # (("Israel", "12345"), True),
        (("Israel", "12345"), ("Margarita", "54321"), True),
        (("Israel", "12345"), ("Margarita", "12345"), False),
        (("Israel", "12345"), ("Margarita", "123"), False),
        (("Israel", "123"), ("Margarita", "54321"), True)
    ]
)
def test_is_consistent(phonebook: Phonebook, first_contact: tuple[str], second_contact: tuple[str],
                       is_consistent: bool) -> None:
    phonebook.add(*first_contact)
    phonebook.add(*second_contact)
    assert phonebook.is_consistent is is_consistent


# Skipping a test:
@pytest.mark.skip("Still working on this")
def test_new_feature(phonebook: Phonebook) -> None:
    assert False
