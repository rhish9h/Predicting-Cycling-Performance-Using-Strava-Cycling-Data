import requests
import pandas as pd
import time

class Data_generator:
    auth_url = 'https://www.strava.com/oauth/token'
    access_token = None
    activities_filepath = 'strava_activities.csv'

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
    def get_power_stream_url(self, activity_id):
        return f'https://www.strava.com/api/v3/activities/{activity_id}/streams?keys=watts&key_by_type=true&series_type=time'

    def load_activities(self):
        return pd.read_csv(self.activities_filepath)

    def fetch_power_stream_by_activity(self, activities):
        power_streams = []
        print(f'Fetching power streams for all activities')

        for _, activity in activities.iterrows():
            id = activity['id']
            cur_power_stream = requests.get(self.get_power_stream_url(id),
                                    headers=self.get_headers()).json()
            cur_power_stream['id'] = id
            print(f'Fetched power streams for activity {id}')
            power_streams.append(cur_power_stream)

            # The APIs are rate limited to 200 per 15 mins and 2000 per day
            # if loop is put on sleep for 5 seconds, 200 requests will take > 1000 seconds
            # 1000 sec = 16.67 mins, this will take care of 15 min rate limiting
            # At the time of pulling data, I have 1601 records, so it won't cross 2000 per day
            time.sleep(5)

        return power_streams

    def generate_data(self):
        activities = self.load_activities()
        power_streams = self.fetch_power_stream_by_activity(activities)
        self.export_csv(data=power_streams, csv_filename='strava_power_streams_per_activity.csv')
        
    def export_csv(self, data, csv_filename):
        df = pd.DataFrame(data)
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