# Script de Détection de Vulnérabilités XSS

## Aperçu

Ce script Python a été conçu pour détecter les vulnérabilités de type Cross-Site Scripting (XSS) sur un site web spécifié. 
Il envoie une charge utile simple à l'URL cible et vérifie si la charge utile est reflétée dans la réponse, indiquant une éventuelle vulnérabilité XSS.

## Utilisation

1. Clonez ce dépôt sur votre machine locale :

    ```bash
    git clone https://github.com/grandtimide/xss-scan-vuln.git
    cd xss-scan-vuln
    ```

2. Exécutez le script et saisissez l'URL cible lorsqu'on vous le demande :

    ```bash
    python xss-scan-vuln.py
    ```

3. Examinez les résultats :

   - Si le script détecte la charge utile XSS dans la réponse, il indiquera une vulnérabilité potentielle.
   - Si le script ne trouve pas la charge utile, il indiquera que le site semble sécurisé.
