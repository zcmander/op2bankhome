# Siirrä OP-tilitapahtumat HomeBank-sovellukseen

## 1. Lataa CSV-muotoinen tiedosto OP-verkkopankista

![Valitse "Tulosta tilotteita"](Step1.PNG)
* Valitse "Tulosta tilotteita"

![Valitse "Tapahtumat ajalta"](Step2.PNG)
* Valitse "Tapahtumat ajalta". Suosituksena viedä tiedot vuosittain, jolloin tietoja on myös helppo hallita HomeBank-sovelluksessa.

![Valitse "Lataa pelkät tilitapahtumat tiedostona"](Step3.PNG)
* Valitse "Lataa pelkät tilitapahtumat tiedostona"

## 2. Muunna HomeBank:n ymmärtämään CSV-tiedostomuotoon

```
python .\tapahtumat_parser.py .\tapahtumat20190101-20191231.csv
```

Tästä muodostuu uusi tiedosto `converted.csv` ja tätä tiedostoa HomeBank suostuu syömään.

## 3. Tuo HomeBank sovellukseen tiedosto

![Valitse "Tiedosto -> Import..."](Step6.PNG)

![Valitse "Tiedosto -> Import..."](Step7.PNG)

* Muista valita kohtaan "Päiväjärjestys" valinnaksi "y-m-d".

![Valitse "Tiedosto -> Import..."](Step9.PNG)

* Ja valitse "Toteuta"

## 4. Korjaa tilin aloitussaldo

![Valitse "Avaa tiliote omaan ikkunaansa"](Step3.PNG)
* Valitse "Avaa tiliote omaan ikkunaansa"

![Valitse "Tiedosto -> Import..."](Step4.PNG)

* Kopioi punaisella merkitty summa, eli tilinotteen alussa ollut saldo.

* Valitse HomeBank-sovelluksesta "Hallitse tilejä"

![Valitse "Tiedosto -> Import..."](Step9.PNG)

* Syötä aloitus saldo kenttään "Start balance".

## Valmista tuli!