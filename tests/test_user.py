import pytest

# in a parametrized tests, can you pass a fixture as a value
# parametrized tests
@pytest.mark.parametrize('user, expected', [
    (normal_user, 'katherine rose'),
    (missing_details, TypeError),
])
def test_parametrize_user_full_name(user, expected):
    '''
    GIVEN a normal user (created as a fixture)
    WHEN creating the user's full name
    THEN the user's first and last name should be shown
    '''
    assert user.create_full_name(user) == expected


# unparametrised tests
def test_for_user_full_name(normal_user):
    '''
    GIVEN a normal user (created as a fixture)
    WHEN creating the user's full name
    THEN the user's first and last name should be shown
    '''
    assert normal_user.create_full_name() == 'katherine rose'

def test_for_calcalate_age(normal_user):
    assert normal_user.calculate_age() == 23

def test_for_calcalate_age_2(edge_case_date):
    assert edge_case_date.calculate_age() == 0




# python -m pytest -v
# pytest --cov=.
# python -m pytest --cov-report term-missing --cov=user tests/