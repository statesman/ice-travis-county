"""
Country records that don't need transformed:
    Albania
    Argentina
    Bangledesh
    Barbados
    Belize
    Bosnia and Herzegovina
    Brazil
    Burma
    Burundi
    Cameroon
    Canada
    Costa Rica
    Dominican Republic
    Ecuador
    Egypt
    El Salvador
    Eritrea
    Ethiopia
    Federated States of Micronesia
    France
    Gabon
    Grenada
    Guatemala
    Honduras
    Hungary
    Iceland
    India
    Indonesia
    Iran
    Iraq
    Ireland
    Ivory Coast
    Jamaica
    Japan
    Jordan
    Kenya
    Mauritania
    Morocco
    Nepal
    Nicaragua
    Niger
    Nigeria
    North Korea
    Other
    Pakistan
    Panama
    Peru
    Philippines
    Romania
    Russia
    Saudi Arabia
    Scotland
    Senegal
    South Korea
    Spain
    Sudan
    Surinam
    Sweden
    Thailand
    Togo
    Tunisia
    Turkey
    Ukraine
    Vanuatu
    Yugoslavia
"""

FELONIES = ('S', 'FS', 'F2', 'F1', 'F3', 'F', 'P', '1', '3', '2', 'FX')

MISDEMEANORS = ('C', 'M*', 'MA', 'A', 'MC', 'MB', 'M', 'B')

COUNTRIES = {
    'Abuascalientes, Mexico': 'Mexico',
    'Africa-Reference Only': 'Africa, unspecified',
    'Alabama': 'United States',
    'Australia (American Samoa for boat RES)': 'Australia',
    'Bahrain/Bahrein': 'Bahrain',
    'Baja California (Northern), Mexico': 'Mexico',
    'British Indian Ocean Territory': 'United Kingdom',
    'California (Not for boat RES)': 'United States',
    'Campeche, Mexico': 'Mexico',
    'Chiapas, Mexico': 'Mexico',
    'Chihuahua, Mexico': 'Mexico',
    'China-Reference only': 'China',
    'Coahuila, Mexico': 'Mexico',
    'Colombia, Republic of': 'Colombia',
    'Congo-Reference only': 'Congo',
    'Cuba, Republic of': 'Cuba',
    'Distrito Federal, Mexico': 'Mexico',
    'Durango, Mexico': 'Mexico',
    'England': 'United Kingdom',
    'Florida': 'United States',
    'Foreign country not listed': 'Other',
    'French Southern and Antartic Lands': 'France',
    'Germany (East and West)': 'Germany',
    'Guadeloupe': 'France',
    'Guam': 'United States',
    'Guanajuato, Mexico': 'Mexico',
    'Guerrero, Mexico': 'Mexico',
    'Hidalgo, Mexico': 'Mexico',
    'Hong Kong': 'China',
    'Howland Island': 'United States',
    'Illinois': 'United States',
    'Indiana': 'U.S.A',
    'Italy, includes Sicily and Sardinia': 'Italy',
    'Jalisco, Mexico': 'Mexico',
    'Juan de Nova Island': 'France',
    'Kansas (not for boat RES-see KA)': 'United States',
    'Kansas-boat RES only': 'United States',
    'Louisiana': 'United States',
    'Maine': 'United States',
    'Maryland': 'United States',
    'Massachusetts (not for boat RES': 'United States',
    'Mexico (State)': 'Mexico',
    'Mexico (Use only when state is unknown)': 'Mexico',
    'Michigan-not for boat RES (boat RES 4 MS)': 'United States',
    'Michoacan, Mexico (boat RES for MI)': 'Mexico',
    'Morelos, Mexico': 'Mexico',
    'Nayarit, Mexico': 'Mexico',
    'New Jersey': 'United States',
    'New Mexico': 'United States',
    'New York': 'United States',
    'North Carolina': 'United States',
    'Northern Mariana Islands': 'United States',
    'Nuevo Leon, Mexico': 'Mexico',
    'Oaxaca, Mexico': 'Mexico',
    "People's Republic of China": 'China',
    'Puebla, Mexico': 'Mexico',
    'Puerto Rico': 'United States',
    'Quebec, Canada': 'Canada',
    'Queretaro, Mexico': 'Mexico',
    'San Luis Potosi, Mexico': 'Mexico',
    'Sinaloa, Mexico': 'Mexico',
    'Socialist Republic of Vietname (North VN)': 'Vietnam',
    'Sonora, Mexico': 'Mexico',
    'South Vietnam-Reference Only': 'Vietnam',
    'Tabasco, Mexico': 'Mexico',
    'Taiwan, Republic of China': 'Taiwan',
    'Tamaulipas, Mexico': 'Mexico',
    'Texas': 'United States',
    'Tlaxcala, Mexico': 'Mexico',
    'Tokelau': 'New Zealand',
    'Venezuela, Republic of': 'Venezuela',
    'Veracruz, Mexico': 'Mexico',
    'Vietnam-Reference Only': 'Vietnam',
    'Virgin Islands': 'United States',
    'Wisconsin - not for boat RES': 'United States',
    'Zacatecas, Mexico': 'Mexico',
    'Zambia, Republic of': 'Zambia'
}


VIOLENT_CRIMES = (
    'AGG ASSAULT AGAINST PUB SERVANT (F1)',
    'AGG ASSAULT AGAINST SECURITY OFFICER (F1)',
    'AGG ASSAULT DATE/FAMILY/HOUSE W/WEAPON(F1)',
    'AGG ASSLT CAUSES SBI',
    'AGG ASSLT W/DEADLY WEAPON',
    'AGG KIDNAPPING',
    'AGG KIDNAPPING BI/SEXUAL ABUSE (F1)',
    'AGG KIDNAPPING FOR RANSOM/REWARD (F1)',
    'AGG ROBBERY',
    'AGG SEXUAL ASSLT',
    'AGG SEXUAL ASSLT CHILD',
    'ARSON CAUSING BODILY INJURY/DEATH (F1)',
    'ASSAULT ON SECURITY OFFICER (F3)',
    'ASSAULT PUBLIC SERVANT (F3)',
    'ASSLT CAUSE BODILY INJ FAMILY VIO ENH (F3)',
    'ASSLT CAUSES BODILY INJ',
    'ASSLT CAUSES BODILY INJ DATE/FAM/HOUSE (F3',
    'ASSLT CAUSES BODILY INJ FAMILY MEMBER ENH',
    'ASSLT CAUSES BODILY INJ:FAMILY MEMBER (MA)',
    'ASSLT INT/RECK IMPEDE BREATH/CIRC (F2)',
    'ASSLT PUBLIC SERVANT',
    'ATTM AGG ROBBERY',
    'ATTM AGG SEXUAL ASSLT',
    'ATTM ASSLT CAUSES BODILY INJ',
    'ATTM INDECENCY W/CHILD SEX/CONTACT',
    'ATTM INJ CHI/ELDER/DISAB REC BOD INJ',
    'ATTM SEXUAL ASSLT',
    'ATTM SEXUAL ASSLT CHILD',
    'ATTM/AGG ASLT W/DEADLY WEAPON',
    'ATTM/AGG SEX ASLT CHILD',
    'ATTM/ASLT PUBLIC SERVANT (FS)',
    'ATTM/ASLT FV STRANGULATION (FS)',
    'ATTM/ASSAULT FV ENH (PREV CONV) (FS)',
    'BURGLARY HABITATION INTEND SEX OFFENSE(F1)',
    'CAPITAL MURDER',
    'CAPITAL MURDER BY TERROR THREAT/OTH FEL(FX',
    'CAPITAL MURDER OF MULTIPLE PERSONS (FX)',
    'CRIM NEGLIGENT HOMICIDE',
    'DISORDERLY CONDUCT-FIGHTING',
    'FAIL STOP RENDER AID INJ/DEATH',
    'FAIL TO STOP AND RENDER AID INJ/DEATH',
    'FEL ASSAULT FV ENHANCED (PREV CONV) (F3)',
    'FEL ASSLT CONTINU VIOLENCE FV 2+W/IN 12MO',
    'FEL ASSLT FV STRANGULATION (F3)',
    'INDECENCY W/CHILD SEXUAL CONTACT',
    'INJ CHI/ELDER/DISAB RECK BOD INJ(FS)',
    'INJ CHILD/ELDER/DISABLE RECK SBI/MEN',
    'INJ CHILD/ELDER/DISABLE W/INT BOD(F3',
    'INJ CHILD/ELDER/DISABLE W/INT SBI/ME',
    'INJ CHILD/ELDERLY/DISABLED CRIM NEG',
    'INTOXICATED MANSLAUGHTER W/VEHICLE',
    'INTOXICATION ASSAULT W/VEHICLE SBI',
    'INTOXICATION MANSLAUGHTER W/VEHICLE',
    'KIDNAPPING',
    'MANSLAUGHTER',
    'MURDER',
    'SEX ABUSE OF CHILD CONTINUOUS:VICT <14 (F1',
    'SEXUAL ASSLT',
    'SEXUAL ASSLT CHILD',
    'SOLIC/COMM CAPITAL MURDER',
    'TAKE WEAPON FROM OFFICER (F3)'
)
