# whatools-python
Python library for integrating Whatools into your app easily.

Notice
This library works only with v3 API. Please make sure your whatools line is configured to use such API version.
Create an account on wha.tools and add a number, you will be assigned an API access key.


API reference

Setting up

The only thing you need is including this library and then create an API object by passing 
your whatools API key as a parameter to the class constructor.

| import whatools
| wa = whatools.Whatools("Replace with API access key")

Remember that you can get the API key for your whatools line by logging into Whatools and then going to Advanced settings > REST API

Logging in and out

Logging in and out is the analog process in v3 API to subscribing and unsubscribing in older API versions.
 Nevertheless, in v3, when you log out you are effectively closing the connection between
WhatsApp servers and your account, so you can be sure you never miss a single message.

| wa.login()
| wa.logout()

Setting your nickname

| wa.setNickname("Your nickname")

Getting your nickname

| wa.getNickname()

Setting your status message

| wa.setStatusMessage("Replace with preferred status message")

Setting your ava

