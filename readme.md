# nameless python script to archive a gemini capsule
TODO write a proper readme

## usage
    pip install -r requirements.txt
    python "gemini://example.com" "~/archive/example.com/"

first argument is url to capsule without trailing slash. second argument is the folder where it'll be stored.

## motivation
i saw a notice about a capsule closing and i wanted to copy it before it went offline. i emailed the owner and they said they're ok with it.

## output format
given the url `gemini://yretek.com/articulos/index.gmi`, it'll output a `gemini___yretek.com_articulos_index.gmi` file with the following headers:

     1   │ Date: 2023-01-22 07:30
     2   │ URL: gemini://yretek.com/articulos/index.gmi
     3   │ Client status: 2
     4   │ Server status: 20
     5   │ Certificate: b7b63cefcc6c6779b9e336b2d06dad41
     6   |
     7   |
     8   |  < file contents >

the output has some metadata at the top (resembling http headers) followed by "\r\n\r\n" and the content. i'm sure there's some sort of format readily available for archives but i couldn't be bothered to implement anything.

## currently archived
i'll upload to archive.org at some point.

### 2023-january-22
- gemini://yretek.com
- gemini://text.eapl.mx
- gemini://sl1200.dystopic.world
- gemini://texto-plano.xyz
- gemini://gemini.astropirados.space
- gemini://gemini.elbinario.net
- gemini://reisub.nsupdate.info
- gemini://c3po.aljadra.xyz
- gemini://compudanzas.net
- gemini://alex.corcoles.net
- gemini://bucareli.online
- gemini://sitio.bitsandlinux.com
- gemini://gemlog.gamifi.cat
- gemini://hispagatos.org
- gemini://ivanruvalcaba.cf
- gemini://gem.juancastro.xyz
- gemini://srlobo.gorritodeplata.xyz
- gemini://michan.noho.st
- gemini://gemini.kosmonautik.net
- gemini://gemini.solobsd.org
- gemini://jorgesanz.net
- gemini://michan.es
- gemini://frankenwolke.com
- gemini://gmi.osiux.com
- gemini://archipielago.uno
- gemini://aves.archipielago.uno
- gemini://azul.archipielago.uno
- gemini://caogena.archipielago.uno
- gemini://diez.archipielago.uno
- gemini://hache.archipielago.uno
- gemini://lind.archipielago.uno
- gemini://ness.archipielago.uno
- gemini://sejo.archipielago.uno
- gemini://tralfanum.archipielago.uno
- gemini://wiki.archipielago.uno
- gemini://aperalesf.flounder.online
- gemini://bogart.flounder.online
- gemini://deivisdiaz.flounder.online
- gemini://latte.flounder.online
- gemini://maxxcan.flounder.online
- gemini://milos.flounder.online
- gemini://monmac.flounder.online
- gemini://moribundo.flounder.online
- gemini://my32.flounder.online
- gemini://pandora.flounder.online
- gemini://soyricky.flounder.online
- gemini://xrasl.flounder.online
