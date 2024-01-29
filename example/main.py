# Require dependencies
from nicolasflamel.mwc_pay import MwcPay


# Initialize MWC Pay
mwcPay = MwcPay()

# Display message
print("Creating payment")

# Create payment
payment = mwcPay.createPayment("123.456", 5, 600, "http://example.com/completed", "http://example.com/received", "http://example.com/confirmed", "http://example.com/expired")

# Check if creating payment failed due to invalid parameters
if payment is None:

	# Display error
	print("Invalid parameters")
	
# Otherwise check if creating payment failed due to a server error
elif payment is False:

	# Display error
	print("Server error")
	
# Otherwise
else:

	# Display payment's payment ID, URL, and recipient payment proof address
	print(f"Payment ID: {payment['payment_id']}")
	print(f"URL: {payment['url']}")
	print(f"Recipient payment proof address: {payment['recipient_payment_proof_address']}")
	
	# Display message
	print("Getting payment info")
	
	# Get payment info
	paymentInfo = mwcPay.getPaymentInfo(payment["payment_id"])
	
	# Check if getting payment info failed due to invalid parameters
	if paymentInfo is None:

		# Display error
		print("Invalid parameters")
		
	# Otherwise check if getting payment info failed due to a server error
	elif paymentInfo is False:

		# Display error
		print("Server error")
		
	# Otherwise
	else:
	
		# Display payment info's URL, price, required confirmations, received, confirmations, time remaining, status, and recipient payment proof address
		print(f"URL: {paymentInfo['url']}")
		print("Price: {}".format("N/A" if paymentInfo["price"] is None else paymentInfo["price"]))
		print(f"Required confirmations: {paymentInfo['required_confirmations']}")
		print("Received: {}".format("true" if paymentInfo["received"] is True else "false"))
		print(f"Confirmations: {paymentInfo['confirmations']}")
		print("Time remaining: {}".format("N/A" if paymentInfo["time_remaining"] is None else paymentInfo["time_remaining"]))
		print(f"Status: {paymentInfo['status']}")
		print(f"Recipient payment proof address: {paymentInfo['recipient_payment_proof_address']}")
		
		# Display message
		print("Getting price")

		# Get price
		price = mwcPay.getPrice()

		# Check if getting price failed due to invalid parameters
		if price is None:

			# Display error
			print("Invalid parameters")
			
		# Otherwise check if getting price failed due to a server error
		elif price is False:

			# Display error
			print("Server error")
			
		# Otherwise
		else:

			# Display price
			print(f"Price: {price}")
			
			# Display message
			print("Getting public server info")
			
			# Get public server info
			publicServerInfo = mwcPay.getPublicServerInfo()

			# Check if getting public server info failed due to invalid parameters
			if publicServerInfo is None:

				# Display error
				print("Invalid parameters")
				
			# Otherwise check if getting public server info failed due to a server error
			elif publicServerInfo is False:

				# Display error
				print("Server error")
				
			# Otherwise
			else:

				# Display public server info's URL and Onion Service address
				print(f"URL: {publicServerInfo['url']}")
				print("Onion Service address: {}".format("N/A" if publicServerInfo["onion_service_address"] is None else publicServerInfo["onion_service_address"]))
