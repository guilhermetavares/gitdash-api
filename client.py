import requests
import os


class GithubClient(object):
    BASE_URL = 'https://api.github.com/'
    HEADERS = {
        'Accept': 'github.v3; format=json',
        'content-type': 'application/json',
        'Authorization': 'token {}'.format(os.environ['GITHUBKEY']),
    }

    def _get(self, url):
        return requests.get(
            url,
            headers=self.HEADERS,
        ).json()

    def pulls(self, org, project):
        url = '{}repos/{}/{}/pulls'.format(self.BASE_URL, org, project)
        data = self._get(url)

        if 'message' in data:
            return data

        for item in data:
            print(item)
            statuses_url = item.get('statuses_url')
            item.update({
                'statuses': self._get(statuses_url),
            })

        return data
