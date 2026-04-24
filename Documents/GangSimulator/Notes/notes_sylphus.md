
## Architecture des lieux, persos et events

### Game
- Money
- Owned_Places
- Recruits (permet les interactions spécifiques au roles + ou -)
- Available_Drugs

### Ville pour l'instant
- Name
- Country
- Pop
- Max_Pop

### établissements
- Name
- Type (box / cave / casino / bar / place)
- Current_Visitors (actualisé chaque jour)
- Max_Visitors
- Boss (un nom)
- Current_Value (pour racheter l'affaire (algo pour la calculer genre avec rep))
- Réputation en % (la fréquentation se fait en fonction de la réputation)

### Les gens 
Ils traînent dans les établissements en fonction de la situation

- Nom
- Age
- Loyauté (entre 25 et 75% au départ) (variable)
- Stability : max 90% (coefficient de changement de loyauté)
- Adresse (boolean)
- Weakness (loves_money, attention_whore, fragile)
- Role (*flic, random, dealer, chemist*, fixer, assassin, pickpocket, détective privé (peut enquêter sur la loyauté, roles etc), addict)
- Known_Roles : `[]`

Optionnels :

- (money)
- (fame)

## Début du jeu

On commence dans une grange abandonnée, assez neutre
Petit loyer mais qui pousse à tryhard
On commence avec un peu d'argent

## Étapes d'une journée

### PROCESS : Mise en place de la journée

- Répartition de la pop dans les lieux
- Actions des pnj calculées
- Actualisation des comptes
- Actualisation des Stocks de drogue
- Actualisation de tout
- Generation des events matinaux

### Wake up

#### Events matinaux
Il peut se passer plusieurs events

- On se fait controller par l'etat / les flics / les impots (mini jeux pour pas se faire prendre)
- On tente de nous assassiner / qqn enquête sur nous
- On reçoit un coup de fil surprise

#### Recap
- On voit le compte de l'argent gagné
- Recap de ce qui s'est passé pendant la nuit (comptes, recap des risques encourus, état des lieux corrompus).

#### Session d'écoute de la radio de la police
- On obtient des infos intéressantes à mémoriser (simple)
- Journées spéciales, events dans des lieux, etc

### Phase de choix d'activité

Dans une journée on peut faire 3 activités (on passe 3 fois par la phase de choix)

- On peut aller trainer dans un lieu (rencontrer des gens) *PRIO*
- On peut manufacturer (dans un lieu) *PRIO*
- On peut dealer *PRIO*
- Rôder (découvrir des lieux, entendre quelque chose) *PRIO*
- On peut acheter un lieu (sert à y cook, autres revenus passifs, mais aussi facteurs de risque)
- On peut commettre un meurtre pour éliminer qqn (par exemple de dangereux pour le business)
	- Choix de le faire soi même ou si on connait un tueur à gages on lui commandite (risques différents)
- On peut menacer une personne pour forcer la loyauté
- On peut enquêter sur une personne
	- Soit soi même soit par un détective privé
	- L'enquete peut donner une fourchette de loyauté sur un personnage
- **Plus tard on rajoutera des options...**

### Fin de journée

#### Payement des factures
- On doit payer les factures (loyer, établissements, libérer qqn de prison)
- Si certaines factures indispensables ne peuvent pas être payées, on perd la game.

## Autres fonctionnalités 
- On ne peut pas assassiner / menacer quelqu'un dont on ne connait pas l'adresse
- Fonction / commande "state" pour avoir un détaillé de tout sur tout dans l'état de la partie.
- Système de sauvegarde (pour l'instant on sauvegarde pas)
- Nombre de jours limités par partie ? (On peut dire 15-20 jours pour une partie). Le but étant de faire le plus gros score ?
- Les établissements peuvent se faire fermer par la police si la reputation est trop basse