#!/usr/bin/env python3

# Définition de la fonction pour calculer le salaire pour un mois
def calcul_mois(taux_horaire):
    heures_par_jour = 8  # Nombre d'heures travaillées par jour
    jours_ouvrables_mois = 22  # Nombre de jours ouvrables dans le mois

    # Calcul du salaire pour un mois en multipliant le taux horaire par le nombre d'heures par jour et le nombre de jours ouvrables dans le mois
    salaire_mois = taux_horaire * heures_par_jour * jours_ouvrables_mois
    return salaire_mois


# Définition de la fonction pour calculer le salaire pour un an
def calcul_an(taux_horaire):
    heures_par_jour = 8  # Nombre d'heures travaillées par jour
    jours_ouvrables_an = 302  # Nombre de jours ouvrables dans l'année

    # Calcul du salaire pour un an en multipliant le taux horaire par le nombre d'heures par jour et le nombre de jours ouvrables dans l'année
    salaire_an = taux_horaire * heures_par_jour * jours_ouvrables_an
    return salaire_an


# Demande à l'utilisateur d'entrer son taux horaire
taux_horaire = float(input("Entrez votre taux horaire : "))

# Appel de la fonction calcul_mois avec le taux horaire entré et affichage du salaire pour un mois
salaire_mois = calcul_mois(taux_horaire)
print("Salaire pour un mois (22 jours ouvrés) :", salaire_mois)

# Appel de la fonction calcul_an avec le taux horaire entré et affichage du salaire pour un an
salaire_an = calcul_an(taux_horaire)
print("Salaire pour un an (302 jours ouvrés) :", salaire_an)
