---
layout: default
title: double boucle for
---

# {{ page.title }}

{% for categorie in site.data.linux-programmes.categories %}
# {{ categorie.nom }}

| Nom | Ubuntu-fr | Description | Installation [apturl](../system/Apt-url.md) |
| --- | --------- | ----------- | ------------------------------------------- |
|     |           |             |                                             |
{% for logiciel in categorie.logiciels %}
| {{ logiciel.Nom }} | [{{ logiciel.Nom }}]({{ logiciel.doc_ubuntu_fr_url }}) | {{ logiciel.description }} | [{{ logiciel.Nom }}]({{ logiciel.apt_url }}) |
{% endfor %}

{% endfor %}
