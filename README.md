# ICE detainers in Travis County

![ice ice baby](https://media.giphy.com/media/j0A3pPBp0NAXe/giphy.gif)

(not even sorry)

This repo contains a Jupyter notebook with scripts to process and analyze ICE detainer data in Travis County, Texas, from the mid-2000s to October 2016.

### Requirements
* python
* virtualenv/virtualenvwrapper

### Setup
Clone or DL this repo, then:
```shell
$ cd ice-travis-county
$ mkvirtualenv ice-data
$ pip install -r requirements.txt
$ jupyter notebook ice-data-parser.ipynb
```

### Assumptions and issues
Some of the booking dates go back to the mid-90s, which is interesting, because ICE wasn't formed until 2003 or so. According to XXXX, data before XXX is unreliable, so records on or before XXXXX are excluded from this analysis.

For the purposes of tallying detainees' self-reported countries of origin, we classified the Federated States of Micronesia (a U.S. "associated state" with its own U.N. representative) as its own country. Others we grouped with a "parent" country:
* British Indian Ocean Territory (United Kingdom)
* French Southern and Antartic [_sic_] Lands (France)
* Guadeloupe (France)
* Guam (United States)
* Hong Kong (China)
* Howland Island (United States)
* Juan de Nova Island (France)
* Northern Mariana Islands (United States)
* Puerto Rico (United States)
* Tokelau (New Zealand)
* Virgin Islands (United States)

(If any of these assumptions are unwarranted, please let us know.)