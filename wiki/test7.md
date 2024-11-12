---
layout: default
title: test 7
---

# {{ page.title }}

{% capture table_header %}
| Nom | Ubuntu-fr | Description | Installation |
| --- | --------- | ----------- | ------------ |
{% endcapture %}

{% for categorie in site.data.linux-programmes.categories %}
## {{ categorie.nom }}

{{ table_header }}
{% capture table_rows %}
{% for logiciel in categorie.logiciels %}
| {{ logiciel.Nom }} | [{{ logiciel.Nom }}]({{ logiciel.doc_ubuntu_fr_url }}) | {{ logiciel.description }} | [{{ logiciel.Nom }}]({{ logiciel.apt_url }}) |
{% endfor %}
{% endcapture %}
{{ table_rows }}

{% endfor %}
