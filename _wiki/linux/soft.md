---
layout: content
title: Programmes
exclude_search_sections: true
---

# {{ page.title }}

{:.no_toc}

## Prérequis pour les liens d'installation rapide

| Type de lien                      | Prérequis                                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `apt-thirdparty://`               | [apt-thirdparty-handler](https://github.com/phramusca/apt-thirdparty-handler/releases/latest) (par moi-même) |
| `flathub://` (`flatpak+https://`) | [flatpak-https-handler](https://github.com/phramusca/flatpak-https-handler/releases/latest) (par moi-même)   |
| `apt://`                          | Généralement natif                                                                                           |

## Sur le Web

{:.no_toc}

Il existe énormément de sites qui listent ou proposent des logiciels
pour [Linux](../). En voici une petite sélection:

- [Logiciels pour Ubuntu](http://doc.ubuntu-fr.org/logiciels) sur Ubuntu-fr - Pour [Linux Mint](../dist/mint), choisir les versions [Ubuntu](../dist/ubuntu) (Gonme) qui sont compatibles et mieux integrées que les logiciels pour Kubuntu (KDE).
- [Alternativeto.net](http://alternativeto.net/) (Anglais) - Trouver des équivalences de programmes. Très utile et pratique !
- [Framasoft](http://www.framasoft.net/) - Association française qui promeut des alternatives libres et éthiques aux services en ligne, notamment en développant et en soutenant des logiciels libres et des outils collaboratifs pour préserver la vie privée et favoriser l'autonomie numérique.

Pour plus d'informations sur l'installation des applications sur Linux, vous pouvez consulter les guides suivants :

- [Installer une application sur Linux Mint](https://www.numetopia.fr/comment-installer-des-applications-sur-linux-mint/).
- [Installer une application sur Ubuntu](https://doc.ubuntu-fr.org/installer_une_application).

## Ma Sélection

{:.no_toc}

Voici un petit aperçu des programmes disponibles que j'ai eu l'occasion de tester, et que j'apprécie, ainsi que des astuces (installation, problèmes connus,...).

Les programmes sont distribués sous [différents formats](../system/soft_packages/), chacun avec ses avantages et ses limites.

Les programmes archivés sont disponibles sur la page [Programmes archivés](../soft_archive).

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
      {% assign logiciels_actifs = categorie.logiciels | where_exp: "logiciel", "logiciel.archive != true" %}
      {% if logiciels_actifs.size > 0 %}
        <tr>
          <td colspan="4" style="text-align: center; color: #B5E852;"><strong>{{ categorie.nom }}</strong></td>
        </tr>
        {% include linux/soft/table.html software_list=logiciels_actifs %}
      {% endif %}
      {% if categorie.categories != null %}
        {% for sous_categorie in categorie.categories %}
          {% assign logiciels_actifs = sous_categorie.logiciels | where_exp: "logiciel", "logiciel.archive != true" %}
          {% if logiciels_actifs.size > 0 %}
            <tr>
              <td colspan="4" style="color: #B5E852;"><strong>{{ sous_categorie.nom }}</strong></td>
            </tr>
            {% include linux/soft/table.html software_list=logiciels_actifs %}
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  </tbody>
</table>
