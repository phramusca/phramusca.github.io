{% for logiciel in {{include.software_list}} %}
    
      {% capture url_internal %}
      {% if logiciel.url_internal %}<a href="{{ logiciel.url_internal }}">{{ logiciel.nom }}</a>{% else %}{{ logiciel.nom }}{% endif %}
      {% endcapture %}

      {% capture apt %}
      {% if logiciel.apt %}<a href="apt://{{ logiciel.apt }}">apt://{{ logiciel.apt }}</a>{% endif %}
      {% endcapture %}

      {% capture url_doc_ubuntu_fr %}
      {% if logiciel.url_doc_ubuntu_fr %}<a href="{{ logiciel.url_doc_ubuntu_fr }}">{{ logiciel.nom }}</a>{% endif %}
      {% endcapture %}

      {% capture url_website %}
      {% if logiciel.url_website %}<a href="{{ logiciel.url_website }}">{{ logiciel.nom }}</a>{% endif %}
      {% endcapture %}

      {% capture url_repository %}
      {% if logiciel.url_repository %}<a href="{{ logiciel.url_repository }}">{{ logiciel.nom }}</a>{% endif %}
      {% endcapture %}

- {{ url_internal }} ({{ logiciel.description }})
    - Installation: {{ apt }}
    - Untutu-fr: {{ url_doc_ubuntu_fr }} 
    - Website: {{ url_website }}
    - Code source: {{ url_repository }}
{% endfor %}