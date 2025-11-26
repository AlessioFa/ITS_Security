Analisi Critica Incidenti Confermati Log Web NASA (Agosto 1995)
Strumento Utilizzato: Python Incident Verification Analyzer (Filtro: Status Code 200 OK)

A. Obiettivo

Isolare e verificare esclusivamente gli eventi in cui un tentativo di accesso a risorse sensibili o pattern di attacco ha avuto successo (Codice HTTP 200). Lo scopo è distinguere i semplici tentativi falliti (blocked events) dalle compromissioni reali dei dati (confirmed breaches).

B. Risultati Chiave

1. Incidente Confermato: Information Disclosure (Backup Files)
L'analisi ha confermato che il server ha servito correttamente (Status 200) file di backup a utenti non autorizzati. Questa è la criticità maggiore rilevata.

    Evidenze Critiche:
    - Il file /software/webadmin/astronauts.old è stato scaricato dall'IP l23aj.jsc.nasa.gov e paris.cs.miami.edu.
    - Il file /history/apollo/apollo-1/apollo-1-info.bak è stato scaricato da decine di IP esterni diversi.

    Analisi: L'estensione .old presente nella cartella /webadmin/ suggerisce la presenza di dati non destinati al pubblico. Questi file non sono stati sanificati e potrebbero contenere PII (Personally Identifiable Information) degli astronauti o credenziali di sistema obsolete ma ancora vulnerabili.

2. Anomalia di Configurazione: Path Traversal
Sono state rilevate risposte positive (200 OK) per richieste contenenti il pattern ../.

    Dettaglio Evento:
    - Pattern ricorrente: GET /mdss/srqa/../MDSS.html
    - IP Coinvolti: bushpea.agcomed.uiuc.edu, phoenix.erc.msstate.edu e altri.

    Interpretazione: Sebbene il server abbia accettato il pattern ../ (tipico degli attacchi traversal), l'analisi del percorso suggerisce che si tratti di link interni malformati piuttosto che di un attacco malevolo esterno. Tuttavia, il fatto che il web server risolva i percorsi relativi rappresenta una vulnerabilità di configurazione sfruttabile.

C. Raccomandazioni Urgenti (Remediation)

    Data Sanitization: Rimuovere immediatamente tutti i file con estensione .bak, .old, .orig e .bak1 dalla directory pubblica del web server.

    Access Control: Limitare l'accesso alla directory /software/webadmin/ esclusivamente agli IP della rete di gestione interna, richiedendo autenticazione forte.

    Investigazione Forense: Analizzare il contenuto del file astronauts.old per determinare l'esatta natura dei dati esfiltrati (es. indirizzi, dati personali) e valutare la gravità del data breach.
