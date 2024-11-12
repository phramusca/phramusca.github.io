---
layout: default
title: double boucle for
---

# {{ page.title }}

{% for categorie in site.data.linux-programmes.categories %}
## {{ categorie.nom }}

{% capture table_rows %}
{% for logiciel in categorie.logiciels %}
| {{ logiciel.Nom }} | [{{ logiciel.Nom }}]({{ logiciel.doc_ubuntu_fr_url }}) | {{ logiciel.description }} | [{{ logiciel.Nom }}]({{ logiciel.apt_url }}) |
{% endfor %}
{% endcapture %}

| Nom | Ubuntu-fr | Description | Installation |
| --- | --------- | ----------- | ------------ |
{{ table_rows }}

{% endfor %}
