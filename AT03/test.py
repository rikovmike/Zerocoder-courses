from main import get_random_cat_image

def test_successful_cat_image(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/mockcat.jpg"}]

    mocker.patch("main.requests.get", return_value=mock_response)

    result = get_random_cat_image()
    assert result == "https://cdn2.thecatapi.com/images/mockcat.jpg"

def test_failed_cat_image_status_code(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {}

    mocker.patch("main.requests.get", return_value=mock_response)

    result = get_random_cat_image()
    assert result is None

def test_exception_handling(mocker):
    mocker.patch("main.requests.get", side_effect=Exception("Network error"))

    result = get_random_cat_image()
    assert result is None