# MWC Pay Python SDK

### Description
Python SDK for [MWC Pay](https://github.com/NicolasFlamel1/MWC-Pay).

### Installing
Run the following command to install this library.
```
pip install nicolasflamel.mwc-pay
```

### Usage
After an `MwcPay` object has been created, it can be used to create payments, query the status of payments, get the current price of MimbleWimble coin, and get info about MWC Pay's public server.

A high level overview of a payment's life cycle when using this SDK consists of the following steps:
1. The merchant creates a payment and gets the payment's URL from the response.
2. The buyer sends MimbleWimble Coin to that URL.
3. The merchant can optionally monitor the payment's status via the `getPaymentInfo` method, the `createPayment` method's `received_callback` parameter, the `createPayment` method's `confirmed_callback` parameter, and/or the `createPayment` method's `expired_callback` parameter.
4. The payment's completed callback is ran once the payment achieves the desired number of on-chain confirmations.

The following code briefly shows how to use this SDK. A more complete example with error checking is available [here](https://github.com/NicolasFlamel1/MWC-Pay-Python-SDK/tree/master/example).
```
# Require dependencies
from nicolasflamel.mwc_pay import MwcPay

# Initialize MWC Pay
mwcPay = MwcPay("http://localhost:9010")

# Create payment
payment = mwcPay.createPayment("123.456", 5, 600, "http://example.com/completed", "http://example.com/received", "http://example.com/confirmed", "http://example.com/expired")

# Get payment info
paymentInfo = mwcPay.getPaymentInfo(payment["payment_id"])

# Get price
price = mwcPay.getPrice()

# Get public server info
publicServerInfo = mwcPay.getPublicServerInfo()
```
