import json
import unittest
from json import loads
from domainreputation import Response, ErrorMessage

_json_response_ok = '''{
    "mode": "full",
    "reputationScore": 91.16,
    "testResults": [
        {
            "test": "Name servers configuration meets best practices",
            "testCode": 76,
            "warnings": [
                "Some name servers are located on a single ASN"
            ],
            "warningCodes": [
                1013
            ]
        },
        {
            "test": "SOA record configuration check",
            "testCode": 84,
            "warnings": [
                "The retry interval is 7200. Recommended range is [600 .. 3600]",
                "The expire interval is 604800. Recommended range is [1209600 .. 2419200]"
            ],
            "warningCodes": [
                1019,
                1024
            ]
        },
        {
            "test": "Mail servers configuration check",
            "testCode": 80,
            "warnings": [
                "AAAA records not configured for mail servers",
                "SPF record not configured",
                "DMARC is not configured"
            ],
            "warningCodes": [
                5007,
                5015,
                5016
            ]
        },
        {
            "test": "Malware databases check",
            "testCode": 82,
            "warnings": [
                "Status: dangerous"
            ],
            "warningCodes": [
                4001
            ]
        },
        {
            "test": "SSL Certificate configuration",
            "testCode": 89,
            "warnings": [
                "No SSL certificates found"
            ],
            "warningCodes": [
                6023
            ]
        }
    ]
}'''

_json_response_error = '''{
    "code": 403,
    "messages": "Access restricted. Check credits balance or enter the correct API key."
}'''


class TestModel(unittest.TestCase):

    def test_response_parsing(self):
        response = loads(_json_response_ok)
        parsed = Response(response)
        self.assertEqual(parsed.mode, response['mode'])
        self.assertEqual(parsed.reputation_score, response['reputationScore'])
        self.assertIsInstance(parsed.test_results, list)
        self.assertEqual(parsed.test_results[0].test, response['testResults'][0]['test'])
        self.assertEqual(parsed.test_results[1].test_code, response['testResults'][1]['testCode'])

        self.assertIsInstance(parsed.test_results[2].warnings, list)
        self.assertListEqual(parsed.test_results[2].warnings, response['testResults'][2]['warnings'])

        self.assertIsInstance(parsed.test_results[2].warning_codes, list)
        self.assertListEqual(parsed.test_results[2].warning_codes, response['testResults'][2]['warningCodes'])

    def test_error_parsing(self):
        error = loads(_json_response_error)
        parsed_error = ErrorMessage(error)
        self.assertEqual(parsed_error.code, error['code'])
        self.assertEqual(parsed_error.message, error['messages'])

    def test_comparing_two_models(self):
        model1 = Response(json.loads(_json_response_ok))
        model2 = Response(json.loads(_json_response_ok))
        self.assertEqual(model1, model2)
