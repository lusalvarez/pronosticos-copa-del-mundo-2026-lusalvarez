import json
import re
from datetime import datetime

# Données extraites du PDF
matches_data = []

# Phase de groupes - 72 matches
phase_groupes = [
    {"numero": 1, "date": "2026-06-11", "heure": "21:00", "groupe": "A", "equipe_domicile": "Mexique", "equipe_exterieur": "Afrique du Sud", "stade": "Estadio Azteca", "ville": "Mexico", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 2, "date": "2026-06-12", "heure": "04:00", "groupe": "A", "equipe_domicile": "Corée du Sud", "equipe_exterieur": "Tchéquie", "stade": "Estadio Akron", "ville": "Guadalajara", "diffusion": ["beIN Sports"]},
    {"numero": 3, "date": "2026-06-12", "heure": "21:00", "groupe": "B", "equipe_domicile": "Canada", "equipe_exterieur": "Bosnie-Herzégovine", "stade": "BMO Field", "ville": "Toronto", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 4, "date": "2026-06-13", "heure": "03:00", "groupe": "D", "equipe_domicile": "États-Unis", "equipe_exterieur": "Paraguay", "stade": "SoFi Stadium", "ville": "Los Angeles", "diffusion": ["beIN Sports"]},
    {"numero": 8, "date": "2026-06-13", "heure": "21:00", "groupe": "B", "equipe_domicile": "Qatar", "equipe_exterieur": "Suisse", "stade": "Levi's Stadium", "ville": "San Francisco / Santa Clara", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 7, "date": "2026-06-14", "heure": "00:00", "groupe": "C", "equipe_domicile": "Brésil", "equipe_exterieur": "Maroc", "stade": "MetLife Stadium", "ville": "New York / East Rutherford", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 5, "date": "2026-06-14", "heure": "03:00", "groupe": "C", "equipe_domicile": "Haïti", "equipe_exterieur": "Écosse", "stade": "Gillette Stadium", "ville": "Boston / Foxborough", "diffusion": ["beIN Sports"]},
    {"numero": 6, "date": "2026-06-14", "heure": "06:00", "groupe": "D", "equipe_domicile": "Australie", "equipe_exterieur": "Turquie", "stade": "BC Place", "ville": "Vancouver", "diffusion": ["beIN Sports"]},
    {"numero": 10, "date": "2026-06-14", "heure": "19:00", "groupe": "E", "equipe_domicile": "Allemagne", "equipe_exterieur": "Curaçao", "stade": "NRG Stadium", "ville": "Houston", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 11, "date": "2026-06-14", "heure": "22:00", "groupe": "F", "equipe_domicile": "Pays-Bas", "equipe_exterieur": "Japon", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 9, "date": "2026-06-15", "heure": "01:00", "groupe": "E", "equipe_domicile": "Côte d'Ivoire", "equipe_exterieur": "Équateur", "stade": "Lincoln Financial Field", "ville": "Philadelphia", "diffusion": ["beIN Sports"]},
    {"numero": 12, "date": "2026-06-15", "heure": "04:00", "groupe": "F", "equipe_domicile": "Suède", "equipe_exterieur": "Tunisie", "stade": "Estadio BBVA", "ville": "Monterrey", "diffusion": ["beIN Sports"]},
    {"numero": 13, "date": "2026-06-15", "heure": "18:00", "groupe": "H", "equipe_domicile": "Espagne", "equipe_exterieur": "Cap-Vert", "stade": "Mercedes-Benz Stadium", "ville": "Atlanta", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 14, "date": "2026-06-15", "heure": "21:00", "groupe": "G", "equipe_domicile": "Belgique", "equipe_exterieur": "Égypte", "stade": "Lumen Field", "ville": "Seattle", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 15, "date": "2026-06-16", "heure": "00:00", "groupe": "H", "equipe_domicile": "Arabie Saoudite", "equipe_exterieur": "Uruguay", "stade": "Hard Rock Stadium", "ville": "Miami", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 16, "date": "2026-06-16", "heure": "03:00", "groupe": "G", "equipe_domicile": "Iran", "equipe_exterieur": "Nouvelle-Zélande", "stade": "SoFi Stadium", "ville": "Los Angeles", "diffusion": ["beIN Sports"]},
    {"numero": 17, "date": "2026-06-16", "heure": "21:00", "groupe": "I", "equipe_domicile": "France", "equipe_exterieur": "Sénégal", "stade": "MetLife Stadium", "ville": "New York / East Rutherford", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 18, "date": "2026-06-17", "heure": "00:00", "groupe": "I", "equipe_domicile": "Irak", "equipe_exterieur": "Norvège", "stade": "Gillette Stadium", "ville": "Boston / Foxborough", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 19, "date": "2026-06-17", "heure": "03:00", "groupe": "J", "equipe_domicile": "Argentine", "equipe_exterieur": "Algérie", "stade": "Arrowhead Stadium", "ville": "Kansas City", "diffusion": ["beIN Sports"]},
    {"numero": 20, "date": "2026-06-17", "heure": "06:00", "groupe": "J", "equipe_domicile": "Autriche", "equipe_exterieur": "Jordanie", "stade": "Levi's Stadium", "ville": "San Francisco / Santa Clara", "diffusion": ["beIN Sports"]},
    {"numero": 21, "date": "2026-06-17", "heure": "19:00", "groupe": "K", "equipe_domicile": "Portugal", "equipe_exterieur": "RD Congo", "stade": "NRG Stadium", "ville": "Houston", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 22, "date": "2026-06-17", "heure": "22:00", "groupe": "L", "equipe_domicile": "Angleterre", "equipe_exterieur": "Croatie", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 23, "date": "2026-06-18", "heure": "01:00", "groupe": "L", "equipe_domicile": "Ghana", "equipe_exterieur": "Panama", "stade": "BMO Field", "ville": "Toronto", "diffusion": ["beIN Sports"]},
    {"numero": 24, "date": "2026-06-18", "heure": "04:00", "groupe": "K", "equipe_domicile": "Ouzbékistan", "equipe_exterieur": "Colombie", "stade": "Estadio Azteca", "ville": "Mexico", "diffusion": ["beIN Sports"]},
    {"numero": 25, "date": "2026-06-18", "heure": "18:00", "groupe": "A", "equipe_domicile": "Tchéquie", "equipe_exterieur": "Afrique du Sud", "stade": "Mercedes-Benz Stadium", "ville": "Atlanta", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 26, "date": "2026-06-18", "heure": "21:00", "groupe": "B", "equipe_domicile": "Suisse", "equipe_exterieur": "Bosnie-Herzégovine", "stade": "SoFi Stadium", "ville": "Los Angeles", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 27, "date": "2026-06-19", "heure": "00:00", "groupe": "B", "equipe_domicile": "Canada", "equipe_exterieur": "Qatar", "stade": "BC Place", "ville": "Vancouver", "diffusion": ["beIN Sports"]},
    {"numero": 28, "date": "2026-06-19", "heure": "03:00", "groupe": "A", "equipe_domicile": "Mexique", "equipe_exterieur": "Corée du Sud", "stade": "Estadio Akron", "ville": "Guadalajara", "diffusion": ["beIN Sports"]},
    {"numero": 29, "date": "2026-06-19", "heure": "21:00", "groupe": "D", "equipe_domicile": "États-Unis", "equipe_exterieur": "Australie", "stade": "Lumen Field", "ville": "Seattle", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 30, "date": "2026-06-20", "heure": "00:00", "groupe": "C", "equipe_domicile": "Écosse", "equipe_exterieur": "Maroc", "stade": "Gillette Stadium", "ville": "Boston / Foxborough", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 31, "date": "2026-06-20", "heure": "02:30", "groupe": "C", "equipe_domicile": "Brésil", "equipe_exterieur": "Haïti", "stade": "Lincoln Financial Field", "ville": "Philadelphia", "diffusion": ["beIN Sports"]},
    {"numero": 32, "date": "2026-06-20", "heure": "05:00", "groupe": "D", "equipe_domicile": "Turquie", "equipe_exterieur": "Paraguay", "stade": "Levi's Stadium", "ville": "San Francisco / Santa Clara", "diffusion": ["beIN Sports"]},
    {"numero": 33, "date": "2026-06-20", "heure": "19:00", "groupe": "F", "equipe_domicile": "Pays-Bas", "equipe_exterieur": "Suède", "stade": "NRG Stadium", "ville": "Houston", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 34, "date": "2026-06-20", "heure": "22:00", "groupe": "E", "equipe_domicile": "Allemagne", "equipe_exterieur": "Côte d'Ivoire", "stade": "BMO Field", "ville": "Toronto", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 35, "date": "2026-06-21", "heure": "02:00", "groupe": "E", "equipe_domicile": "Équateur", "equipe_exterieur": "Curaçao", "stade": "Arrowhead Stadium", "ville": "Kansas City", "diffusion": ["beIN Sports"]},
    {"numero": 36, "date": "2026-06-21", "heure": "06:00", "groupe": "F", "equipe_domicile": "Tunisie", "equipe_exterieur": "Japon", "stade": "Estadio BBVA", "ville": "Monterrey", "diffusion": ["beIN Sports"]},
    {"numero": 37, "date": "2026-06-21", "heure": "18:00", "groupe": "H", "equipe_domicile": "Espagne", "equipe_exterieur": "Arabie Saoudite", "stade": "Mercedes-Benz Stadium", "ville": "Atlanta", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 38, "date": "2026-06-21", "heure": "21:00", "groupe": "G", "equipe_domicile": "Belgique", "equipe_exterieur": "Iran", "stade": "SoFi Stadium", "ville": "Los Angeles", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 39, "date": "2026-06-22", "heure": "00:00", "groupe": "H", "equipe_domicile": "Uruguay", "equipe_exterieur": "Cap-Vert", "stade": "Hard Rock Stadium", "ville": "Miami", "diffusion": ["beIN Sports"]},
    {"numero": 40, "date": "2026-06-22", "heure": "03:00", "groupe": "G", "equipe_domicile": "Nouvelle-Zélande", "equipe_exterieur": "Égypte", "stade": "BC Place", "ville": "Vancouver", "diffusion": ["beIN Sports"]},
    {"numero": 43, "date": "2026-06-22", "heure": "19:00", "groupe": "J", "equipe_domicile": "Argentine", "equipe_exterieur": "Autriche", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 41, "date": "2026-06-22", "heure": "23:00", "groupe": "I", "equipe_domicile": "France", "equipe_exterieur": "Irak", "stade": "Lincoln Financial Field", "ville": "Philadelphia", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 42, "date": "2026-06-23", "heure": "02:00", "groupe": "I", "equipe_domicile": "Norvège", "equipe_exterieur": "Sénégal", "stade": "MetLife Stadium", "ville": "New York / East Rutherford", "diffusion": ["beIN Sports"]},
    {"numero": 44, "date": "2026-06-23", "heure": "05:00", "groupe": "J", "equipe_domicile": "Jordanie", "equipe_exterieur": "Algérie", "stade": "Levi's Stadium", "ville": "San Francisco / Santa Clara", "diffusion": ["beIN Sports"]},
    {"numero": 45, "date": "2026-06-23", "heure": "19:00", "groupe": "K", "equipe_domicile": "Portugal", "equipe_exterieur": "Ouzbékistan", "stade": "NRG Stadium", "ville": "Houston", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 46, "date": "2026-06-23", "heure": "22:00", "groupe": "L", "equipe_domicile": "Angleterre", "equipe_exterieur": "Ghana", "stade": "Gillette Stadium", "ville": "Boston / Foxborough", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 47, "date": "2026-06-24", "heure": "01:00", "groupe": "L", "equipe_domicile": "Panama", "equipe_exterieur": "Croatie", "stade": "BMO Field", "ville": "Toronto", "diffusion": ["beIN Sports"]},
    {"numero": 48, "date": "2026-06-24", "heure": "04:00", "groupe": "K", "equipe_domicile": "Colombie", "equipe_exterieur": "RD Congo", "stade": "Estadio Akron", "ville": "Guadalajara", "diffusion": ["beIN Sports"]},
    {"numero": 49, "date": "2026-06-24", "heure": "21:00", "groupe": "B", "equipe_domicile": "Suisse", "equipe_exterieur": "Canada", "stade": "BC Place", "ville": "Vancouver", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 50, "date": "2026-06-24", "heure": "21:00", "groupe": "B", "equipe_domicile": "Bosnie-Herzégovine", "equipe_exterieur": "Qatar", "stade": "Lumen Field", "ville": "Seattle", "diffusion": ["beIN Sports"]},
    {"numero": 55, "date": "2026-06-25", "heure": "00:00", "groupe": "C", "equipe_domicile": "Écosse", "equipe_exterieur": "Brésil", "stade": "Hard Rock Stadium", "ville": "Miami", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 56, "date": "2026-06-25", "heure": "00:00", "groupe": "C", "equipe_domicile": "Maroc", "equipe_exterieur": "Haïti", "stade": "Mercedes-Benz Stadium", "ville": "Atlanta", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 52, "date": "2026-06-25", "heure": "03:00", "groupe": "A", "equipe_domicile": "Tchéquie", "equipe_exterieur": "Mexique", "stade": "Estadio Azteca", "ville": "Mexico", "diffusion": ["beIN Sports"]},
    {"numero": 51, "date": "2026-06-25", "heure": "03:00", "groupe": "A", "equipe_domicile": "Afrique du Sud", "equipe_exterieur": "Corée du Sud", "stade": "Estadio BBVA", "ville": "Monterrey", "diffusion": ["beIN Sports"]},
    {"numero": 58, "date": "2026-06-25", "heure": "22:00", "groupe": "E", "equipe_domicile": "Curaçao", "equipe_exterieur": "Côte d'Ivoire", "stade": "Lincoln Financial Field", "ville": "Philadelphia", "diffusion": ["beIN Sports"]},
    {"numero": 57, "date": "2026-06-25", "heure": "22:00", "groupe": "E", "equipe_domicile": "Équateur", "equipe_exterieur": "Allemagne", "stade": "MetLife Stadium", "ville": "New York / East Rutherford", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 60, "date": "2026-06-26", "heure": "01:00", "groupe": "F", "equipe_domicile": "Japon", "equipe_exterieur": "Suède", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["beIN Sports"]},
    {"numero": 59, "date": "2026-06-26", "heure": "01:00", "groupe": "F", "equipe_domicile": "Tunisie", "equipe_exterieur": "Pays-Bas", "stade": "Arrowhead Stadium", "ville": "Kansas City", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 54, "date": "2026-06-26", "heure": "04:00", "groupe": "D", "equipe_domicile": "Turquie", "equipe_exterieur": "États-Unis", "stade": "SoFi Stadium", "ville": "Los Angeles", "diffusion": ["beIN Sports"]},
    {"numero": 53, "date": "2026-06-26", "heure": "04:00", "groupe": "D", "equipe_domicile": "Paraguay", "equipe_exterieur": "Australie", "stade": "Levi's Stadium", "ville": "San Francisco / Santa Clara", "diffusion": ["beIN Sports"]},
    {"numero": 61, "date": "2026-06-26", "heure": "21:00", "groupe": "I", "equipe_domicile": "Norvège", "equipe_exterieur": "France", "stade": "Gillette Stadium", "ville": "Boston / Foxborough", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 62, "date": "2026-06-26", "heure": "21:00", "groupe": "I", "equipe_domicile": "Sénégal", "equipe_exterieur": "Irak", "stade": "BMO Field", "ville": "Toronto", "diffusion": ["beIN Sports"]},
    {"numero": 65, "date": "2026-06-27", "heure": "02:00", "groupe": "H", "equipe_domicile": "Cap-Vert", "equipe_exterieur": "Arabie Saoudite", "stade": "NRG Stadium", "ville": "Houston", "diffusion": ["beIN Sports"]},
    {"numero": 66, "date": "2026-06-27", "heure": "02:00", "groupe": "H", "equipe_domicile": "Uruguay", "equipe_exterieur": "Espagne", "stade": "Estadio Akron", "ville": "Guadalajara", "diffusion": ["beIN Sports"]},
    {"numero": 68, "date": "2026-06-27", "heure": "05:00", "groupe": "G", "equipe_domicile": "Égypte", "equipe_exterieur": "Iran", "stade": "Lumen Field", "ville": "Seattle", "diffusion": ["beIN Sports"]},
    {"numero": 67, "date": "2026-06-27", "heure": "05:00", "groupe": "G", "equipe_domicile": "Nouvelle-Zélande", "equipe_exterieur": "Belgique", "stade": "BC Place", "ville": "Vancouver", "diffusion": ["beIN Sports"]},
    {"numero": 71, "date": "2026-06-27", "heure": "23:00", "groupe": "L", "equipe_domicile": "Panama", "equipe_exterieur": "Angleterre", "stade": "MetLife Stadium", "ville": "New York / East Rutherford", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 72, "date": "2026-06-27", "heure": "23:00", "groupe": "L", "equipe_domicile": "Croatie", "equipe_exterieur": "Ghana", "stade": "Lincoln Financial Field", "ville": "Philadelphia", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 69, "date": "2026-06-28", "heure": "01:30", "groupe": "K", "equipe_domicile": "Colombie", "equipe_exterieur": "Portugal", "stade": "Hard Rock Stadium", "ville": "Miami", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 70, "date": "2026-06-28", "heure": "01:30", "groupe": "K", "equipe_domicile": "RD Congo", "equipe_exterieur": "Ouzbékistan", "stade": "Mercedes-Benz Stadium", "ville": "Atlanta", "diffusion": ["beIN Sports"]},
    {"numero": 64, "date": "2026-06-28", "heure": "04:00", "groupe": "J", "equipe_domicile": "Algérie", "equipe_exterieur": "Autriche", "stade": "Arrowhead Stadium", "ville": "Kansas City", "diffusion": ["beIN Sports"]},
    {"numero": 63, "date": "2026-06-28", "heure": "04:00", "groupe": "J", "equipe_domicile": "Jordanie", "equipe_exterieur": "Argentine", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["beIN Sports"]}
]

# Phase finale - Seizièmes de finale
seiziemes = [
    {"numero": 73, "date": "2026-06-28", "heure": "21:00", "phase": "Seizième de finale", "equipe_domicile": "2A", "equipe_exterieur": "2B", "stade": "SoFi Stadium", "ville": "Los Angeles", "diffusion": ["beIN Sports"]},
    {"numero": 74, "date": "2026-06-29", "heure": "15:00", "phase": "Seizième de finale", "equipe_domicile": "1F", "equipe_exterieur": "2C", "stade": "Estadio BBVA", "ville": "Monterrey", "diffusion": ["beIN Sports"]},
    {"numero": 75, "date": "2026-06-29", "heure": "18:30", "phase": "Seizième de finale", "equipe_domicile": "1E", "equipe_exterieur": "3e ABCDF", "stade": "Gillette Stadium", "ville": "Boston / Foxborough", "diffusion": ["beIN Sports"]},
    {"numero": 76, "date": "2026-06-29", "heure": "22:00", "phase": "Seizième de finale", "equipe_domicile": "1C", "equipe_exterieur": "2F", "stade": "NRG Stadium", "ville": "Houston", "diffusion": ["beIN Sports"]},
    {"numero": 77, "date": "2026-06-30", "heure": "15:00", "phase": "Seizième de finale", "equipe_domicile": "1A", "equipe_exterieur": "3e CEFHI", "stade": "Estadio Azteca", "ville": "Mexico", "diffusion": ["beIN Sports"]},
    {"numero": 78, "date": "2026-06-30", "heure": "19:00", "phase": "Seizième de finale", "equipe_domicile": "2E", "equipe_exterieur": "2I", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["beIN Sports"]},
    {"numero": 79, "date": "2026-06-30", "heure": "23:00", "phase": "Seizième de finale", "equipe_domicile": "1I", "equipe_exterieur": "3e CDFGH", "stade": "MetLife Stadium", "ville": "New York / East Rutherford", "diffusion": ["beIN Sports"]},
    {"numero": 80, "date": "2026-07-01", "heure": "14:00", "phase": "Seizième de finale", "equipe_domicile": "1D", "equipe_exterieur": "3e BEFIJ", "stade": "Levi's Stadium", "ville": "San Francisco / Santa Clara", "diffusion": ["beIN Sports"]},
    {"numero": 81, "date": "2026-07-01", "heure": "18:00", "phase": "Seizième de finale", "equipe_domicile": "1L", "equipe_exterieur": "3e EHIJK", "stade": "Mercedes-Benz Stadium", "ville": "Atlanta", "diffusion": ["beIN Sports"]},
    {"numero": 82, "date": "2026-07-01", "heure": "22:00", "phase": "Seizième de finale", "equipe_domicile": "1G", "equipe_exterieur": "3e AEHIJ", "stade": "Lumen Field", "ville": "Seattle", "diffusion": ["beIN Sports"]},
    {"numero": 83, "date": "2026-07-02", "heure": "14:00", "phase": "Seizième de finale", "equipe_domicile": "1H", "equipe_exterieur": "2J", "stade": "SoFi Stadium", "ville": "Los Angeles", "diffusion": ["beIN Sports"]},
    {"numero": 84, "date": "2026-07-02", "heure": "17:00", "phase": "Seizième de finale", "equipe_domicile": "1B", "equipe_exterieur": "3e EFGIJ", "stade": "BC Place", "ville": "Vancouver", "diffusion": ["beIN Sports"]},
    {"numero": 85, "date": "2026-07-02", "heure": "21:00", "phase": "Seizième de finale", "equipe_domicile": "2K", "equipe_exterieur": "2L", "stade": "BMO Field", "ville": "Toronto", "diffusion": ["beIN Sports"]},
    {"numero": 86, "date": "2026-07-03", "heure": "03:30", "phase": "Seizième de finale", "equipe_domicile": "1K", "equipe_exterieur": "3e DEIJL", "stade": "Arrowhead Stadium", "ville": "Kansas City", "diffusion": ["beIN Sports"]},
    {"numero": 87, "date": "2026-07-03", "heure": "20:00", "phase": "Seizième de finale", "equipe_domicile": "2D", "equipe_exterieur": "2G", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["beIN Sports"]},
    {"numero": 88, "date": "2026-07-04", "heure": "00:00", "phase": "Seizième de finale", "equipe_domicile": "1J", "equipe_exterieur": "2H", "stade": "Hard Rock Stadium", "ville": "Miami", "diffusion": ["beIN Sports"]}
]

# Huitièmes de finale
huitiemes = [
    {"numero": 89, "date": "2026-07-04", "heure": "19:00", "phase": "Huitième de finale", "equipe_domicile": "V73", "equipe_exterieur": "V75", "stade": "NRG Stadium", "ville": "Houston", "diffusion": ["beIN Sports"]},
    {"numero": 90, "date": "2026-07-04", "heure": "23:00", "phase": "Huitième de finale", "equipe_domicile": "V74", "equipe_exterieur": "V77", "stade": "Lincoln Financial Field", "ville": "Philadelphia", "diffusion": ["beIN Sports"]},
    {"numero": 91, "date": "2026-07-05", "heure": "02:00", "phase": "Huitième de finale", "equipe_domicile": "V79", "equipe_exterieur": "V80", "stade": "Estadio Azteca", "ville": "Mexico", "diffusion": ["beIN Sports"]},
    {"numero": 92, "date": "2026-07-05", "heure": "22:00", "phase": "Huitième de finale", "equipe_domicile": "V76", "equipe_exterieur": "V78", "stade": "MetLife Stadium", "ville": "New York / East Rutherford", "diffusion": ["beIN Sports"]},
    {"numero": 93, "date": "2026-07-06", "heure": "14:00", "phase": "Huitième de finale", "equipe_domicile": "V81", "equipe_exterieur": "V82", "stade": "Lumen Field", "ville": "Seattle", "diffusion": ["beIN Sports"]},
    {"numero": 94, "date": "2026-07-06", "heure": "21:00", "phase": "Huitième de finale", "equipe_domicile": "V83", "equipe_exterieur": "V84", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["beIN Sports"]},
    {"numero": 95, "date": "2026-07-07", "heure": "18:00", "phase": "Huitième de finale", "equipe_domicile": "V86", "equipe_exterieur": "V88", "stade": "Mercedes-Benz Stadium", "ville": "Atlanta", "diffusion": ["beIN Sports"]},
    {"numero": 96, "date": "2026-07-07", "heure": "22:00", "phase": "Huitième de finale", "equipe_domicile": "V85", "equipe_exterieur": "V87", "stade": "BC Place", "ville": "Vancouver", "diffusion": ["beIN Sports"]}
]

# Quarts de finale
quarts = [
    {"numero": 97, "date": "2026-07-09", "heure": "22:00", "phase": "Quart de finale", "equipe_domicile": "V89", "equipe_exterieur": "V90", "stade": "Gillette Stadium", "ville": "Boston / Foxborough", "diffusion": ["beIN Sports"]},
    {"numero": 98, "date": "2026-07-10", "heure": "21:00", "phase": "Quart de finale", "equipe_domicile": "V93", "equipe_exterieur": "V94", "stade": "SoFi Stadium", "ville": "Los Angeles", "diffusion": ["beIN Sports"]},
    {"numero": 99, "date": "2026-07-11", "heure": "23:00", "phase": "Quart de finale", "equipe_domicile": "V91", "equipe_exterieur": "V92", "stade": "Hard Rock Stadium", "ville": "Miami", "diffusion": ["beIN Sports"]},
    {"numero": 100, "date": "2026-07-12", "heure": "03:00", "phase": "Quart de finale", "equipe_domicile": "V95", "equipe_exterieur": "V96", "stade": "Arrowhead Stadium", "ville": "Kansas City", "diffusion": ["beIN Sports"]}
]

# Demi-finales
demis = [
    {"numero": 101, "date": "2026-07-14", "heure": "20:00", "phase": "Demi-finale", "equipe_domicile": "V97", "equipe_exterieur": "V98", "stade": "AT&T Stadium", "ville": "Dallas / Arlington", "diffusion": ["M6", "beIN Sports"]},
    {"numero": 102, "date": "2026-07-15", "heure": "02:00", "phase": "Demi-finale", "equipe_domicile": "V99", "equipe_exterieur": "V100", "stade": "Mercedes-Benz Stadium", "ville": "Atlanta", "diffusion": ["M6", "beIN Sports"]}
]

# Petite finale
petite_finale = {"numero": 103, "date": "2026-07-18", "heure": "21:00", "phase": "Petite finale", "equipe_domicile": "P101", "equipe_exterieur": "P102", "stade": "Hard Rock Stadium", "ville": "Miami", "diffusion": ["M6", "beIN Sports"]}

# Finale
finale = {"numero": 104, "date": "2026-07-19", "heure": "21:00", "phase": "Finale", "equipe_domicile": "V101", "equipe_exterieur": "V102", "stade": "MetLife Stadium", "ville": "New York / East Rutherford", "diffusion": ["M6", "beIN Sports"]}

# Créer la structure JSON complète
calendrier = {
    "competition": "Coupe du Monde 2026",
    "dates": "11 juin - 19 juillet 2026",
    "pays_hotes": ["États-Unis", "Canada", "Mexique"],
    "total_matches": 104,
    "fuseau_horaire": "Europe/Paris (CEST)",
    "source": "coupedumonde2026.net",
    "derniere_mise_a_jour": "01/05/2026",
    "phases": {
        "phase_de_groupes": {
            "nombre_matches": 72,
            "dates": "11 juin - 28 juin 2026",
            "matches": phase_groupes
        },
        "phase_finale": {
            "nombre_matches": 32,
            "dates": "28 juin - 19 juillet 2026",
            "seiziemes_de_finale": {
                "nombre_matches": 16,
                "dates": "28 juin - 4 juillet 2026",
                "matches": seiziemes
            },
            "huitiemes_de_finale": {
                "nombre_matches": 8,
                "dates": "4 juillet - 7 juillet 2026",
                "matches": huitiemes
            },
            "quarts_de_finale": {
                "nombre_matches": 4,
                "dates": "9 juillet - 12 juillet 2026",
                "matches": quarts
            },
            "demi_finales": {
                "nombre_matches": 2,
                "dates": "14 juillet - 15 juillet 2026",
                "matches": demis
            },
            "petite_finale": petite_finale,
            "finale": finale
        }
    }
}

# Sauvegarder dans le fichier JSON
with open('calendrier-matches-2026.json', 'w', encoding='utf-8') as f:
    json.dump(calendrier, f, ensure_ascii=False, indent=2)

print("Fichier JSON cree avec succes!")
print(f"Total de matches extraits: {len(phase_groupes) + len(seiziemes) + len(huitiemes) + len(quarts) + len(demis) + 2}")

# Made with Bob
