import dataclasses
import pytest

from task_J import two_rectangles


##################
# TEST FOR TASK J
##################


@dataclasses.dataclass
class Case:
    i_max: int
    j_max: int
    field: list[list[str]]
    result: str

    def __str__(self) -> str:
        return f"two_rectangles_{self.field}"


TEST_CASES = [
    Case(i_max=2, j_max=1, field=[["#"], ["."]], result="NO"),
    Case(i_max=2, j_max=2, field=[[".", "."], ["#", "#"]], result="YES\n..\nab"),
    Case(i_max=1, j_max=3, field=[["#", "#", "#"]], result="YES\nabb"),
    Case(i_max=1, j_max=5, field=[["#", "#", "#", "#", "."]], result="YES\nabbb."),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_two_rectangles(t: Case) -> None:
    result = two_rectangles(t.i_max, t.j_max, t.field)
    assert result == t.result
