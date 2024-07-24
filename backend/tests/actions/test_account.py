from actions.account import get_full_watchlist


def test_get_full_watchlist(mocker):
    mock_get_tmbd_watchlist = mocker.patch("actions.account.get_watchlist_movies")

    def get_tmbd_watchlist(_, page):
        total_results = [{"id": n} for n in range(30)]
        start_index = (page - 1) * 20
        end_index = start_index + 20
        return {
            "results": total_results[start_index:end_index],
            "total_pages": 2 if len(total_results) > 20 else 1,
        }

    mock_get_tmbd_watchlist.side_effect = get_tmbd_watchlist
    result = get_full_watchlist(123)
    expected_result = [{"id": n} for n in range(30)]
    assert result == expected_result
