Analisi Preliminare Log Web NASA (Agosto 1995) Strumento Utilizzato: Python Basic Analyzer (Volume, Errori, Keyword statiche)

A. Obiettivo

Analizzare il file di log per identificare anomalie di volume, errori massivi e tentativi di accesso a risorse note come sensibili (admin, file di sistema) utilizzando un approccio basato su firme semplici.

B. Risultati Chiave

1. Analisi Volumetrica (Top Talkers) L'analisi del volume di traffico ha evidenziato i seguenti attori principali:

    IP Principale: edams.ksc.nasa.gov con 6530 richieste.

    Analisi: Essendo un dominio .nasa.gov (Kennedy Space Center), questo traffico è classificato come INTERNO/LEGITTIMO.

    Nota: Diversi sottodomini prodigy.com (provider internet) generano alto traffico (ca. 4000 richieste ciascuno). Questo pattern è coerente con il normale traffico utenti/proxy e non indica un attacco DoS.

2. Analisi degli Errori (Enumeration Detection) Gli IP che generano il maggior numero di errori (Codici 4xx/5xx) sono:

    IP Sospetto: dialip-217.den.mmc.com (62 errori).

    Interpretazione: Un alto tasso di errori rispetto alle richieste normali suggerisce un'attività di Scanning (tentativi di indovinare URL) o una configurazione client errata. Sebbene il numero non sia critico, merita monitoraggio.

3. Rilevamento Minacce (Signature Matching) Sono state rilevate 113 occorrenze di parole chiave sospette.

    Minaccia Principale: L'host malin.space.se ha effettuato tentativi ripetuti e mirati.

    Dettaglio Attacco:

        GET /software/webadmin/

        GET /software/webadmin/readme.txt

        GET /software/webadmin/apollo.perl

    Conclusione: Questo è un chiaro tentativo di Discovery/Enumeration. L'attaccante sta cercando script amministrativi (.perl) e documentazione nella cartella /webadmin/.

C. Raccomandazioni Iniziali

    Blocco IP: Valutare il blocco dell'IP malin.space.se sul firewall perimetrale.

    Verifica Percorso: Verificare se la cartella /software/webadmin/ è accessibile pubblicamente. Se sì, restringerla immediatamente (HTTP Auth o restrizione IP).

    Approfondimento: Eseguire una seconda analisi mirata per vedere se l'IP malin.space.se ha mai ricevuto un codice 200 OK (accesso riuscito).
