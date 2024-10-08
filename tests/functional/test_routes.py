from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country':'Lebanon'})
    assert response.status_code == 200


def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<account_id>' endpoint is posted to (PUT) to update an account
    THEN check that the response is valid and the account details are updated
    """
    # First, create an account to update
    response = testing_client.post('/accounts', json={'name': 'Jane Doe', 'currency': '$', 'country': 'Lebanon'})
    assert response.status_code == 200
    
    # Extract the account ID from the response (assuming the response contains the account's ID)
    account_id = response.json.get('id')

    # Now, update the account details
    update_response = testing_client.put(f'/accounts/{account_id}', json={'name': 'Jane Smith', 'currency': '$', 'country': 'Lebanon'})
    
    # Check the update was successful
    assert update_response.status_code == 200
    assert update_response.json['name'] == 'Jane Smith'
    
    
def test_create_account_and_verify_content(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check that the response is valid and contains the correct account details
    """
    # Create an account
    response = testing_client.post('/accounts', json={
        'name': 'Charlie Brown',
        'currency': '$',
        'country': 'USA'
    })
    
    # Ensure account creation was successful
    assert response.status_code == 200
    
    # Verify the response contains the expected data
    response_data = response.get_json()
    assert response_data['name'] == 'Charlie Brown'
    assert response_data['currency'] == '$'
    assert response_data['country'] == 'USA'


