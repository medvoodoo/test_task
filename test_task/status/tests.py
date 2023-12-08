import json
from datetime import date
import subprocess
from django.test import TestCase, Client

# Create your tests here.


class SettingTest(TestCase):

    def test_details(self):

        c = Client()
        response = c.get(
        "/status",
        headers={"accept": "application/json"},
        )
        try:
            o = subprocess.run(['uname', '-a'], capture_output=True, text=True)
            message = o.stdout.strip()
        
        except:
            message = subprocess.check_output("uname -a", shell=True)
        result = {
            'host': message.strip(),
            'date': str(date.today()),
            'status': 'Ok'
        }
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.content.decode('UTF-8'),json.dumps(result))
