from Exercises._Common.utils import ExerciseUtils


def test_search_using_re():
    """
    using search from re module
    """
    exu = ExerciseUtils()
    count = exu.run_search('mbox-short.txt', 'From:')
    assert count == 27
