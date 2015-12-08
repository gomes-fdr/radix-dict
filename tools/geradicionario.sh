#!/bin/sh
#
# Script para fazer dump do dicionario do aspell, requer os pacotes
# aspell e aspell-pt_BR.
#
#------------------------------------------------------------------

which aspell >/dev/null 2<&1
if [ $? -eq "0" ]; then
    aspell -d pt_BR dump master >/dev/null 2>&1
    if [ $? -eq "0" ]; then
        aspell -d pt_BR dump master | aspell -l pt_BR expand > dicionario.txt
	echo "Arquivo dicionario-pt_BR.txt gerado com sucesso."
    else
	echo "O pacote de dicionário do aspell para pt_BR não está instalado."
    fi
else
    echo "Pacote aspell nao foi encontrado."
fi
