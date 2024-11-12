---
layout: default
---

<table>
  <thead>
    <tr>
      <th>Nom</th>
      <th>Age</th>
      <th>Ville</th>
    </tr>
  </thead>
  <tbody>
    {% for personne in site.data.donnees %}
    <tr>
      <td>{{ personne.Nom }}</td>
      <td>{{ personne.Age }}</td>
      <td>{{ personne.Ville }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
