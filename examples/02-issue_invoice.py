# -*- encoding: utf-8 -*-

import sys
import uuid
import logging

from pprint import pformat
from braspag.core import BraspagRequest

if len(sys.argv) > 1:
    MERCHANT_ID = sys.argv[1]
else:
    MERCHANT_ID = u'12345678-1234-1234-1234-1234567890AB'

logging.root.setLevel(logging.INFO)

# Create request object
request = BraspagRequest(merchant_id=MERCHANT_ID, homologation=True)

response = request.issue_invoice(
    order_id=uuid.uuid4(),
    customer_id=u'12345678900',
    customer_name=u'José da Silva',
    customer_email='jose123@dasilva.com.br',
    amount=10000,
)
logging.info(pformat(response.__dict__))
