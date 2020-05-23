from stats import github


def test_contributions():
    """Test for the contributions function
    """
    response = github.contributions()
    assert type(response) == type({})
