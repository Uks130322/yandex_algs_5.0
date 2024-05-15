import dataclasses
import pytest

from task_A import playlists


##################
# TEST FOR TASK A
##################


@dataclasses.dataclass
class Case:
    songs: list[set[str]]
    result: list[str]

    def __str__(self) -> str:
        return f"playlists_{self.songs}"


TEST_CASES = [
    Case(songs=[{'Love', 'Life'}, {'Life', 'GoodDay'}], result=['Life'])
    ]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_playlists(t: Case) -> None:
    result = playlists(t.songs)
    assert result == t.result
