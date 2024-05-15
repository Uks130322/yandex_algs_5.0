import dataclasses
import pytest

from task_G import destroy


##################
# TEST FOR TASK G
##################


@dataclasses.dataclass
class Case:
    my_solders: int
    casern: int
    enemies: int
    result: int

    def __str__(self) -> str:
        return f"destroy_{self.my_solders}, {self.casern}, {self.enemies}"


TEST_CASES = [
    Case(my_solders=10, casern=11, enemies=15, result=4),
    Case(my_solders=1, casern=2, enemies=1, result=-1),
    Case(my_solders=12, casern=20, enemies=5, result=3),
    Case(my_solders=15, casern=20, enemies=5, result=2),
    Case(my_solders=15, casern=7, enemies=10, result=1),
    Case(my_solders=13, casern=7, enemies=10, result=1),
    Case(my_solders=5, casern=7, enemies=10, result=-1),
    Case(my_solders=1, casern=1, enemies=1, result=1),
    Case(my_solders=25, casern=200, enemies=10, result=13),
    Case(my_solders=250, casern=500, enemies=187, result=4),
    Case(my_solders=250, casern=500, enemies=234, result=10),
    Case(my_solders=250, casern=500, enemies=209, result=6),
    Case(my_solders=31, casern=495, enemies=15, result=30),
    Case(my_solders=250, casern=500, enemies=240, result=13),
    Case(my_solders=499, casern=500, enemies=499, result=3),
    Case(my_solders=14, casern=471, enemies=9, result=92),
    Case(my_solders=2, casern=3, enemies=2, result=3),
    Case(my_solders=5, casern=8, enemies=5, result=4),
    Case(my_solders=3, casern=1, enemies=1, result=1),
    Case(my_solders=300, casern=301, enemies=484, result=6),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_destroy(t: Case) -> None:
    result = destroy(t.my_solders, t.casern, t.enemies)
    assert result == t.result
