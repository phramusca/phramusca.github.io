---
layout: default
---

# {{ page.title }}

{% for personne in site.data.donnees %}

- **Nom** : {{ personne.Nom }}
- **Âge** : {{ personne.Age }}
- **Ville** : {{ personne.Ville }}

{% endfor %}
