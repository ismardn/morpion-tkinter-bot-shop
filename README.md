# Morpion Avancé – Tkinter (Bot Invincible + Boutique)

Ce projet est une version enrichie du célèbre jeu du Morpion (Tic-Tac-Toe), réalisée avec **Tkinter**.  
Le joueur peut notamment affronter un **bot très difficile** (invincible), et accéder à une **boutique d’apparences** pour personnaliser ses pions.

Une sauvegarde automatique permet de conserver ses achats d’une session à l’autre.

## Fonctionnalités
- Interface graphique en Tkinter
- Bot invincible (utilise une stratégie optimale)
- Boutique pour personnaliser l'apparence des croix et des cercles
- Système de score / monnaie pour débloquer des éléments (la monnaie est gagnable lors d'une victoire contre le bot de niveau "Moyen")
- Sauvegarde persistante dans un fichier texte

## Fichiers
- `jeu_du_morpion.pyw` : script principal du jeu
- `sauvegarde.txt` : état de la boutique / apparences débloquées / nombre de pièces
- `SAUVEGARDE_DEFAUT.txt` : sauvegarde d’usine utilisée pour réinitialiser le jeu
- `images/` : ressources graphiques du jeu
  - `apparences/` : skins alternatifs pour croix et cercles

## Lancer le jeu

Assurez-vous d’avoir Python 3 installé.

```bash
python jeu_du_morpion.pyw
```

---

*Projet réalisé en juin 2022, mis en ligne ici en juin 2025.*
