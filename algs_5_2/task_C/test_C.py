import dataclasses
import pytest

from task_C import get_rope


##################
# TEST FOR TASK C
##################


@dataclasses.dataclass
class Case:
    n: int
    lengths: list[int]
    result: int

    def __str__(self) -> str:
        return f"get_rope_{self.lengths}"


TEST_CASES = [
    Case(n=4, lengths=[1, 5, 2, 1], result=1),
    Case(n=4, lengths=[5, 12, 4, 3], result=24),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_get_rope(t: Case) -> None:
    result = get_rope(t.n, t.lengths)
    assert result == t.result
