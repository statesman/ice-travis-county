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

### Assumptions and data issues

#### Pre-ICE data excluded
Some of the booking dates go back to the mid-90s, which is weird because ICE wasn't formed until 2003 or so. According to XXXX, data before XXX is unreliable, so records on or before XXXXX are excluded from this analysis.

#### Grouping by country
For the purposes of tallying detainees' self-reported countries of origin, we classified the Federated States of Micronesia (a U.S. "associated state" with its own U.N. representative) as its own country. Others we grouped with its "parent" country:
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

#### What is a "violent crime"?
We classified 61 of the XXXXXX charges present in the data as "violent crime":
* ASSAULT AGAINST PUB SERVANT (F1)
* AGG ASSAULT AGAINST SECURITY OFFICER (F1)
* AGG ASSAULT DATE/FAMILY/HOUSE W/WEAPON(F1)
* AGG ASSLT CAUSES SBI
* AGG ASSLT W/DEADLY WEAPON
* AGG KIDNAPPING
* AGG KIDNAPPING BI/SEXUAL ABUSE (F1)
* AGG KIDNAPPING FOR RANSOM/REWARD (F1)
* AGG ROBBERY
* AGG SEXUAL ASSLT
* AGG SEXUAL ASSLT CHILD
* ARSON CAUSING BODILY INJURY/DEATH (F1)
* ASSAULT ON SECURITY OFFICER (F3)
* ASSAULT PUBLIC SERVANT (F3)
* ASSLT CAUSE BODILY INJ FAMILY VIO ENH (F3)
* ASSLT CAUSES BODILY INJ
* ASSLT CAUSES BODILY INJ DATE/FAM/HOUSE (F3
* ASSLT CAUSES BODILY INJ FAMILY MEMBER ENH
* ASSLT CAUSES BODILY INJ:FAMILY MEMBER (MA)
* ASSLT INT/RECK IMPEDE BREATH/CIRC (F2)
* ASSLT PUBLIC SERVANT
* ATTM AGG ROBBERY
* ATTM AGG SEXUAL ASSLT
* ATTM ASSLT CAUSES BODILY INJ
* ATTM INDECENCY W/CHILD SEX/CONTACT
* ATTM INJ CHI/ELDER/DISAB REC BOD INJ
* ATTM SEXUAL ASSLT
* ATTM SEXUAL ASSLT CHILD
* ATTM/AGG ASLT W/DEADLY WEAPON
* ATTM/AGG SEX ASLT CHILD
* ATTM/ASLT PUBLIC SERVANT (FS)
* ATTM/ASLT FV STRANGULATION (FS)
* ATTM/ASSAULT FV ENH (PREV CONV) (FS)
* BURGLARY HABITATION INTEND SEX OFFENSE(F1)
* CAPITAL MURDER
* CAPITAL MURDER BY TERROR THREAT/OTH FEL(FX
* CAPITAL MURDER OF MULTIPLE PERSONS (FX)
* CRIM NEGLIGENT HOMICIDE
* DISORDERLY CONDUCT-FIGHTING
* FAIL STOP RENDER AID INJ/DEATH
* FAIL TO STOP AND RENDER AID INJ/DEATH
* FEL ASSAULT FV ENHANCED (PREV CONV) (F3)
* FEL ASSLT CONTINU VIOLENCE FV 2+W/IN 12MO
* FEL ASSLT FV STRANGULATION (F3)
* INDECENCY W/CHILD SEXUAL CONTACT
* INJ CHI/ELDER/DISAB RECK BOD INJ(FS)
* INJ CHILD/ELDER/DISABLE RECK SBI/MEN
* INJ CHILD/ELDER/DISABLE W/INT BOD(F3
* INJ CHILD/ELDER/DISABLE W/INT SBI/ME
* INJ CHILD/ELDERLY/DISABLED CRIM NEG
* INTOXICATED MANSLAUGHTER W/VEHICLE
* INTOXICATION ASSAULT W/VEHICLE SBI
* INTOXICATION MANSLAUGHTER W/VEHICLE
* KIDNAPPING
* MANSLAUGHTER
* MURDER
* SEX ABUSE OF CHILD CONTINUOUS:VICT <14 (F1
* SEXUAL ASSLT
* SEXUAL ASSLT CHILD
* SOLIC/COMM CAPITAL MURDER
* TAKE WEAPON FROM OFFICER (F3)


