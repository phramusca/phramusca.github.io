---
layout: content
title: Programmes archivés
---

# {{ page.title }}

Cette page regroupe les programmes conservés à titre d'archive.

Ils ne figurent plus dans la [liste principale des programmes](../soft).

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const toggleButtons = document.querySelectorAll(".toggle-button");

    toggleButtons.forEach(button => {
      button.addEventListener("click", function () {
        const contentRow = this.closest("tr").nextElementSibling;

        if (contentRow.style.display === "none") {
          contentRow.style.display = "table-row";
          this.innerHTML = "-";
        } else {
          contentRow.style.display = "none";
          this.innerHTML = "+";
        }
      });
    });
  });
</script>

<table>
  <tbody>
    {% for categorie in site.data.soft_list.categories %}
      {% assign logiciels_archives = categorie.logiciels | where_exp: "logiciel", "logiciel.archive == true" %}
      {% if logiciels_archives.size > 0 %}
        <tr>
          <td colspan="4" style="text-align: center; color: #B5E852;"><strong>{{ categorie.nom }}</strong></td>
        </tr>
        {% include linux/soft/table.html software_list=logiciels_archives %}
      {% endif %}
      {% if categorie.categories != null %}
        {% for sous_categorie in categorie.categories %}
          {% assign logiciels_archives = sous_categorie.logiciels | where_exp: "logiciel", "logiciel.archive == true" %}
          {% if logiciels_archives.size > 0 %}
            <tr>
              <td colspan="4" style="color: #B5E852;"><strong>{{ categorie.nom }} — {{ sous_categorie.nom }}</strong></td>
            </tr>
            {% include linux/soft/table.html software_list=logiciels_archives %}
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  </tbody>
</table>
