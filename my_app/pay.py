from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from paystackapi.verification import Verification

paystack_secret_key = "sk_test_a18b4a0dcad6d60a03b5be78a47e14f8d28686ce"
paystack_public_key = "pk_test_80c9e3e62c12dca2e7a51baaccf342279ffa8f1a" 
paystack = Paystack(secret_key=paystack_secret_key)

paramz = '9sxzb9weo8'
details = Transaction.verify(reference=paramz)
status = details['data']['status']

print(details)
print(status)