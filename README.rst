===============================
PayPal IPN notification example
===============================

Overview
========

Simple flask application with a
landing page that has a buy now
button.

When a purchase is made,
IPN notification is sent and
processed.

If notification is verified,
take action.

Notes
=====

- Set a custom value in the IPN message by setting the hidden form field `custom`
- Set the IPN notification URL in the PayPal button editor (can override in form as `notify_url`)

Reference links
===============

Use developer portal to create sandbox accounts:
https://developer.paypal.com/docs/classic/lifecycle/ug_sandbox/?mark=sandbox

Use Sandbox website for performing tests:
https://www.sandbox.paypal.com/us/home

Saved button page (sandbox):
https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_button-management

Production website:
https://www.paypal.com/us/home

Live stream writing this code:
https://www.youtube.com/watch?v=NFUdd3gveN8

Source:
https://github.com/DevDungeon/PayPalFlaskIPN