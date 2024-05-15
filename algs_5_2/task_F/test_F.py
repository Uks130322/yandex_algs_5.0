import dataclasses
import pytest

from task_F import spin_to_win


##################
# TEST FOR TASK F
##################


@dataclasses.dataclass
class Case:
    sectors: int
    sector_list: list[int]
    min_v: int
    max_v: int
    slow_down: int
    result: int

    def __str__(self) -> str:
        return f"spin_to_win_{self.sector_list}, {self.min_v}, {self.max_v}, {self.slow_down}"


TEST_CASES = [
    Case(sectors=5, sector_list=[1, 2, 3, 4, 5], min_v=3, max_v=5, slow_down=2, result=5),
    Case(sectors=5, sector_list=[1, 2, 3, 4, 5], min_v=15, max_v=15, slow_down=2, result=4),
    Case(sectors=5, sector_list=[5, 4, 3, 2, 1], min_v=2, max_v=5, slow_down=2, result=5),
    Case(sectors=4, sector_list=[744, 43, 468, 382], min_v=20, max_v=48, slow_down=12, result=468),
    Case(sectors=4, sector_list=[208, 794, 866, 717], min_v=258_262_581, max_v=998_614_008, slow_down=740_351_427,
         result=794)

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_spin_to_win(t: Case) -> None:
    result = spin_to_win(t.sectors, t.sector_list, t.min_v, t.max_v, t.slow_down)
    assert result == t.result
