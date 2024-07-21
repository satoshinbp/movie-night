from actions.account import get_watchlist


def test_get_watchlist(mocker):
    mock_get_tmbd_watchlist = mocker.patch("actions.account.get_tmbd_watchlist")
    mock_get_tmbd_regions = mocker.patch("actions.account.get_tmbd_regions")
    mock_get_tmbd_provider = mocker.patch("actions.account.get_tmbd_provider")
    mock_get_tmbd_runtime = mocker.patch("actions.account.get_tmbd_runtime")

    mock_get_tmbd_watchlist.return_value = [{"id": 1}, {"id": 2}, {"id": 3}]
    mock_get_tmbd_regions.return_value = [
        {"iso_3166_1": "US"},
        {"iso_3166_1": "CA"},
        {"iso_3166_1": "UK"},
    ]
    mock_get_tmbd_provider.side_effect = lambda movie_id: {
        1: {"US": {"flatrate": [{"provider_name": "Netflix"}]}},
        2: {"CA": {"flatrate": [{"provider_name": "Netflix"}]}},
        3: {"UK": {"flatrate": [{"provider_name": "Amazon Prime Video"}]}},
    }[movie_id]
    mock_get_tmbd_runtime.side_effect = lambda movie_id: {1: 120, 2: 90, 3: 105}[
        movie_id
    ]

    result = get_watchlist(123)

    expected_result = [
        {"id": 1, "netflix_regions": ["US"], "runtime": 120},
        {"id": 2, "netflix_regions": ["CA"], "runtime": 90},
        {"id": 3, "netflix_regions": [], "runtime": 105},
    ]

    assert result == expected_result
