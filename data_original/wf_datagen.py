import requests
import pandas
import time

class Data_generator:
    auth_url = 'https://www.strava.com/oauth/token'
    activities_url = 'https://www.strava.com/api/v3/athlete/activities'
    access_token = None

    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def get_headers(self):
        return {
            'Authorization': 'Bearer ' + self.access_token
        }
    
    def get_params(self, per_page, page):
        return {
            'per_page': per_page,
            'page': page
        }
    
    # This probably can be made better in terms of security,
    # but considering libraries allowed, it might be the simplest feasible solution
    def get_zones_url(self, id):
        return f'https://www.strava.com/api/v3/activities/{id}/zones'

    def fetch_activities(self):
        activities = []
        page = 1
        print(f'Fetching activities from {self.activities_url}')

        while True:
            cur_page = requests.get(self.activities_url, 
                                    headers=self.get_headers(), 
                                    params=self.get_params(200, page)).json()
            if (len(cur_page) == 0):
                break
            print(f'Fetched activities [{(page-1) * 200 + 1},{(page-1) * 200 + len(cur_page)}]')
            page += 1
            activities.extend(cur_page)

        return activities

    def fetch_zones_by_activity(self, activities):
        zones = []
        print(f'Fetching zones for all activities')

        for activity in activities:
            id = activity['id']
            cur_zone = requests.get(self.get_zones_url(id),
                                    headers=self.get_headers()).json()
            cur_zone.append({'id': id})
            print(f'Fetched zones for activity {id}')
            zones.append(cur_zone)

            # The APIs are rate limited to 200 per 15 mins and 2000 per day
            # if loop is put on sleep for 5 seconds, 200 requests will take > 1000 seconds
            # 1000 sec = 16.67 mins, this will take care of 15 min rate limiting
            # At the time of pulling data, I have 1601 records, so it won't cross 2000 per day
            time.sleep(5)

        return zones

    def generate_data(self):
        activities = self.fetch_activities()
        self.export_csv(data=activities, csv_filename='strava_activities.csv')
        zones = self.fetch_zones_by_activity(activities)
        self.export_csv(data=zones, csv_filename='strava_zones_per_activity.csv')
        
    def export_csv(self, data, csv_filename):
        df = pandas.DataFrame(data)
        df.to_csv(csv_filename)
        print(f'Exported dataset to {csv_filename}')
    
if __name__ == '__main__':
    '''
    https://developers.strava.com/docs/authentication/

    To get access_token I had to do the following steps:

    1. Register an app on Strava
    2. Open this link on browser -> http://strava.com/oauth/authorize?client_id=113526&redirect_uri=http://localhost&response_type=code&scope=activity:read_all
    (Above link takes in my client_id and scope and redirects to another page after authentication and authorization with a code in the url)
    (The url looks like this -> http://localhost/?state=&code=f3ffd8d4857815e7f45a1066b56b9bd5fad89211&scope=read,activity:read_all)
    3. The code from url is now used to get the access_token by sending a post request
    (POST https://www.strava.com/oauth/token?client_id=113526&client_secret={{CLIENT_SECRET}}&code={{Strava_post_auth_code}}&grant_type=authorization_code)
    (CLIENT_SECRET is found in the registered Strava app and Strava_post_auth_code is the code from previous redirect url)
    4. This returns access_token and refresh_token. The access_token is being input in this app, which is used as bearer token header for all API calls

    NOTE: The above steps are not automated yet because it requires a web application since authentication page is loaded on browser as well as the redirects.
    However, at a later stage if I make a web app, this can be automated and generalized for any Strava user.
    '''
    data_generator = Data_generator(input('pls enter access_token: '))
    print('--------------------------------------------------------------------------')
    data_generator.generate_data()
    print('--------------------------------------------------------------------------')