#!/bin/bash


if [ "$1" = "delete" ]; then
  if [ -f lista_zakupow.txt ]; then
    echo -e "\n Usuwamy twoją listę zakupów"
    rm lista_zakupow.txt
  else
    echo -e "\n \n Jeszcze nie stworzyłeś swojej listy zakupów! Zacznij od dodania produktu: ./lista.sh <produkt>"
  fi
elif [ "$1" = "send" ]; then
  if [ -f lista_zakupow.txt ]; then
    if [[ "$2" == *"@"* ]]; then
      mail -s "Twoja lista zakupów już tu jest!" -r "$2" -A lista_zakupow.txt  "$2" < lista_zakupow.txt
      echo -e "\n \n Twoja lista zakupów została wysłana na mail: $2 \n"
    else
      echo -e "\n \n Jesteś pewny, że to poprawny mail? Spróbuj jeszcze raz"
    fi
  else
    echo -e "\n \n Jeszcze nie stworzyłeś swojej listy zakupów! Zacznij od dodania produktu: ./lista.sh <produkt>"
  fi
elif [ -z "$1" ]; then
  echo -e  "\n Tworzenie listy zakupów. Użycie:\n \n	Jeśli chcemy dodać coś na listę: ./lista.sh  <produkt1> <produkt2> ... \n	Jeśli chcemy wyświetlić swoją listę: ./lista.sh show \n	Jeśli chcemy usunąć listę: ./lista.sh delete"
  echo -e "	Jeśli chcemy wysłać listę na maila: ./lista.sh send <adres e-mail>"
elif [ "$1" = "show" ]; then
  if [ -f lista_zakupow.txt ]; then
    echo -e "\n Oto twoja lista zakupów: \n"
    cat lista_zakupow.txt
  else
    echo -e "\n \n Jeszcze nie stworzyłeś swojej listy zakupów! Zacznij od dodania produktu: ./lista.sh <produkt>"
  fi
else
 touch lista_zakupow.txt
 licznik=`cat lista_zakupow.txt | wc -l`
  for parametr in "$@"
  do
      if [ `grep -o "$parametr" lista_zakupow.txt` ]; then
         echo -e "\n Masz już $parametr na liście"
      else
         licznik=$[licznik + 1]
         echo -e "\n Dodano $parametr do listy!"
         echo "$licznik: $parametr" >> lista_zakupow.txt
      fi
  done
fi
echo -e " \n "