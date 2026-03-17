---
layout: content
title: Programmes
exclude_search_sections: true
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

Pour tester:

[apt://bruno](apt://bruno)

[snap://bruno](snap://bruno)

[Bruno en Flatpak](https://flathub.org/en/apps/com.usebruno.Bruno) (ou [install direct](https://dl.flathub.org/repo/appstream/com.usebruno.Bruno.flatpakref))

- apt
  - s'installe direct avec les liens [apt-url](../system/apturl), ex apt://nomDuProgramme
- snap: Canonical/Ubuntu propriétaire. Désactivé par défaut dans Mint
  - [Ubuntu](../dist/Ubuntu): snap est disponible par défaut.
  - [Linux Mint](../dist/Mint):
    - <https://linuxmint-user-guide.readthedocs.io/en/latest/snap.html>

      ```bash
      # Remove the lock
      sudo rm /etc/apt/preferences.d/nosnap.pref 
      # Update apt
      sudo apt update
      # Install snapd (snap deamon)                       
      sudo apt install snapd
      # Install snap store (qui est un snap) pou pouvoir ouvrir les liens snap://
      snap install snap-store
      ```

    - Voir si on peut se passer du snap-store: <https://doc.ubuntu-fr.org/utilisateurs/amiralgaby/snap_parametrage_avance>
- flatpak
  - il n’y a pas de protocole `flatpak://`
  - le bouton « Install » sur [Flathub](https://flathub.org/) ouvre la logithèque si le type `.flatpakref` lui est associé, sinon le fichier se télécharge et on peut lancer `flatpak install ./xxx.flatpakref` ou `flatpak install https://flathub.org/repo/appstream/io.usebruno.Bruno.flatpakref`.
  - Si les pages « Install » Flathub (URL **flatpak+https**) ne font rien : [prendre en charge flatpak+https](../system/flatpak-url-handler).
  - Pour Ubuntu, y'a pas par défaut. A tester: https://www.reddit.com/r/Ubuntu/comments/1d68i68/installing_flatpak_on_ubuntu_2404/?tl=fr et https://flathub.org/fr/setup/Ubuntu

> Comment [Installer un programme sous Linux](../system/Installer_un_programme_sous_Linux) ?

### Applications
{:.no_toc}

* TOC
{:toc}

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
      {% if categorie.logiciels != null or categorie.categories != null%}
        <tr>
          <td colspan="4" style="text-align: center; color: #B5E852;"><strong>{{ categorie.nom }}</strong></td>
        </tr>
        {% include linux/soft/table.html software_list=categorie.logiciels %}
      {% endif %}
      {% if categorie.categories != null %}
        {% for sous_categorie in categorie.categories %}
          <tr>
            <td colspan="4" style="color: #B5E852;"><strong>{{ sous_categorie.nom }}</strong></td>
          </tr>
          {% include linux/soft/table.html software_list=sous_categorie.logiciels %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  </tbody>
</table>
