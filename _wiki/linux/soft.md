---
layout: content
title: Programmes
exclude_search_sections: true
---

# {{ page.title }}

{:.no_toc}

Il existe des centaines (voire des milliers) d'applications disponible sous [Linux](../). Il n'est pas facile de s'y retrouver, mais voici déjà un point de départ.

- [Installer une application sur Linux Mint](https://www.numetopia.fr/comment-installer-des-applications-sur-linux-mint/).
- [Installer une application sur Ubuntu](https://doc.ubuntu-fr.org/installer_une_application).

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

|                                                                                           | Store                                                   | Description                                                                                                                  | Installation facile par URL                                                                    | Ligne de commande                                                     | [Ubuntu](../dist/Ubuntu)                                                             | [Linux Mint](../dist/Mint)                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [APT](https://salsa.debian.org/apt-team/apt) ([ubuntu-fr](https://doc.ubuntu-fr.org/apt)) | Selon OS.                                               | Paquets “classiques” pour les [distributions Linux basées sur Debian](../#distributions-basées-sur-debian-linux-mint-ubuntu) | [apt-url](../system/apturl), ex [apt://gimp](apt://gimp)                                       | `sudo apt install <pkg>`                                              | ✅ Par défaut.                                                                       | ✅ Par défaut.                                                                                                                                                                                               |
| [AppImage](https://appimage.org/) ([ubuntu-fr](https://doc.ubuntu-fr.org/appimage))       | N/A                                                     | Un seul fichier exécutable, pratique pour tester une version.        | N/A. Pas d'installation.                                                                       | `chmod +x fichier.AppImage && ./fichier.AppImage`                     | ✅ Possible (téléchargement + `chmod +x`).                                           | ✅ Possible (téléchargement + `chmod +x`).                                                                                                                                                                   |
| [Flatpak](https://flatpak.org/) ([ubuntu-fr](https://doc.ubuntu-fr.org/flatpak))          | [Flathub](https://flathub.org) ou autres.               | Apps (surtout GUI) via Flathub, sandbox (portals/bubblewrap), bon cross-distro. Pas de `flatpak://` (plutôt `.flatpakref`).  | [flathub.org](https://flathub.org), ex [Bruno](https://flathub.org/en/apps/com.usebruno.Bruno) | `flatpak install flathub <appID>`                                     | ⚠️ Pas par défaut (à [installer/configurer](https://flathub.org/fr/setup/Ubuntu)). | ✅ Possible (via la logithèque/Flathub).                                                                                                                                                             |
| [Snap](https://snapcraft.io/) ([ubuntu-fr](https://doc.ubuntu-fr.org/flatpak))            | [Snap Store](https://snapcraft.io/store) exclusivement. | ⚠️ Format Ubuntu/Canonical avec Snap Store **propriétaire**. **Non recommandé !**                                          | [snap://bruno](snap://bruno)                                                                   | `sudo snap install <pkg>`                                             | ✅ Par défaut (snapd et snap-store préinstallé).                                     | ❌ [Désactivé par défaut](https://linuxmint-user-guide.readthedocs.io/en/latest/snap.html) (snapd verrouillé; nécessite déverrouillage + installation + ``snap install snap-store`` pour liens ``snap://``). |
| Compiler les sources                                                                      | N/A                                                     | Rarement utilisé. [Tutoriel compilation](http://doc.ubuntu-fr.org/tutoriel/compilation)                                      | N/A                                                                                            | [Tutoriel compilation](http://doc.ubuntu-fr.org/tutoriel/compilation) | ✅ Possible                                                                          | ✅ Possible                                                                                                                                                                                                  |

### Applications

{:.no_toc}

- TOC
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
