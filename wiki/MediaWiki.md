# MediaWiki

[MediaWiki](http://www.mediawiki.org/wiki/MediaWiki/fr) est un des
nombreux Wiki open-source disponible sur la toile. Facile à mettre en
place (meme sur Free), en suivant les instructions sur le site de
[MediaWiki](http://www.mediawiki.org/wiki/MediaWiki/fr).

## Configuration

<http://www.mediawiki.org/wiki/Manual:Configuration>

### Change logo

- Dans LocalSettings.php, add the line (à la fin):



    $wgLogo = "{$wgScriptPath}/business_news.png";

### Autres types d'URL

<http://www.mediawiki.org/wiki/Manual:$wgUrlProtocols>

Par exemple, pour autoriser les liens comme <apt://> à être reconnus
comme des liens hypertextes, il faut rajouter la ligne suivante dans
LocalSettings.php:

    $wgUrlProtocols[] = "apt:";

### Anti-SPAM

- <http://bima.astro.umd.edu/wiki/index.php/Mediawiki_spam_protection>
- <http://www.mediawiki.org/wiki/Manual:Combating_spam>

## Extensions

### Syntax Highlighter

J'utilise maintenant, pour mettre du code source, un [Syntax
Highlighter](http://alexgorbatchev.com/wiki/SyntaxHighlighter).

[Source du tutoriel
(anglais)](http://www.lastengine.com/syntax-highlighter-code-colorizer-mediawiki/)

#### Installation

Pour le mettre en place, rien de plus simple:

- Télécharger et de-zipper dans le répertoire /extensions de MediaWiki
  le ZIP :
  <http://www.lastengine.com/wp-content/uploads/2009/04/syntax-highlighter-code-colorizer.zip>
- Dans LocalSettings.php, ajouter la ligne suivante (à la fin):

    `require_once("extensions/syntax-highlighter-code-colorizer/syntax-highlighter-mediawiki.php");`

#### Utilisation

- Une fois l'extension installée, pour l'utiliser, il suffit d'entourer
  le code à mettre en valeur avec:

`<pre class="brush:[code-alias]"> Ton code ici </pre>`

- [Liste des "code-alias"
  utlisables](http://alexgorbatchev.com/wiki/SyntaxHighlighter:Brushes)
- Par exemple, pour mettre du code PHP:

`<pre class="brush:php"> Ton code PHP ici </pre>`

------------------------------------------------------------------------

Retour à l'[Accueil](README)
