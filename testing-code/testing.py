#testing proves that your code works as its supposed to un response to all kinds of input its designed to receive
#testing code using pytest
#pytest library is a collection of tools that will help you write your first tests quickly and simply while supporting your tests as they grow in complexity along with your project.


#installing pytest with pip
#third-party package is a library thats developer outside the core python language.


#updating pip
#pip tool thats is used to install third-party packages.
#syntax: python -m pip install --upgrade package_name
#python -m pip install --upgrade pip
#python -m pip -tells python to run the module pip
#install --upgrade - tells python to update a package thats already been installed
#pip - specifies which third-party package to update

#installing pytest
#python -m pip install --user pytest
#we are using the core command (pip install) without the --upgrade flag.
#--user flag tells python to install this package for current user only. you can as well ignore while installing.


#testing a function 


#unit tests and test cases
#unit test verifies that one specific aspect of a functions behavior is correct.
#test case is a collection of unit tests that together prove that a function behaves as its supposed to, within the full range of situations you expect it to handle.
#a good test case:
#1. includes full range of unit tests for all the behavior you expect from a function.
#2. includes tests to prove that a function fails in the ways you expect it to.
#3. has complete coverage, meaning that it includes a full range of tests for all the code in a function.
#4. is well-organized so you can understand the set of tests you've written.



#A passing test
#the test function will call the function we're testing and we'll make an assertion about the value thats returned.
#if the assertion s correct the test will pass, if the assertion fails the test will raise an exception.
#syntax: assert function_name(arguments) == expected_output