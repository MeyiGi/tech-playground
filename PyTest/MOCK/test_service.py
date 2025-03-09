import unittest.mock as mock
import service


@mock.patch("service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked MeyiGi"
    username = service.get_user_from_db(2)
    
    assert username == "Mocked MeyiGi"
    
    
    
@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id" : 1, "name" : "MeyiGi"}
    mock_get.return_value = mock_response
    
    data = service.get_users()
    
    assert data == {"id" : 1, "name" : "MeyiGi"}