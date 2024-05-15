import dataclasses
import pytest

from task_A import tree_painter


##################
# TEST FOR TASK A
##################


@dataclasses.dataclass
class Case:
    vasya: str
    masha: str
    result: str

    def __str__(self) -> str:
        return f"tree_painter_{self.result}"


TEST_CASES = [
    Case(vasya='1 2', masha='7 1', result='8'),
    Case(vasya='7 1', masha='1 2', result='8'),
    Case(vasya='-1 2', masha='-7 1', result='8'),
    Case(vasya='-7 1', masha='-1 2', result='8'),
    Case(vasya='1 2', masha='4 2', result='8'),
    Case(vasya='1 2', masha='4 5', result='11'),
    Case(vasya='4 5', masha='1 2', result='11'),
    Case(vasya='-4 5', masha='-1 2', result='11'),
    Case(vasya='1 2', masha='-4 6', result='14'),
    Case(vasya='1 0', masha='3 1', result='4'),
    Case(vasya='3 1', masha='1 0', result='4'),
    Case(vasya='1 0', masha='3 0', result='2'),
    Case(vasya='1 0', masha='1 0', result='1'),
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_tree_painter(t: Case) -> None:
    result = tree_painter(t.vasya, t.masha)
    assert result == t.result
