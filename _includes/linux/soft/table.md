{% for logiciel in {{include.software_list}} %}
{% capture url_internal %}<a href="soft?name={{ logiciel.nom }}">{{ logiciel.nom }}</a>{% endcapture %}
- {{ url_internal }} -- {{ logiciel.description }}
{% endfor %}