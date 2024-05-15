"""Wrong output, do not use"""

import dataclasses
import pytest

from task_H import run


##################
# TEST FOR TASK H
##################


@dataclasses.dataclass
class Case:
    L: int
    x1: int
    v1: int
    x2: int
    v2: int
    result: str

    def __str__(self) -> str:
        return f"run_{self.L} {self.x1} {self.v1} {self.x2} {self.v2}"


TEST_CASES = [
    Case(L=6, x1=3, v1=1, x2=1, v2=1, result=1.0),
    Case(L=12, x1=8, v1=10, x2=5, v2=20, result=0.3),
    Case(L=5, x1=0, v1=0, x2=1, v2=2, result=2.0),
    Case(L=10, x1=7, v1=-3, x2=1, v2=4, result=0.8571428571),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_run(t: Case) -> None:
    result = run(t.L, t.x1, t.v1, t.x2, t.v2)
    assert result == t.result
