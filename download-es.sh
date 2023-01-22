#!/usr/bin/bash

capsules=(
	"gemini://yretek.com" "yretek.com"
	"gemini://text.eapl.mx" "eapl.mx"
	"gemini://sl1200.dystopic.world" "sl1200"
	"gemini://texto-plano.xyz" "texto-plano.xyz"
	"gemini://gemini.astropirados.space" "resetreboot"
	"gemini://gemini.elbinario.net" "elbinario"
	"gemini://reisub.nsupdate.info" "reisub-hosting-gemini-free-50m"
	"gemini://c3po.aljadra.xyz" "c3po"
	"gemini://compudanzas.net" "compudanzas"
	"gemini://alex.corcoles.net" "alex.corcoles.net"
	#"gemini://costas.dev" "ariel_costas"
	"gemini://bucareli.online" "bucareli"
	"gemini://sitio.bitsandlinux.com" "davidochobits"
	#"gemini://elmau.net" "elmau.net"
	"gemini://gemlog.gamifi.cat" "gamifi.cat"
	"gemini://hispagatos.org" "hispagatos"
	"gemini://ivanruvalcaba.cf" "ivanruvalcaba.cf"
	"gemini://gem.juancastro.xyz" "juancastro.xyz"
	"gemini://srlobo.gorritodeplata.xyz" "srlobo"
	"gemini://michan.noho.st" "roboron-noho.st"
	"gemini://gemini.kosmonautik.net" "kosmonautik"
	"gemini://gemini.solobsd.org" "thedarkmuon"
	"gemini://jorgesanz.net" "jorgesanz.net"
	"gemini://michan.es" "roboron-michan.es"
	"gemini://frankenwolke.com" "frankenwolke.com"
	"gemini://gmi.osiux.com" "osiux"

	"gemini://archipielago.uno" "archipielago.uno"
	"gemini://aves.archipielago.uno" "aves.archipielago.uno"
	"gemini://azul.archipielago.uno" "azul.archipielago.uno"
	"gemini://caogena.archipielago.uno" "caogena.archipielago.uno"
	"gemini://diez.archipielago.uno" "diez.archipielago.uno"
	"gemini://hache.archipielago.uno" "hache.archipielago.uno"
	"gemini://lind.archipielago.uno" "lind.archipielago.uno"
	"gemini://ness.archipielago.uno" "ness.archipielago.uno"
	"gemini://sejo.archipielago.uno" "sejo.archipielago.uno"
	"gemini://tralfanum.archipielago.uno" "tralfanum.archipielago.uno"
	"gemini://wiki.archipielago.uno" "wiki.archipielago.uno"

	"gemini://aperalesf.flounder.online" "aperalesf"
	"gemini://bogart.flounder.online" "bogart.flounder.online"
	"gemini://deivisdiaz.flounder.online" "deivisdiaz.flounder.online"
	"gemini://latte.flounder.online" "latte.flounder.online"
	"gemini://maxxcan.flounder.online" "maxxcan.flounder.online"
	"gemini://milos.flounder.online" "milos.flounder.online"
	"gemini://monmac.flounder.online" "monmac.flounder.online"
	"gemini://moribundo.flounder.online" "archienemigos"
	"gemini://my32.flounder.online" "my32.flounder.online"
	"gemini://pandora.flounder.online" "pandora.flounder.online"
	"gemini://soyricky.flounder.online" "soyricky.flounder.online"
	"gemini://xrasl.flounder.online" "xrasl.flounder.online"
)

target="archive"

for (( i = 0; i < ${#capsules[@]}; i += 2 )); do
	url="${capsules[$i]}"
	name="${capsules[$((i+1))]}"

	folder="${target}/$(date +'%Y-%m-%d')-${name}/"
	if [[ -d "$folder" ]]; then
		echo "$folder already exists, skipping $url..."
		continue
	fi

	mkdir -p "$folder"
	python main.py "$url" "$folder" &
done
