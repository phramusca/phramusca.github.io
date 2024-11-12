---
layout: default
title: double boucle for
---

# {{ page.title }}

{% for categorie in site.data.linux-programmes.categories %}
## {{ categorie.nom }}

<table>
  <thead>
    <tr>
      <th>Nom</th>
      <th>Ubuntu-fr</th>
      <th>Description</th>
      <th>Installation</th>
    </tr>
  </thead>
  <tbody>
    {% for logiciel in categorie.logiciels %}
    <tr>
      <td>{{ logiciel.Nom }}</td>
      <td><a href="{{ logiciel.doc_ubuntu_fr_url }}">{{ logiciel.Nom }}</a></td>
      <td>{{ logiciel.description }}</td>
      <td><a href="{{ logiciel.apt_url }}">{{ logiciel.Nom }}</a></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

{% endfor %}
