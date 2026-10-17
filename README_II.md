# Generatore del Triangolo di Pascal (Layout Equilatero)

Un'applicazione CLI Python robusta e ottimizzata visivamente che genera e mostra il Triangolo di Pascal in un layout equilatero perfettamente bilanciato. Sviluppata e testata nativamente all'interno dell'IDE Thonny.

## Funzionalità

- **Allineamento Geometrico Perfetto:** Utilizza la formattazione avanzata delle stringhe (`^2`) e rapporti matematici di spaziatura strutturale per garantire che sia i numeri a una cifra che quelli a due cifre si allineino perfettamente in un triangolo equilatero simmetrico.
- **Validazione Robusta dell'Input:** Implementa un ciclo di controllo stringente tramite `try-except` che rifiuta numeri decimali, stringhe di testo e caratteri speciali senza causare il crash del programma.
- **Limite Visivo di Sicurezza:** Include un vincolo di sicurezza integrato impostato a un massimo di 9 righe. Questo impedisce all'output di andare a capo o di rompere la sua forma geometrica sui terminali standard a spaziatura fissa a causa dell'espansione dei numeri a più cifre.

## Codice Sorgente Python

Copia ed esegui questo codice all'interno del tuo ambiente Python:

```python
list1 = []

# Ciclo di verifica per l'input dell'utente
while True:
    try:
        user_input = input("Enter the number of rows to discover (Max 9): ")
        
        # Converte in intero (intercetta testo e caratteri speciali)
        n = int(user_input)
        
        # Controllo del limite geometrico e visivo
        if n <= 0:
            print("Error: Please enter a number greater than 0.")
        elif n > 9:
            print(f"Error: The value {n} exceeds the maximum limit of 9 rows.")
            print("Beyond row 9, the visual formatting of the triangle breaks down.")
        else:
            break # Input valido, esce dal ciclo
            
    except ValueError:
        print("Error: Input contains text or special characters. Please enter a whole number only.")

# Generazione del Triangolo di Pascal
for i in range(n):
    temp_list=[]
    for j in range(i+1):
        if (j== 0 or j == i):
            temp_list.append(1)
        else:
            temp_list.append(list1[i-1][j-1] +list1[i-1][j])
    list1.append(temp_list)

# Blocco di stampa per un Triangolo Equilatero Perfetto e Simmetrico
for i in range(n):
    # Ogni riga arretra esattamente di 2 spazi rispetto alla precedente
    print(" " * (n - i - 1) * 2, end="")
    
    # Centratura simmetrica (^2) di ogni numero all'interno del suo blocco
    row_strings = [format(list1[i][j], "^2") for j in range(i+1)]
    print("  ".join(row_strings))
```

## Requisiti

- Python 3.x
- Qualsiasi ambiente di terminale standard a spaziatura fissa o IDE (ottimizzato per Thonny).
