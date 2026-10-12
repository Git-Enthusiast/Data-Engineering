"""Automated checks for the Task Tracker. Run with: python tests.py"""
from main import add_task, complete_task, remove_task


def raises_value_error(function, *args):
    try:
        function(*args)
    except ValueError:
        return True
    return False


def test_add_task():
    tasks = add_task([], "Buy milk")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Buy milk"
    assert tasks[0]["done"] is False


def test_empty_title_rejected():
    assert raises_value_error(add_task, [], "   ")


def test_complete_task():
    tasks = add_task([], "Buy milk")
    complete_task(tasks, 1)
    assert tasks[0]["done"] is True


def test_remove_task():
    tasks = add_task(add_task([], "A"), "B")
    remove_task(tasks, 1)
    assert [t["title"] for t in tasks] == ["B"]


def test_invalid_number_rejected():
    tasks = add_task([], "Buy milk")
    assert raises_value_error(complete_task, tasks, 99)
    assert raises_value_error(remove_task, tasks, 0)


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    failed = 0
    for test in tests:
        try:
            test()
            print("PASS", test.__name__)
        except AssertionError:
            failed += 1
            print("FAIL", test.__name__)
    print(f"\n{len(tests) - failed} passed, {failed} failed")
