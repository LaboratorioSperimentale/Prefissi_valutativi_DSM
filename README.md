# Prefissi

6 prefissi:
- ultra
- extra
- iper
- arci
- super
- stra


## Fase 1:
Controllare frequenze di aggettivi, sostantivi, avverbi, verbi derivati composti da:
- `[pref]X`
- `[pref]-X`
- `[pref] X`


Abbiamo una lista dallo Zingarelli per escludere i derivati in cui la prefissazione non è l'ultimo processo di formazione e quelli in cui il morfema non è un prefisso.

## Fase 2:
Costruiamo uno spazio distribuzionale normalizzando le versioni ortografiche dei composti con prefisso

es. `[pref]-X` > `[pref]X`

## Fase 3:
Per ogni prefisso, clusterizziamo le basi X.

Facciamo emergere i sensi dai cluster e controlliamo la relazione con i sensi elencanei dizionari per ogni prefisso.

## Fase 3b:

Manual tagging di esempi

TODO: definire come estrarre sample

## Fase 4:
Calcoliamo, per ogni possibile base X il vector offset

`v_o = v(X) - v([pref]X)`

e controlliamo se ci sono differenze significative tra gli offset di sensi diversi.



# NOTE
* Abstract a workshop SLI?