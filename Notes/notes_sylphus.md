
## Architecture des lieux, persos et events

### Ville pour l'instant
- Name
- Country
- Pop
- Max_Pop

### établissements
- Name
- Current_Visitors
- Max_Visitors
- Exployees (array)
- Boss (un nom)
- Current_Value (pour racheter l'affaire)
- Réputation (la fréquentation se fait en fonction de la réputation)

### Les gens 
Ils trainent dans les établissements en fonction de la situation

- Nom
- Age
- Money
- Fame
- Corruption (money / fame / menace)
- Loyauté (variable)
- Adresse
- Friend (boolean)
- Status (flic, random, brig, dealer, chemist, fixer, assassin, détective privé, addict)
	- Le fait qu'on découvre un status n'est pas enregistré. Le joueur peut guess par exemple pour demander une enquête privée, mais si il se trompe, il perd un tour de jeu et peut prendre des risques. ça simplifie le code et rajoute une mécanique obscure où il faut retenir / prendre des notes. (à voir)
- Notes (un array d'infos enregistrées / découvertes sur le personnage par le joueur)

Tour par tour de jour en jour on rencontre des gens

## Étapes d'une journée

### Wake up (recap)
- Recap de ce qui s'est passé pendant la nuit (comptes, recap des risques encourus, etat des lieux corrompus).
- Session d'écoute de la radio de la police

### Phase de choix d'activité
- On peut aller trainer dans la rue (rencontrer des gens) *PRIO*
- On peut manufacturer *PRIO*
- On peut dealer *PRIO*
- On peut commettre un meurtre pour éliminer qqn (par exemple de dangereux pour le business)
	- Choix de le faire soi même ou si on connait un tueur à gages on lui commandite (risques différents)
- On peut menacer une personne pour forcer la loyauté
- On peut enquêter sur une personne
	- Soit soi même soit par un détective privé
- **Plus tard on rajoutera des options...**

Activité bonus qui compte pas dans le compteur : 
- Prendre des notes sur un personnage
	- Possible n'importe quand ? 

### Phase d'activités

Dans une journée on peut faire 3 activités (on passe 3 fois par la phase de choix)

### Fin de journée

#### Events de fin de journée
Il peut se passer plusieurs events
- On se fait controller par l'etat / les flics / les impots (mini jeux pour pas se faire prendre)
- On tente de nous assassiner / qqn enquête sur nous
- On reçoit un coup de fil surprise

#### Payement des factures
- On voit le compte de l'argent gagné, les points d'influence
- On doit payer les factures (loyer, établissements, libérer qqn de prison)
- Si certaines factures indispensables ne peuvent pas être payées, on perd la game.

## Autres fonctionnalités 
- On ne peut pas assassiner / menacer quelqu'un dont on ne connait pas l'adresse
- Fonction / commande "state" pour avoir un détaillé de tout sur tout dans l'état de la partie.
- Système de sauvegarde (pour l'instant on sauvegarde pas)
- Nombre de jours limités par partie ? (On peut dire 15-20 jours pour une partie). Le but étant de faire le plus gros score ?