from TestLibrary import check_response
from File import reverse


def test_reverse():
    assert reverse("Говно?") == "?онвоГ"


def test_get_response():
    assert check_response() == 200