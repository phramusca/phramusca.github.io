# Java

J'utilise pour ma part NetBeans comme IDE (un autre équivalent est le
bien connu Eclipse, que je ne connais que très peu)

## Généralités

- Developpez.com (tutoriels, outils, api,...) :
  <http://java.developpez.com/>
- Cours bien complet:
  <http://www.siteduzero.com/tutoriel-3-10601-programmation-en-java.html>
- Cours, un autre: <http://prevert.upmf-grenoble.fr/Prog/>
- Ubuntu.fr: <http://doc.ubuntu-fr.org/java>

- Verify the Java Version

    `java -version`

- Check Installed Java Versions

  `update-alternatives --config java`

- Set the Default Java Version

  `sudo update-alternatives --config java`

## Log

- <http://imss-www.upmf-grenoble.fr/prevert/Prog/Java/CoursJava/fichierDeLogs.html>
- <http://cyberzoide.developpez.com/java/logging/>

## Librairies

| Nom                              | Description                                                   | Documentation                                                                                                                                                     | Download                                                                                           |
|----------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| SQLite JDBC Driver               | SQLite                                                        |                                                                                                                                                                 | [https://bitbucket.org/xerial/sqlite-jdbc](https://bitbucket.org/xerial/sqlite-jdbc)             |
| MySQL Connector/J                | MySQL                                                         | - [Tutoriel](http://www.fobec.com/CMS/java/tutorial/connecter-une-base-mysql-avec-driver-jdbc_943.html)<br>- [NetBeans tuto](http://fr.netbeans.org/edi/articles/concours/mysql-client.html) | [http://dev.mysql.com/downloads/connector/j/5.1.html](http://dev.mysql.com/downloads/connector/j/5.1.html) |
| Apache Commons Net              | FTP, Telnet, POP3, FTP, SMTP, ...                           | - [Exemples](http://www.informit.com/guides/content.aspx?g=java&amp;seqNum=40)<br>- [Exemple upload/download FTP](http://www.developpez.net/forums/d627242/java/general-java/debuter/connexion-java-ftp/)<br>- [FTP Binary mode](http://www.developpez.net/forums/d590818/java/general-java/apis/io/envoi-ftp-fichier-excel-org-apache-commons-net-ftp/) | [http://commons.apache.org/net/download_net.cgi](http://commons.apache.org/net/download_net.cgi) |
| JSch - Java Secure Channel       | SSH                                                           | - [Create InputStream](http://www.java-forums.org/new-java/10195-creating-inputstream.html)                                                                     | [http://www.jcraft.com/jsch/](http://www.jcraft.com/jsch/)                                       |
| javax.comm                       | Ports Série (serial port)                                    | - [Tutoriel](http://christophej.developpez.com/tutoriel/java/javacomm/)<br>- [Tuto en anglais - utile ?](http://en.wikibooks.org/wiki/Serial_Programming/Serial_Java)<br>- [Windows Installation Guide](http://circuitnegma.wordpress.com/2007/02/07/how-to-install-the-java-communications-api-in-a-windows-environment/) |                                                                                                    |
| [Jaudiotagger](http://www.jthink.net/jaudiotagger/) | MP3 ID3 tag (2011-?)                                        | *Autres librairies (outdated)* :<br>- [mp3agic](https://github.com/mpatric/mp3agic) (2010-2011)<br>- [JLayer](http://www.javazoom.net/javalayer/javalayer.html) (1999-2008)<br>- [javamp3](http://developer.berlios.de/projects/javamp3/) (2004-2008)<br>- [myid3](http://www.fightingquaker.com/myid3/) (2007-2008)<br>- [entagged](http://entagged.sourceforge.net/developer.php) (2003-2006)<br>- [javamusictag](http://javamusictag.sourceforge.net/) (2003-2006)<br>- [jid3](http://jid3.blinkenlights.org/) (? - 2005) | [Maven .jar builds](http://download.java.net/maven/2/org/jaudiotagger)                              |
| [Java Excel API](http://jexcelapi.sourceforge.net/) (jxl) | Excel                                                        | - [Tutoriel](http://www.vogella.com/articles/JavaExcel/article.html) <em>A tester</em> : [http://poi.apache.org/](http://poi.apache.org/)                                              |                                                                                                    |
| [lastfm-java](http://code.google.com/p/lastfm-java/)  | Last.fm API bindings for Java                                 |                                                                                                                                                                 |                                                                                                    |
| [JLayer](http://www.javazoom.net/javalayer/javalayer.html) | MP3 decoder/player/converter library for Java™ platform.     |                                                                                                                                                                 |                                                                                                    |
| [ini4j](http://ini4j.sourceforge.net/) | Java API for handling Windows ini file format               |                                                                                                                                                                 |                                                                                                    |
| [jCharts](http://jcharts.sourceforge.net/) | Charts                                                        | See also: [JFreeChart](http://www.jfree.org/jfreechart/) (a tester, plus compliqué mais plus puissant apparemment)                                            |                                                                                                    |
| [coverartarchive-api](https://github.com/lastfm/coverartarchive-api) | MusicBrainz Cover Art Archive API                             | To use a proxy: First, make DefaultCoverArtArchiveClient(HttpClient client) public in DefaultCoverArtArchiveClient class<br>Then:<br>  ```DefaultHttpClient httpclient = new DefaultHttpClient();<br>HttpHost proxy = new HttpHost("xx.xx.xx.xx", 8080);<br>httpclient.getParams().setParameter(ConnRoutePNames.DEFAULT_PROXY, proxy);<br>CoverArtArchiveClient client = new DefaultCoverArtArchiveClient(httpclient);``` |                                                                                                    |
| [musicbrainzws2-java](http://code.google.com/p/musicbrainzws2-java/) | Java binding for MusicBrainz XML Web Service/Version 2      | *Autres librairies (to be tested)* :<br>- [musicbrainz-data](https://github.com/lastfm/musicbrainz-data) (Need to learn more about Spring framework and eventually Maven: [forum issue](https://github.com/lastfm/musicbrainz-data/issues/2)) (<a href="https://oss.sonatype.org/index.html#view-repositories;releases~browsestorage~/fm/last/musicbrainz-data/1.2/musicbrainz-data-1.2.jar">JAR Builds</a>)<br>- [javamusicbrainz](http://javamusicbrainz.sourceforge.net/) |                                                                                                    |
| [JAVE](http://www.sauronsoftware.it/projects/jave/) | Java Audio Video Encoder                                     |                                                                                                                                                                 |                                                                                                    |

## Runtime exec et Threads

- <http://alwin.developpez.com/tutorial/JavaThread/>
- Interruptions:
  <http://java.developpez.com/faq/java/?page=langage_threads>
- Interruptions:
  <http://thecodersbreakfast.net/index.php?post/2009/06/08/G%C3%A9rer-proprement-les-interruptions-de-threads-en-Java>
- <http://ydisanto.developpez.com/tutoriels/java/runtime-exec/>
- From Runtime.exec() to ProcessBuilder :
  <http://www.java-tips.org/java-se-tips/java.util/from-runtime.exec-to-processbuilder.html>
- Passing a parameter to a thread:
  <http://stackoverflow.com/questions/877096/how-can-i-pass-a-parameter-to-a-java-thread>

## Misc

### Swing

|  |  |  |
|----|----|----|
| Component | Description | Lien |
| JList | Get selected item(s) | <http://www.exampledepot.com/egs/javax.swing/list_ListGetSel.html> |
|  | Double click | <http://www.developpez.net/forums/d539105/java/interfaces-graphiques-java/awt-swing/composants/listes/jlist-double-clique-element/#> |
|  | How to add a checkbox to items in a JList | <http://helpdesk.objects.com.au/java/how-do-add-a-checkbox-to-items-in-a-jlist> |
| JTable | Hide/Show columns | <http://www.stephenkelvin.de/XTableColumnModel/> |
|  | Choose the color of a JTable cell | <http://www.javaworld.com/article/2077430/core-java/set-the-jtable.html> |
|  | How to change color of JTable row having a particular value | <http://www.java-forums.org/awt-swing/541-how-change-color-jtable-row-having-particular-value.html> |
|  | Horizontal scrollbar | <http://stackoverflow.com/questions/2452694/jtable-horizontal-scrollbar-in-java> <http://stackoverflow.com/questions/3857807/java-swing-problems-with-horizontal-scroll-for-a-jtable-embedded-in-a-jscrolled> |
|  | How to Insert Image into JTable Cell | <http://stackoverflow.com/questions/4941372/how-to-insert-image-into-jtable-cell> |
|  | JButton in a JTable cell | <http://www.theinsanetechie.in/2013/08/java-jbutton-in-jtable-cell.html> |
|  | Click event | <http://stackoverflow.com/questions/7350893/click-event-on-jtable-java> |
| ImageIcon | Creating border around ImageIcon on a JLabel, not around the Jlabel | <http://stackoverflow.com/questions/7350893/click-event-on-jtable-java> |

### Graphic

|  |  |
|----|----|
| Description | Lien |
| Reading an Image from a File, InputStream, or URL | <http://www.exampledepot.com/egs/javax.imageio/BasicImageRead.html> |
| Saving a Generated Graphic to a PNG or JPEG File | <http://www.exampledepot.com/egs/javax.imageio/Graphic2File.html> |

### String

|  |  |
|----|----|
| Description | Lien |
| Left-padding integers | <http://stackoverflow.com/questions/473282/left-padding-integers-with-zeros-in-java> |
| Date format | <http://30minparjour.la-bnbox.fr/post/2010/petit-point-sur-simpledateformat> |
| Regex | <http://benhur.teluq.uqam.ca/SPIP/inf6460/article.php3?id_article=29&id_rubrique=7&sem=5> |

### Convert

| Description          | Lien                                                                                             |
|----------------------|--------------------------------------------------------------------------------------------------|
| Blob to String       | [http://shitmores.blogspot.fr/2007/06/convert-javasqlblob-to-string.html](http://shitmores.blogspot.fr/2007/06/convert-javasqlblob-to-string.html) |
| Inter > String       | ```String.valueOf(myInt);```                                                                     |
| String > Integer     | ```Integer.parseInt(myString);```                                                                |

## En vrac (pour l'instant)

- Tableaux associatifs:
  <http://www.chicoree.fr/w/Programmation_imp%C3%A9rative/Tableaux_associatifs>
- <http://download.oracle.com/javase/tutorial/index.html>
- Overriding .equals():
  - <http://stevenharman.net/blog/archive/2006/04/27/HowTo_Override_equals_and_hashCode_Part1.aspx>
  - <http://java.developpez.com/faq/java/?page=divers#DIVERS_equals>
- OnExit Event:
  <http://stackoverflow.com/questions/2467070/onexit-event-for-a-swing-application>
- Collections:
  <http://fmora.developpez.com/tutoriel/java/collections/introduction/>
- Overriding equals():
  <http://stackoverflow.com/questions/27581/overriding-equals-and-hashcode-in-java>
- Look&Feel (a tester):
  <http://docs.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html>
- JavaDoc:
  <http://www.siteduzero.com/tutoriel-3-35079-presentation-de-la-javadoc.html>
- mime: <http://www.rgagnon.com/javadetails/java-0487.html>
- Cloner des objets:
  <http://ydisanto.developpez.com/tutoriels/java/cloneable/>
- Get User Name: <http://www.rgagnon.com/javadetails/java-0048.html>
- Group a List by property:
  <http://vladzloteanu.wordpress.com/2009/05/20/java-lists-group-by-element-property-as-ruby-group_by-method/>
- Random numbers:
  <http://www.cs.geneseo.edu/~baldwin/reference/random.html>
- How to split a path platform independent?:
  <http://stackoverflow.com/questions/1099859/how-to-split-a-path-platform-independent>
- Maven behind proxy:
  - Maven does not use Netbean's nor system configured proxy
  - You have to modify Maven's settings.xml configuration file as
    described here: <http://wiki.netbeans.org/FaqMavenProxySettings>
  - On Windows, the file is located under C:\Program Files\NetBeans
    7.0.1\java\maven\conf

## Maven (A TESTER)

- <http://dcabasson.developpez.com/articles/java/maven/introduction-maven2/>
- <http://chrisdail.com/2008/04/17/building-with-maven/>

## JAR Version

A étudier plus sérieusement

- <http://stackoverflow.com/questions/1237084/netbeans-manifest>
- <http://docs.oracle.com/javase/7/docs/technotes/guides/versioning/spec/versioning2.html>
- <http://www.rgagnon.com/javadetails/java-0388.html>

## Include librairies in JAR

- Maven: in pom.xml, add the following lines in `<plugins>`
  ([Source](http://maven.40175.n5.nabble.com/How-can-I-include-pom-xml-dependencies-in-output-jar-td88102.html)):

```xml
<plugin>
  <artifactId>maven-assembly-plugin</artifactId>
  <configuration>
    <descriptorRefs>
    <descriptorRef>jar-with-dependencies</descriptorRef>
    </descriptorRefs>
  </configuration>
  <executions>
    <execution>
      <id>make-assembly</id>
      <phase>package</phase>
      <goals>
        <goal>attached</goal>
      </goals>
    </execution>
  </executions>
</plugin>
```

- Ant: in build.xml, add the following lines
  ([Source](http://dchikhaoui.janua.fr/post/2012/09/07/How-to-include-external-libraries-in-the-final-Jar-with-Netbeans)):
  - The result will be an independent jar named finalApp.jar which
    includes, in this example, log4j library.
  - "Main-Class" attribute should be set to what you have in Project
    Properties, under Run/Main Class:
  - Note: "-post-jar" insures that this package build is made at the
    end, so expected files are present in dist folder

```xml
<target name="-post-jar">
  <jar jarfile="dist/finalApp.jar">
    <zipfileset src="${dist.jar}" excludes="META-INF/*" />
    <zipfileset src="dist/lib/log4j-1.2.16.jar" excludes="META-INF/*" />
    <manifest>
      <attribute name="Main-Class" value="com.example.package.Main"/>
    </manifest>
  </jar>
</target>
```

## Temp: jMusicLib

J'ai un projet en cours [jMusicLib](JMusicLib) dont le nom
n'est pas encore fixé et qui n'est pas encore disponible en ligne. Mais
pour mon propre besoin, je commence à écrire une doc.
