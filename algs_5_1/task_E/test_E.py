import dataclasses
import pytest

from task_E import startup


##################
# TEST FOR TASK E
##################


@dataclasses.dataclass
class Case:
    profit: str
    founders: str
    days: str
    result: int

    def __str__(self) -> str:
        return f"startup_{self.profit}_{self.founders}_{self.days}"


TEST_CASES = [
    Case(profit='21', founders='108', days='1', result='216'),
    Case(profit='23', founders='1080', days='1', result='-1'),
    Case(profit='5', founders='12', days='4', result='-1'),
    Case(profit='36', founders='23', days='5', result='3680000'),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_startup(t: Case) -> None:
    result = startup(t.profit, t.founders, t.days)
    assert result == t.result
