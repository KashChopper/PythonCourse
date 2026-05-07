"""
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
"""

message = "Hey everyone! Do you want to make a lot of money from home with zero effort? Don't wait—buy now to get our exclusive guide. You should also subscribe this channel for more daily secrets. Just click this link to get started immediately!"

spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

if spam1 in message or spam2 in message or spam3 in message or spam4 in message:
    print("This is a spam message")
else:
    print("This is not a spam message")
