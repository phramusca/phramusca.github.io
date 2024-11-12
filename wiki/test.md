---
layout: default
title: Liste des personnes
---

# Liste des personnes

{% for personne in site.data.donnees %}

- **Nom** : {{ personne.Nom }}
- **Âge** : {{ personne.Age }}
- **Ville** : {{ personne.Ville }}

{% endfor %}
