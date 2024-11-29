---
layout: default
title: Programmes
---

# {{ page.title }}
{:.no_toc}

Il existe des centaines (voire des milliers) d'applications disponible sous [Linux](../). Il n'est pas facile de s'y retrouver, mais voici déjà un point de départ.

## Sur le Web
{:.no_toc}

Il existe énormément de sites qui listent ou proposent des logiciels
pour [Linux](../). En voici une petite sélection:

- [Logiciels pour Ubuntu](http://doc.ubuntu-fr.org/logiciels) sur Ubuntu-fr - Pour [Linux Mint](../dist/Mint), choisir les versions [Ubuntu](../dist/Ubuntu) (Gonme) qui sont compatibles et mieux integrées que les logiciels pour Kubuntu (KDE).
- [Alternativeto.net](http://alternativeto.net/) (Anglais) - Trouver des équivalences de programmes. Très utile et pratique !
- [Framasoft](http://www.framasoft.net/) - Association française qui promeut des alternatives libres et éthiques aux services en ligne, notamment en développant et en soutenant des logiciels libres et des outils collaboratifs pour préserver la vie privée et favoriser l'autonomie numérique.

## Ma Sélection
{:.no_toc}

Voici un petit aperçu des programmes disponibles que j'ai eu l'occasion de tester, et que j'apprécie, ainsi que des astuces (installation, problèmes connus,...).

La plupart s'installent en un click avec les liens [apt-url](../system/apturl).

> Comment [Installer un programme sous Linux](../system/Installer_un_programme_sous_Linux) ?

### Applications
{:.no_toc}

* TOC
{:toc}

{% for categorie in site.data.soft_list.categories %}

#### {{ categorie.nom }}

  {% if categorie.categories != null %}
    {% for sous_categorie in categorie.categories %}

##### {{ sous_categorie.nom }}

{% include linux/soft/table software_list=sous_categorie.logiciels %}

    {% endfor %}
  {% else %}

{% include linux/soft/table software_list=categorie.logiciels %}

  {% endif %}

{% endfor %}
