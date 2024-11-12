---
layout: default
title: Programmes
---

# {{ page.title }}

Il existe des centaines (voire des milliers) d'applications disponible sous [Linux](../README.md). Il n'est pas facile de s'y retrouver, mais voici déjà un point de départ.

## Sur le Web

Il existe énormément de sites qui listent ou proposent des logiciels
pour [Linux](../README.md). En voici une petite sélection:

- [Logiciels pour Ubuntu](http://doc.ubuntu-fr.org/logiciels) sur Ubuntu-fr - Pour [Linux Mint](../dist/Mint.md), choisir les versions [Ubuntu](../dist/Ubuntu.md) (Gonme) qui sont compatibles et mieux integrées que les logiciels pour Kubuntu (KDE).
- [Alternativeto.net](http://alternativeto.net/) (Anglais) - Trouver des équivalences de programmes. Très utile et pratique !
- [Framasoft](http://www.framasoft.net/) - Association française qui promeut des alternatives libres et éthiques aux services en ligne, notamment en développant et en soutenant des logiciels libres et des outils collaboratifs pour préserver la vie privée et favoriser l'autonomie numérique.

## Ma Sélection

Voici un petit aperçu des programmes disponibles que j'ai eu l'occasion de tester, et que j'apprécie, ainsi que des astuces (installation, problèmes connus,...).

La plupart s'installent en un click avec les liens [apt-url](../system/apturl).

> Comment [Installer un programme sous Linux](../system/Installer_un_programme_sous_Linux.md) ?

### Applications

{% for categorie in site.data.linux.soft.list.categories %}

#### {{ categorie.nom }}

<table>
  <thead>
    <tr>
      <th>Nom</th>
      <th>Apt Url</th>
      <th>Ubuntu-fr</th>
      <th>Site</th>
      <th>Repo</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    {% for logiciel in categorie.logiciels %}
    <tr>
      <td>{% if logiciel.url_internal %}<a href="{{ logiciel.url_internal }}">{{ logiciel.nom }}</a>{% else %}{{ logiciel.nom }}{% endif %}</td>
      <td>{% if logiciel.apt %}<a href="apt://{{ logiciel.apt }}">{{ logiciel.apt }}</a>{% else %}N/A{% endif %}</td>
      <td><a href="{{ logiciel.url_doc_ubuntu_fr }}">{{ logiciel.nom }}</a></td>
      <td><a href="{{ logiciel.url_website }}">{{ logiciel.nom }}</a></td>
      <td><a href="{{ logiciel.url_repository }}">{{ logiciel.nom }}</a></td>
      <td>{{ logiciel.description }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

{% endfor %}
