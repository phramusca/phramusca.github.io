Windows est un système d'exploitation (OS) qui se distingue de
[Linux](Linux "wikilink") principalement par le fait d'être propriétaire
(non libre) et par conséquent payant (Microsoft, son éditeur n'étant pas
philanthrope). Bien d'autres différences fondamentales (ou moins)
existent entre les 2 mondes, que je ne détaillerais pas ici, mais voici
quelques pistes:

- <http://www.framablog.org/index.php/post/2008/09/02/differences-entre-linux-et-windows>
- <http://www.commentcamarche.net/faq/7283-linux-n-est-pas-windows>

# Logiciels

## Libres

Bien que Windows ne soit pas libre, il existe cependant de nombreuses
application libres (open source) sous Windows (souvent portée depuis le
monde [Linux](Linux "wikilink").

Voici quelques sites pour trouver des équivalences:

- <http://www.misfu.com/equivalence-logiciels-windows-linux.html>
- <http://lesalternatives.free.fr/>
- <http://alternativeto.net/>

Et voici quelques exemples qui me paraissent intéressants:

|  |  |  |
|----|----|----|
| Site internet | Description | Semblable à |
| [wxchecksums](http://wxchecksums.sourceforge.net/) | Création de checksums (MD5, SHA-1,...) |  |
| [GIMP](http://www.gimp.org/) | Gnu Image Manipulation Program | Adobe Photoshop |
| [Sumatra PDF](http://blog.kowalczyk.info/software/sumatrapdf/) | Visionneuse de fichiers PDF | Adobe Reader (anciennement Acrobat Reader) |

## Gratuits

Voici des logiciels utiles, gratuits, mais pas libres.

|  |  |  |
|----|----|----|
| Site internet | Description | Semblable à |
| [Auslogics Disk Defrag](http://www.auslogics.com/en/software/disk-defrag/) | Défragmenteur de disques. Bien plus efficace et complet que celui par défaut de Windows. | Défragmenteur de disque Windows |
| [Page Defrag](http://www.commentcamarche.net/download/telecharger-248-pagedefrag/) | Défragmenteur de fichiers systèmes. Le défragmenteur de Windows, ni même les autres alternatives ne peuvent défragmenter les fichiers systèmes (swap, base de registre). Ce petit utilitaire, fourni par Microsoft le fait. | Aucun |
| [IceTeaReplacer](http://www.icetear.com/en/menu/home/) | Permet de rechercher (et de remplacer) du texte dans des fichiers Word 2007(docx), Excel 2007(xlsx) et Excel 2003(xls) contenus dans un répertoire donné. | Aucun |

# Trucs et Astuces

<table>
<tbody>
<tr>
<td><p>Logiciel</p></td>
<td><p>Astuce</p></td>
<td><p>Détails</p></td>
</tr>
<tr>
<td><p>Excel (Microsoft Office)</p></td>
<td><p>Listes de validation</p></td>
<td><p><a
href="http://www.excel-downloads.com/forum/81047-excel-liste-de-validation-dans-une-cellule.html">http://www.excel-downloads.com/forum/81047-excel-liste-de-validation-dans-une-cellule.html</a></p></td>
</tr>
<tr>
<td><p>Excel (Microsoft Office)</p></td>
<td><p>Ouvrir Excel dans des instances différentes</p></td>
<td><p>Open registry HKEY_CLASSES_ROOT =&gt; Excel.Sheet.8 =&gt; Shell
=&gt; Open =&gt; Command</p>
<p>The (default) value will be something like this:</p>
<p>"C:\Program Files (x86)\Microsoft Office\Office12\EXCEL.EXE" /e</p>
<p>And you'll want to append a "%1" to the end of that, making it:</p>
<p>"C:\Program Files (x86)\Microsoft Office\Office12\EXCEL.EXE" /e
"%1"</p>
<p>Delete or rename the command key, which is right below the (Default)
key</p>
<p>Delete or rename the DDEexec key</p>
<p>Excel.Sheet.8 =&gt; Excel 97-2003 file type.</p>
<p>Excel.Sheet.12 =&gt; Excel 2007 files</p></td>
</tr>
<tr>
<td><p>Excel (Microsoft Office)</p></td>
<td><p>copy every visible worksheet in a new workbook and save the
workbook with the name of the sheet in a newly created folder in the
same path as the workbook with this macro</p></td>
<td><p><a
href="http://www.rondebruin.nl/copy6.htm">http://www.rondebruin.nl/copy6.htm</a></p></td>
</tr>
<tr>
<td><p>Windows</p></td>
<td><p>Liens symboliques</p></td>
<td><p><a
href="http://technet.microsoft.com/fr-fr/sysinternals/bb896768%28en-us%29.aspx">http://technet.microsoft.com/fr-fr/sysinternals/bb896768%28en-us%29.aspx</a></p></td>
</tr>
<tr>
<td><p>Windows</p></td>
<td><p>Config réseau</p></td>
<td><p>en ligne de commande: netsh ex: netsh interface ip set address
name="<nomDeLaConnexion>" static 172.26.175.218 255.255.255.0 none</p>
<p>Plus d'infos: <a
href="http://fr.wikipedia.org/wiki/Netsh">http://fr.wikipedia.org/wiki/Netsh</a></p></td>
</tr>
<tr>
<td><p>GIMP</p></td>
<td><p>Masquer le dossier gegl dans Mes Documents (ATTRIB)</p></td>
<td><p><a
href="http://www.commentcamarche.net/forum/affich-15193901-supprimer-le-dossier-gegl-0-0">http://www.commentcamarche.net/forum/affich-15193901-supprimer-le-dossier-gegl-0-0</a></p></td>
</tr>
<tr>
<td><p>Outlook (Microsoft Office)</p></td>
<td><p>Fichier NK2 (fichier qui stocke les adresses de la saisie
automatique)</p></td>
<td><p>Le fichier se trouve ici: Documents and
settings\<User>\Application Data\Microsoft\Outlook Un éditeur: <a
href="http://www.nirsoft.net/utils/outlook_nk2_edit.html">http://www.nirsoft.net/utils/outlook_nk2_edit.html</a></p></td>
</tr>
<tr>
<td><p>Nokia OVI Suite</p></td>
<td><p>Exportation des contacts</p></td>
<td><p>Utiliser "Grab My Contacts" sous: <a
href="http://www.zodus.tk/">http://www.zodus.tk/</a></p></td>
</tr>
<tr>
<td><p>Firefox</p></td>
<td><p>Comment limiter l’utilisation de mémoire RAM?</p></td>
<td><p><a
href="http://ceclair.fr/deboguer-firefox-comment-limiter-lutilisation-de-memoire-ram">http://ceclair.fr/deboguer-firefox-comment-limiter-lutilisation-de-memoire-ram</a></p></td>
</tr>
<tr>
<td><p>Google Desktop</p></td>
<td><p>Changer l'emplacement du répertoire “Google Desktop Data” (par
défaut dans "Mes Documents")</p></td>
<td><p><a
href="http://www.vanachteren.net/2008/02/16/how-to-change-the-default-google-desktop-data-index-folder/">http://www.vanachteren.net/2008/02/16/how-to-change-the-default-google-desktop-data-index-folder/</a></p></td>
</tr>
</tbody>
</table>