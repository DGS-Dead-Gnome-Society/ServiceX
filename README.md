# ServiceX
A pseudo-services bot wrote in Python 3 for the DGS IRC network. We had a Limnoria bot called X which was hosting channel statistics and a polling system however there were a few hardcoded things I didn't like about Limnoria so I decided to re-invent the wheel.

## How will ServiceX work?
At current, I have multiple models on how ServicesX should be coded.

## Features
The features listed below are prioritised based on difficulity and importance.
* [ ] SASL authentication (Ability to authentication via SASL upon connect)
* [ ] Virtual IRC operator (Ability to authenticate as an oper)
* [ ] Command interpreter (Commands sent to ServiceX in channels and via PM)
* [ ] Channel Statistics
* Polling System (Democracy)
* Ensured compatibility with `UnrealIRCd specifics`
* Verification of users based on the NickServ account username shown in their WHOIS
* Automatically join all channels in the `#DGS-* namespace` (Configurable)
* Module engine
