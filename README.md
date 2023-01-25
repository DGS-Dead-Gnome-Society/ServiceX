# ServiceX
A pseudo-services bot wrote in Python 3 for the DGS IRC network. We had a Limnoria bot called X which was hosting channel statistics and a polling system however there were a few hardcoded things I didn't like about Limnoria so I decided to re-invent the wheel.

## How will ServiceX work?
At current, I have multiple models on how ServicesX should be coded.

## Features
* [ ] Configurability (Either TOML or JSON)
* [ ] Ensured compatibility with `UnrealIRCd specifics`
* [ ] SASL authentication (Ability to authentication via SASL upon connect)
* [ ] Virtual IRC operator (Ability to authenticate as an oper)
* [ ] Automatically join all channels in the `#DGS-* namespace` (Configurable)
* [ ] Command interpreter (Commands sent to ServiceX in channels and via PM)
* [ ] Module engine
* [ ] Verification of users based on the NickServ account username shown in their WHOIS
* [ ] Polling System (Democracy)
* [ ] Channel Statistics
