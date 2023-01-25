# ServiceX
A pseudo-services bot wrote in Python 3 for the DGS IRC network. We had a Limnoria bot called X which was hosting channel statistics and a polling system however there were a few hardcoded things I didn't like about Limnoria so I decided to re-invent the wheel.

## How will ServiceX work?
At current, I have multiple models on how ServicesX should be coded.

## Features
* Channel Statistics
* Polling System (Democracy)
* Virtual IRC operator
* Ensured compatibility with `UnrealIRCd specifics`
* Verification of users based on the NickServ account username shown in their WHOIS
* Automatically join all channels in the `#DGS-* namespace` (Configurable)
