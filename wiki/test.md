---
layout: default
title: Mon nouveau titre dynamique
---

# {{ page.title }}

{% for personne in site.data.donnees %}
{% if personne.Nom %}
- **Nom** : {{ personne.Nom }}
{% endif %}
{% if personne.Age %}
- **Âge** : {{ personne.Age }}
{% endif %}
{% if personne.Ville %}
- **Ville** : {{ personne.Ville }}
{% endif %}
{% endfor %}
