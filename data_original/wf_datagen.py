import requests

class Data_generator:
    auth_url = 'https://www.strava.com/oauth/token'
    activities_url = 'https://www.strava.com/api/v3/athlete/activities'
    access_token = None
    full_dataset = []

    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def get_headers(self):
        return {
            'Authorization': 'Bearer ' + self.access_token
        }
    
    def get_params(self, page):
        return {
            'per_page': 200,
            'page': page
        }

    def fetch_activities(self):
        activities = []
        page = 1

        while True:
            cur_page = requests.get(self.activities_url, 
                                    headers=self.get_headers(), 
                                    params=self.get_params(page)).json()
            if (len(cur_page) == 0):
                break
            page += 1
            activities.extend(cur_page)

        return activities

    def generate_data(self):
        activities = self.fetch_activities()
        self.full_dataset.extend(activities)

    def get_full_dataset(self):
        return self.full_dataset
    
    def export_csv(self):
        pass
    
if __name__ == '__main__':
    data_generator = Data_generator(input('pls enter access_token: '))
    data_generator.generate_data()
    dataset = data_generator.get_full_dataset()
    print(dataset[0])
