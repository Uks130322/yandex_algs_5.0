import dataclasses
import pytest

from task_H import fury_of_the_elves


##################
# TEST FOR TASK H
##################


@dataclasses.dataclass
class Case:
    race: int
    classes: int
    race_class: list[list[int]]
    result: tuple[int]

    def __str__(self) -> str:
        return f"fury_of_the_elves_{self.race}, {self.classes}, {self.race_class}"


TEST_CASES = [
    Case(race=2, classes=2, race_class=[[1, 2], [3, 4]], result=(2, 2)),
    Case(race=3, classes=4, race_class=[[1, 3, 5, 7], [9, 11, 2, 4], [6, 8, 10, 12]], result=(3, 2)),
    Case(race=3, classes=3, race_class=[[1, 2, 1], [2, 1, 1], [2, 1, 1]], result=(1, 1)),
    Case(race=4, classes=5, race_class=[[999999997, 1, 2, 3, 4], [10, 2, 1000000000, 1, 7],
                                        [3, 9, 999999999, 5, 10], [1, 7, 3, 999999998, 6]], result=(4, 3)),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_fury_of_the_elves(t: Case) -> None:
    result = fury_of_the_elves(t.race, t.classes, t.race_class)
    assert result == t.result
