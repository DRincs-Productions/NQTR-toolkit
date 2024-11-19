import pytest


def test_button():
    """Base tests, to prove that default button  state is one we expect"""
    from pythonpackages.nqtr.button import Button

    some_button = Button()

    assert some_button.align == (0, 0)
    assert some_button.name == ""
    assert some_button.label_name is None
    assert some_button.button_icon is None
    assert some_button.button_icon_selected is None
    assert some_button.picture_in_background is None
    assert some_button.picture_in_background_selected is None
    assert some_button.xalign == 0
    assert some_button.yalign == 0
    assert some_button.hidden is False
    assert some_button.default_label_name is None


def test_align_not_working_as_expected():
    """Previously this test was showcasing problem with align"""
    from pythonpackages.nqtr.button import Button

    some_button = Button()

    assert type(some_button.align) is tuple
    assert some_button.align == (0, 0)

    some_button.xalign = 0

    assert type(some_button.align) is tuple
    assert some_button.align == (0, 0)


@pytest.mark.parametrize(
    "xalign,yalign,xexpected,yexpected",
    [
        (0, 0, 0, 0),
        (1, 1, 1, 1),
        (-1, -1, -1, -1),
        (1.1, 1.2, 1.1, 1.2),
        (-1.1, -1.2, -1.1, -1.2),
        ("", "", 0, 0),
        (False, False, 0, 0),
        (None, None, 0, 0),
        ({}, {}, 0, 0),
        ("0", "0", "0", "0"),
    ],
)
def test_button_aligns_accept_any_param_except_none(
    xalign, yalign, xexpected, yexpected
):
    """Check if various xalign, yalign attributes are properly saved to the class, all
    Falsey values should be converted to 0 (special caveat for "0", it's not False-y,
    but some may thing it is)
    """
    from pythonpackages.nqtr.button import Button

    some_button = Button(xalign=xalign, yalign=yalign)

    assert some_button.xalign == xexpected
    assert some_button.yalign == yexpected
    assert type(some_button.xalign) is type(xexpected)
    assert type(some_button.yalign) is type(yexpected)
