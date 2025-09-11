import pytest

from targets.bva_api.app import validate_username_length


@pytest.mark.api
def test_username_length_4():
    result = validate_username_length("John")
    assert result == "422 TOO_SHORT"
    # "John" has 4 characters


@pytest.mark.api
def test_username_length_5():
    result = validate_username_length("Johny")
    assert result == "200 OK"
    # "Johny" has 5 characters


@pytest.mark.api
def test_username_length_6():
    result = validate_username_length("Johnny")
    assert result == "200 OK"
    # "Johnny" has 6 characters


@pytest.mark.api
def test_username_length_15():
    result = validate_username_length("Johnny_is_back1")
    assert result == "200 OK"
    # "Johnny_is_back1" has 15 characters


@pytest.mark.api
def test_username_length_29():
    result = validate_username_length("Johnny_english_is_do_you_this")
    assert result == "200 OK"
    # "Johnny_english_is_do_you_this" has 29 characters


@pytest.mark.api
def test_username_length_30():
    result = validate_username_length("Johnny_english_is_do_you_this?")
    assert result == "200 OK"
    # "Johnny_english_is_do_you_this?" has 30 characters


@pytest.mark.api
def test_username_length_31():
    result = validate_username_length("Johnny_english_is_do_you_this??")
    assert result == "422 TOO_LONG"
    # "Johnny_english_is_do_you_this??" has 31 characters
