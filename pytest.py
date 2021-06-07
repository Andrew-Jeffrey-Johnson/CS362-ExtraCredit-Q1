import pytest
import question1

# Successful test
def test_empty():
	assert question1.question1("Hello, World") == "World Hello,", "Failed to say Hello"
