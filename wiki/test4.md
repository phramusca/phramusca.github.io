---
layout: default
title: double boucle for
---

<h1>{{ page.title }}</h1>

{% for categorie in site.data.votre_fichier_yaml.categories %}
<h2>{{ categorie.nom }}</h2>

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
