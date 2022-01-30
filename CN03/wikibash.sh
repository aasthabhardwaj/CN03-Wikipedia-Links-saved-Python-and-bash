#!/bin/sh
if [[ -z "$1" ]]; then
  echo "Please enter search keyword"
  read search_key
elif [[ -n "$1" ]]; then
  search_key="$*"
fi

search_key="${search_key// /_}"

echo "...Scanning wikipedia links for the word:  $search_key"

url="https://en.wikipedia.org/wiki/$search_key"

echo "URL FOUND : $url"
destdir=wikiLinks.txt
echo "${url}" >> "$destdir"
