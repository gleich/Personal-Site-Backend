from stats.github import contributions


def test_contributions():
    """Test for the contributions function
    """
    response = contributions()
    assert type(response) == type({})
