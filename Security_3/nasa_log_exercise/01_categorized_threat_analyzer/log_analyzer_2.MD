Analisi delle Minacce e Categorizzazione Log Web NASA (Agosto 1995) Strumento Utilizzato: Python Categorized Threat Analyzer (Classificazione Tattiche e Intenti)

A. Obiettivo

Approfondire l'analisi preliminare classificando le richieste sospette in categorie di attacco specifiche (Information Disclosure, Path Traversal, Admin Hunting). L'obiettivo è comprendere l'intento degli attaccanti e distinguere tra semplice "rumore" di fondo e tentativi di intrusione mirati.

B. Risultati Chiave

1. Minaccia Critica: Information Disclosure (Backup Files) Sono stati rilevati 73 tentativi di accesso a file con estensioni di backup (.bak, .old, .orig).

    Attori: La richiesta proviene da IP eterogenei, tra cui 128.159.143.37 e interlock.turner.com.

    Analisi: A differenza del semplice scanning di directory, questa attività indica la ricerca specifica di errori di configurazione (file dimenticati dagli amministratori).

    Conclusione: Rappresenta il rischio più elevato. Se questi file sono accessibili, potrebbero contenere codice sorgente, password o dati sensibili non presenti nella versione pubblica del sito.

2. Minaccia Tecnica: Directory Traversal Sono stati isolati 16 eventi contenenti il pattern ../ (dot-dot-slash).

    IP Sospetti: Tra gli altri, tmedina.sp.trw.com e player.sea.sikorsky.com.

    Interpretazione: Il pattern suggerisce un tentativo di "uscire" dalla cartella radice del web server per accedere a file di sistema o altre directory non autorizzate.

    Nota: La ripetitività di alcune richieste (spesso legate a percorsi specifici) potrebbe indicare anche link interni malformati nel sito, oltre a possibili attacchi manuali.

3. Attività Diffusa: Ricerca Privilegi (Admin Hunting) La categoria più numerosa conta 89 tentativi di accesso a percorsi amministrativi ("admin").

    Dettaglio: Le richieste provengono da tutto il mondo, inclusi domini universitari (paris.cs.miami.edu) e provider internazionali (ganca122.vol.it, jheaphy.actrix.gen.nz).

    Analisi: Questo traffico rappresenta un "rumore di fondo" costante. Conferma che le pagine di login sono un bersaglio primario per bot e curiosi.

    Conclusione: Sebbene numeroso, questo traffico è meno sofisticato rispetto alla ricerca mirata di file .bak.

C. Raccomandazioni Operative

    Hardening del Server: Configurare il web server per rifiutare tassativamente (Status 403 Forbidden) qualsiasi richiesta per file con estensione .bak, .old, .orig e .config.

    Sanificazione Input: Verificare che il server gestisca correttamente le richieste contenenti ../ e non permetta la navigazione al di fuori della web root.

    Prossimo Step (Cruciale): Eseguire un'analisi mirata ("Incident Verification") per incrociare queste minacce con i codici di risposta HTTP. Dobbiamo sapere se qualcuno di questi 73 tentativi di scaricare backup ha restituito un codice 200 OK (Successo).
