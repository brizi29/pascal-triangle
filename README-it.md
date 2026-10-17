# Generatore del Triangolo di Pascal (Layout Equilatero)

Un'applicazione CLI Python robusta e ottimizzata visivamente che genera e mostra il Triangolo di Pascal in un layout equilatero perfettamente bilanciato. Sviluppata e testata nativamente all'interno dell'IDE Thonny.

## Funzionalità

- **Allineamento Geometrico Perfetto:** Utilizza la formattazione avanzata delle stringhe (`^2`) e rapporti matematici di spaziatura strutturale per garantire che sia i numeri a una cifra che quelli a due cifre si allineino perfettamente in un triangolo equilatero simmetrico.
- **Validazione Robusta dell'Input:** Implementa un ciclo di controllo stringente tramite `try-except` che evita input decimali, stringhe di testo e caratteri speciali senza causare il crash del programma.
- **Limite Visivo di Sicurezza:** Include un vincolo di sicurezza integrato impostato a un massimo di 9 righe. Questo impedisce all'output di andare a capo o di rompere la sua forma geometrica sui terminali standard a spaziatura fissa a causa dell'espansione dei numeri a più cifre.

## Come Funziona

1. Il programma richiede continuamente all'utente un numero valido di righe (intero da 1 a 9).
2. Costruisce dinamicamente la matrice del triangolo utilizzando una struttura a liste annidate.
3. Un blocco di stampa su misura inserisce dinamicamente un'indentazione proporzionale e la centratura degli elementi per preservare la simmetria visiva.

## Requisiti

- Python 3.x
- Qualsiasi ambiente di terminale standard a spaziatura fissa o IDE (ottimizzato per Thonny).
