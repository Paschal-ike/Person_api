import requests

def test_create_person():
    response = requests.post('http://localhost:8000/api/', json={'name': 'Joanthan Brew'})
    assert response.status_code == 201

def test_get_person():
    response = requests.get('http://localhost:8000/api/1')
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'Elon Musk'}

def test_update_person():
    response = requests.put('http://localhost:8000/api/1', json={'name': 'Samanthan Brew'})
    assert response.status_code == 200

def test_delete_person():
    response = requests.delete('http://localhost:8000/api/1')
    assert response.status_code == 204

if __name__ == '__main__':
    test_create_person()
    test_get_person()
    test_update_person()
    test_delete_person()