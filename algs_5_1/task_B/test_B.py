import dataclasses
import pytest

from task_B import football_comment


##################
# TEST FOR TASK b
##################


@dataclasses.dataclass
class Case:
    first_game: str
    second_game: str
    first_field: str
    result: str

    def __str__(self) -> str:
        return f"football_comment_{self.first_game}_{self.second_game}_{self.first_field}"


TEST_CASES = [
    Case(first_game='0:0', second_game='0:0', first_field='1', result='1'),
    Case(first_game='0:2', second_game='0:3', first_field='1', result='5'),
    Case(first_game='0:2', second_game='0:3', first_field='2', result='6'),
    Case(first_game='1:0', second_game='0:1', first_field='1', result='1'),
    Case(first_game='2:2', second_game='3:0', first_field='2', result='0'),
    Case(first_game='2:3', second_game='5:4', first_field='2', result='1'),
    Case(first_game='2:4', second_game='3:3', first_field='1', result='2'),
    Case(first_game='1:4', second_game='5:1', first_field='1', result='0'),
    Case(first_game='2:4', second_game='3:0', first_field='2', result='0'),
    Case(first_game='2:3', second_game='2:3', first_field='2', result='3'),
    Case(first_game='2:2', second_game='1:1', first_field='1', result='1'),
    Case(first_game='2:2', second_game='1:1', first_field='2', result='0'),
    Case(first_game='2:2', second_game='0:1', first_field='1', result='2')
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_football_comment(t: Case) -> None:
    result = football_comment(t.first_game, t.second_game, t.first_field)
    assert result == t.result
