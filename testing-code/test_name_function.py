from name_function import get_formatted_name #import the function we want to test.

def test_first_last_name(): #define the test function need to start with test followed by underscore.any function that start with test_ will be discoverd by pytest and will be running as part of the testing process. test name should be longer and descriptive. you never call  the function yourself pytest will find the function and run it for you.
    """"Do name like 'Caleb Cheptumo' work?"""
    formatted_name = get_formatted_name('caleb', 'cheptumo') # call the function we want to test and store the result in a variable. which takes two arguments first and last name.
    assert formatted_name == 'Caleb Cheptumo' # make assertion about the result of the function call. if the result is what we expect the test will pass. if the result is not what we expect the test will fail.
    #assertion is a claim about a condition.
    