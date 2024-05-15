import dataclasses
import pytest

from task_F import make_odd


##################
# TEST FOR TASK F
##################


@dataclasses.dataclass
class Case:
    n: str
    numbers: str
    result: str

    def __str__(self) -> str:
        return f"make_odd_{self.numbers}"


TEST_CASES = [
    Case(n='3', numbers='5 7 2', result='x+'),
    Case(n='2', numbers='4 -5', result='+'),
    Case(n='4', numbers='8 2 1 1', result='++x'),
    Case(n='3', numbers='5 7 11', result='xx'),
    Case(n='3', numbers='5 0 11', result='+x'),
    Case(n='4', numbers='5 2 11 6', result='+x+'),
    Case(n='4', numbers='2 2 11 6', result='+++'),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_make_odd(t: Case) -> None:
    result = make_odd(t.n, t.numbers)
    assert result == t.result
