
import sys
import os
import subprocess
import pytest

# Set up for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

def test_exercise01():
    import os
    import exercise01
    
    assert os.environ['my_var'] == 'value'

def test_exercise02():
    import exercise02

    # assert that subprocess is in namespace of exercise02
    assert hasattr(exercise02, "subprocess")

    with open("sample.txt", "r") as f:
        text = f.read()
    
    assert exercise02.run_subprocess() == text

# Test for command line functionality
def test_exercise03():
    # Mock a test file with known content
    test_filename = 'test_file.txt'
    test_content = 'This is a test file with eight words.'
    with open(test_filename, 'w') as file:
        file.write(test_content)

    # Run the script using subprocess
    result = subprocess.run(['python', 'exercise03.py', test_filename], capture_output=True, text=True)

    # Clean up the test file
    subprocess.run(['rm', test_filename])

    # Check if the output is as expected
    assert '8' in result.stdout

# Test for command line functionality
def test_exercise04():
    # Test Case 1: Word appears multiple times
    test_filename1 = 'test_file1.txt'
    test_content1 = 'Test this test file. Test word appears three times.'
    with open(test_filename1, 'w') as file:
        file.write(test_content1)

    result = subprocess.run(['python', 'exercise04.py', test_filename1, 'Test'], capture_output=True, text=True)
    subprocess.run(['rm', test_filename1])
    assert '2' in result.stdout, f"Failed Test Case 1: Expected 2, got {result.stdout}"

    # Test Case 2: Word does not appear
    test_filename2 = 'test_file2.txt'
    test_content2 = 'Another file without the specified word.'
    with open(test_filename2, 'w') as file:
        file.write(test_content2)

    result = subprocess.run(['python', 'exercise04.py', test_filename2, 'missing'], capture_output=True, text=True)
    subprocess.run(['rm', test_filename2])
    assert '0' in result.stdout, f"Failed Test Case 2: Expected 0, got {result.stdout}"
