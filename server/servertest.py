import requests

class TestSearch():

    def test_search_valid_product(self):
        url = 'https://ivolunteer-app.herokuapp.com/users/login'
        myobj = {"Email": "Gasasa255@gmail.com","Password": "123456"}
        x = requests.post(url, data=myobj)
        assert x.status_code == 500
        assert x.elapsed.total_seconds() < 20



    def test_register(self):
        url = 'https://ivolunteer-app.herokuapp.com/users/register'
        myobj = {"FirstName": "rivka","LastName": "gasasa","Email": "Gasasa255@gmail.com","Password": "123456",
        "Age": "28","ProfilePic": "dad1b51e-fa16-4f21-bdd4-9f027ad7d9bf.jpg"}
        x = requests.post(url, data=myobj)
        assert x.status_code == 500
        assert x.elapsed.total_seconds() < 20





