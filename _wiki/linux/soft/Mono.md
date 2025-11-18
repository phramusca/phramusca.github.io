---
layout: default
---

# Mono

Mono est obsolète. Dernière mise à jour en 2019.

Mono a été repris par Microsoft dans un fork et on peut faire du .NET sous linux avec Visual Code. 

Voici l'annonce sur le wiki:

> [!IMPORTANT]
> The [Mono Project (mono/mono)]( https://github.com/mono/mono) (‘original mono’) has been an important part of the .NET ecosystem since it was launched in 2001. Microsoft became the steward of the Mono Project when it acquired Xamarin in 2016.
>
> The last major release of the Mono Project was in July 2019, with minor patch releases since that time. The last patch release was February 2024.
>
> We are happy to announce that the WineHQ organization will be taking over as the stewards of the Mono Project upstream at [wine-mono / Mono · GitLab (winehq.org)](https://gitlab.winehq.org/wine-mono/mono).  Source code in existing [mono/mono](https://github.com/mono/mono) and other repos will remain available, although repos may be archived. Binaries will remain available for up to four years.
>
> Microsoft maintains a modern fork of [Mono runtime in the dotnet/runtime repo](https://github.com/dotnet/runtime/tree/main/src/mono) and has been progressively moving workloads to that fork. That work is now complete, and we recommend that active Mono users and maintainers of Mono-based app frameworks migrate to [.NET](https://github.com/dotnet/core) which includes work from this fork.
>
> We want to recognize that the Mono Project was the first .NET implementation on Android, iOS, Linux, and other operating systems. The Mono Project was a trailblazer for the .NET platform across many operating systems. It helped make cross-platform .NET a reality and enabled .NET in many new places and we appreciate the work of those who came before us.
>

Ce qui suit est pour archive:

--------------------------------

Mono est une mise en œuvre libre (sous licence GNU GPL, GNU LGPL ou X11 selon les éléments) de la plate-forme de développement Microsoft .NET basé sur la CLI. Mono a été initié par Miguel de Icaza au sein de sa société Ximian et est actuellement soutenu par Novell qui l'a rachetée en 2003.

Plus d'infos: <http://fr.wikipedia.org/wiki/Mono_(logiciel)>

## MonoDevelop

MonoDevelop est un IDE, similaire à Visual Studio de Microsoft

### Installation

- [MonoDevelop](apt://monodevelop,libmono-i18n2.0-cil,gtk-sharp2,mono-gmcs,mono-gac,mono-utils)
  ([Détail pour
  libmono-i18n2.0-cil](http://ubuntuforums.org/showthread.php?t=831409))
  (gtk-sharp2 depuis Ubuntu Lucid 10.04)
- [Librairie MySQL](apt://libmysql-cil-dev)
- [Documentation](apt://monodoc-browser,monodoc-mysql-manual,monodoc-gtk2.0-manual)
- [Contrôle de Version](apt://monodevelop-versioncontrol); permet
  d'utiliser entre autre [Subversion](Subversion).
- [Debugger](apt://monodevelop-debugger-mdb,monodevelop-debugger-gdb),
  pour version \>= 2.0 (linux/dist/Ubuntu \>= 9.04):

### Astuces

- Ajouter un répertoire existant dans un projet:
  - enable "Show All Files" (at the top of the solution explorer in VS).
  - The folder will be shown in grey (you might need to refresh, using
    the "Refresh" button near the "Show all files").
  - Right-mouse, "include in project".

- [Subversion](Subversion): **TODO**

## Documentation

- [Mono Project](http://mono-project.com/)
- [MonoDevelop](http://monodevelop.com)
- [Doc Ubuntu](http://doc.ubuntu-fr.org/monodevelop)
- [Portail francophone des utilisateurs de
  Mono](http://monofrance.tuxfamily.org/)
- [Référence Mono](http://www.go-mono.com/docs/)
- [Sharp ToolBox](http://sharptoolbox.com/) (A TESTER)

## Programmer

Cette section contient des exemples et des astuces pour MonoDevelop.

### SQL

- <http://www.mono-project.com/MySQL>
- <http://vincentlaine.developpez.com/tuto/dotnet/mono/>
- Cours VB.NET d'accord mais très complet (et facilement adaptable en
  C#):
  <http://plasserre.developpez.com/cours/vb-net/?page=bases-donnees1#LXVII-B-4>

### Gtk Widgets

#### Node View

Un NodeView est un TreeView simplifié.

- [Tutoriel](http://www.mono-project.com/GtkSharpNodeViewTutorial)

#### Tree View

- [Tutoriel](http://www.mono-project.com/GtkSharp_TreeView_Tutorial)
- [Tutoriel plus détaillé](http://www.mono-lab.ch/?p=22)
- [Un tutoriel plus complet, mais
  complexe](http://scentric.net/tutorial/treeview-tutorial.html)
- [DataBinding an IList as DataSource for the
  Gtk.TreeView](http://pvanhoof.be/blog/index.php/2006/04/21/databinding-an-ilist-as-datasource-for-the-gtktreeview)

### Librairies

- [TagLib
  Sharp](http://developer.novell.com/wiki/index.php/TagLib_Sharp) : .NET
  library capable of reading and writing both the basic and advanced
  tagging information stored in popular audio formats.

## Programmes

Voici un liste non exhaustive de programmes fait en Mono. **A TESTER !**
(pour voir si il ya des choses intéressantes à récupérer pour
inspiration)

- MonoCop, l'équivalent du FxCop qui permet de faire un "audit" de code
  et de vérifier de nombreuses règles personnalisables.
  (http://www.advogato.org/person/jluke/diary.html?start=24)
- MonoForge, un hébergeur de site web dédié à la plateforme Mono/Linux
  avec MySQL. Actuellement en phase de test, l'hébergement est gratuit
  pendant 1 an : <http://www.monoforge.com/>
- Gecko# marche sous Windows, il devient possible de faire un navigateur
  portable en GTK#.
  (http://primates.ximian.com/~miguel/pic.php?name=mozwin32.JPG&ca)
- Tomboy, un utilitaire intégré à GNome pour faciliter la prise de notes
  (http://www.beatniksoftware.com/tomboy/)
- Blam!, un agrégateur de news RSS intégré à Gnome
  (http://www.imendio.com/projects/blam/)
- F-Spot, un gestionnaire de photo pour Gnome
  (http://www.gnome.org/projects/f-spot/ , quelques jolis screenshot des
  futures focntionnalités par ici :
  <http://primates.ximian.com/~glesage/wiki/doku.php?id=f-spot>)
- iFolder3, une solution de partage de fichiers multi-plateforme, porté
  par Novell sur Mono.
  (http://forge.novell.com/modules/xfmod/project/?ifolder)
- Galaxium Messenger, un messenger compatible MSN
  (http://galaxium.sourceforge.net/)
- GLyrics, une application qui cherche toute seule comme une grande les
  paroles d'une chanson sur internet. S'intègre avec xmms.
  (http://zapdos.codemonkey.cl/glyrics/)
- Bless, un éditeur hexa (http://home.gna.org/bless/screenshots.html)
- Fewnn, une interface pour l'émulateur MAME
  (http://people.mmgsecurity.com/~lorenb/fewnn/)
- MonkeyPop, une application qui permet d'afficher des notifications en
  HTML ou SVG sous Gnome
  (http://mspace.berlios.de/gunther-user/view.php/page/MonkeyPop)
- ADP, un provider de Base de données compatible SQLServer, Oracle,
  Firebird, Sqlite, Postgres et Mysql.
  (http://advanced-ado.sourceforge.net/)
- GFax, un front-end de gestionnaires de fax pour Gnome
  (http://gfax.cowlug.org/)
- Muine, un player audio (http://muine-player.org/wiki/Main_Page)

------------------------------------------------------------------------

Retour à [Programmes](Programmes)
