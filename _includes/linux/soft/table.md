{% for logiciel in {{include.software_list}} %}
{% capture url_internal %}<a href="detail?name={{ logiciel.nom }}">{{ logiciel.nom }}</a>{% endcapture %}
- {{ url_internal }} -- {{ logiciel.description }}
{% endfor %}