.. image:: https://img.shields.io/badge/License-MIT-green.svg
    :alt: domain-reputation-py license
    :target: https://opensource.org/licenses/MIT

.. image:: https://img.shields.io/pypi/v/domain-reputation.svg
    :alt: domain-reputation-py release
    :target: https://pypi.org/project/domain-reputation

.. image:: https://github.com/whois-api-llc/domain-reputation-py/workflows/Build/badge.svg
    :alt: domain-reputation-py build
    :target: https://github.com/whois-api-llc/domain-reputation-py/actions

========
Overview
========

The client library for
`Domain Reputation API <https://domain-reputation.whoisxmlapi.com/api>`_
in Python language.

The minimum Python version is 3.6.

Installation
============

.. code-block:: shell

    pip install domain-reputation

Examples
========

Full API documentation available `here <https://domain-reputation.whoisxmlapi.com/api/documentation/making-requests>`_

Create a new client
-------------------

.. code-block:: python

    from domainreputation import *

    client = Client('Your API key')

Make basic requests
-------------------

.. code-block:: python

    # Get DNS records for a domain name.
    response = client.get('youtube.com')
    print(response)

    # Get raw API response in XML format
    raw_result = client.get_raw('bbc.com',
        output_format=Client.XML_FORMAT)

Advanced usage
-------------------

Extra request parameters

.. code-block:: python

    result = client.get(
        'samsung.com',
        Client.MODE_FULL)

Response model overview
-----------------------

.. code-block:: python

    Response:
        - mode: str
        - reputation_score: float
        - test_results: [TestResult]
            - test: str
            - test_code: int
            - warnings: [str]
            - warning_codes: [int]


Sample response
---------------

.. code-block:: python

  {
  'mode': 'full',
  'reputation_score': 81.16,
  'test_results':
    [
        {
            "test": "Name servers configuration meets best practices",
            "testCode": 76,
            "warnings": [
                "Some name servers are located on a single ASN: \
                 ns44.domaincontrol.com - AS44273, ns43.domaincontrol.com - AS44273"
            ],
            "warningCodes": [
                1013
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
  }

