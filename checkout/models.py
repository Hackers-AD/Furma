from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''


The checkout process comprises the following steps:

    Gateway - Anonymous users are offered the choice of logging in, registering, or checking out anonymously. Signed in users will be automatically redirected to the next step.

    Shipping address - Enter or choose a shipping address.

    Shipping method - Choose a shipping method. If only one shipping method is available then it is automatically chosen and the user is redirected onto the next step.

    Payment method - Choose the method of payment plus any allocations if payment is to be split across multiple sources. If only one method is available, then the user is redirected onto the next step.

    Preview - The prospective order can be previewed.

    Payment details - If any sensitive payment details are required (e.g., bankcard number), then a form is presented within this step. This has to be the last step before submission so that sensitive details don’t have to be stored in the session.

    Submission - The order is placed.

    Thank you - A summary of the order with any relevant tracking information.
'''