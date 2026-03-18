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

Il existe plusieurs façons d'installer des programmes sous linux.

|                                                       | Description                                                                                                                 | Installation facile par URL                                                                    | Ligne de commande                                 | [Ubuntu](../dist/Ubuntu)                         | [Linux Mint](../dist/Mint)                                                                                                                                                                                   |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [APT](https://help.ubuntu.com/community/AptGet/Howto) | Paquets “classiques” de la distro (intégration système, libs/CLI/services).                                                 | [apt-url](../system/apturl), ex [apt://gimp](apt://gimp)                                       | `sudo apt install <pkg>`                          | ✅ Par défaut.                                   | ✅ Par défaut.                                                                                                                                                                                               |
| [AppImage](https://appimage.org/)                     | Un seul fichier exécutable, pas d’installation, pratique pour tester/épingler une version. Pas de sandbox par défaut.       | N/A. Pas d'installation.                                                                       | `chmod +x fichier.AppImage && ./fichier.AppImage` | ✅ Possible (téléchargement + `chmod +x`).       | ✅ Possible (téléchargement + `chmod +x`).                                                                                                                                                                   |
| [Flatpak](https://flatpak.org/)                       | Apps (surtout GUI) via Flathub, sandbox (portals/bubblewrap), bon cross-distro. Pas de `flatpak://` (plutôt `.flatpakref`). | [flathub.org](https://flathub.org), ex [Bruno](https://flathub.org/en/apps/com.usebruno.Bruno) | `flatpak install flathub <appID>`                 | ⚠️ Pas par défaut (à installer/configurer).    | ✅ Possible (souvent via la logithèque/Flathub).                                                                                                                                                             |
| [Snap](https://snapcraft.io/)                         | ⚠️ Format Ubuntu/Canonical avec Snap Store **propriétaire**. **Non recommandé !**                                         | [snap://bruno](snap://bruno)                                                                   | `sudo snap install <pkg>`                         | ✅ Par défaut (snapd et snap-store préinstallé). | ❌ [Désactivé par défaut](https://linuxmint-user-guide.readthedocs.io/en/latest/snap.html) (snapd verrouillé; nécessite déverrouillage + installation + ``snap install snap-store`` pour liens ``snap://``). |

TODO: Faire un repo pour ce .deb pour gerer **flatpak+https**
- flatpak
  - il n’y a pas de protocole `flatpak://`
  - le bouton « Install » sur [Flathub](https://flathub.org/) ouvre la logithèque si le type `.flatpakref` lui est associé, sinon le fichier se télécharge et on peut lancer `flatpak install ./xxx.flatpakref` ou `flatpak install https://flathub.org/repo/appstream/io.usebruno.Bruno.flatpakref`.
  - Si les pages « Install » Flathub (URL **flatpak+https**) ne font rien : [prendre en charge flatpak+https](../system/flatpak-url-handler).
  - Pour Ubuntu, y'a pas par défaut. A tester: https://www.reddit.com/r/Ubuntu/comments/1d68i68/installing_flatpak_on_ubuntu_2404/?tl=fr et https://flathub.org/fr/setup/Ubuntu

TODO: Supprimer la page ci-dessous
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
