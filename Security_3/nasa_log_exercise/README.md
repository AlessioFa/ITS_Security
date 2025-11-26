# NASA Log Analysis Exercise (1995)

## Project Description
In this project, I analyzed the NASA web server logs from August 1995 using Python. 
I organized the work into three folders to simulate a real investigation process:

1.  **Basic Analysis:** Checking traffic volume and errors to understand the general situation.
2.  **Threat Intelligence:** Searching for specific attack patterns (like "admin" or "backup files").
3.  **Incident Verification:** Checking if any attack was successful (Status Code 200).

## Note on My Learning Process
I am currently studying for the **CompTIA Security+** certification and I am learning Python. 
For this exercise, I used Generative AI (Gemini) to help me write and understand the code.

My main goal was to focus on the **logic** of Log Analysis and Threat Hunting. I wanted to understand *what* to look for in the logs and *how* to interpret the results, rather than writing complex Python scripts from scratch. This helped me understand how a SOC Analyst works.

## Dataset Information
The raw log file used in this project (`NASA_access_log_Aug95`) is **not included** in this repository because it is too large (167 MB).

If you want to run these scripts, you can download the original dataset from the official source (or Kaggle) and place it in the main folder.

## What I Learned
* **Traffic Analysis:** How to distinguish between normal high traffic (like proxies) and suspicious activity.
* **Signatures:** I learned to look for specific "Attack Signatures" (for example: `../` for directory traversal or `.bak` for hidden files).
* **Incident Response:** I understood the critical difference between a failed attempt (Error 404) and a confirmed data breach (Status 200 OK).
