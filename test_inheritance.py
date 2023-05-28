class PaypalPayment:
    payment_approved = True

    def is_approved(self):
        return self.payment_approved

class StripePayment:
    payment_approved = False

    def is_approved(self):
        return self.payment_approved

class PaymentVerification(StripePayment, PaypalPayment):
    pass

payment = PaymentVerification()
print(payment.is_approved())
