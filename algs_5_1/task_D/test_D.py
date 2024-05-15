import dataclasses
import pytest

from task_D import safe_places


##################
# TEST FOR TASK D
##################


@dataclasses.dataclass
class Case:
    board: str
    result: str

    def __str__(self) -> str:
        return f"safe_places_{self.result}"


TEST_CASES = [
    Case(board="""********
********
*R******
********
********
********
********
********""", result='49'),
    Case(board="""********
******B*
********
***R****
********
********
******R*
********""", result='31'),
    Case(board="""********
********
********
*******R
********
********
********
********""", result='49'),
    Case(board="""********
********
**B*****
********
********
********
********
********""", result='52'),
    Case(board="""********
********
********
********
********
********
********
**B*****""", result='56'),
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_safe_places(t: Case) -> None:
    result = safe_places(t.board)
    assert result == t.result
