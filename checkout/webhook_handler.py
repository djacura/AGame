from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    def __init__(self):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown or unexpected webhook
        """
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)

