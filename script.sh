#!/bin/bash

index=2871

run=true

while $run;
do
  if [ $index -le 6000 ];
  then 
    curl -H "Accept: application/json" -H "Accept-Language: en-US,en" -X GET https://downloads.nordcdn.com/configs/files/ovpn_udp/servers/ca${index}.nordvpn.com.udp.ovpn > ca/ca${index}.udp.ovpn;
    curl -H "Accept: application/json" -H "Accept-Language: en-US,en" -X GET https://downloads.nordcdn.com/configs/files/ovpn_udp/servers/de${index}.nordvpn.com.udp.ovpn > de/de${index}.udp.ovpn;
    curl -H "Accept: application/json" -H "Accept-Language: en-US,en" -X GET https://downloads.nordcdn.com/configs/files/ovpn_udp/servers/dk${index}.nordvpn.com.udp.ovpn > dk/dk${index}.udp.ovpn;
    curl -H "Accept: application/json" -H "Accept-Language: en-US,en" -X GET https://downloads.nordcdn.com/configs/files/ovpn_udp/servers/es${index}.nordvpn.com.udp.ovpn > es/es${index}.udp.ovpn;
    curl -H "Accept: application/json" -H "Accept-Language: en-US,en" -X GET https://downloads.nordcdn.com/configs/files/ovpn_udp/servers/hk${index}.nordvpn.com.udp.ovpn > hk/hk${index}.udp.ovpn;
    curl -H "Accept: application/json" -H "Accept-Language: en-US,en" -X GET https://downloads.nordcdn.com/configs/files/ovpn_udp/servers/il${index}.nordvpn.com.udp.ovpn > il/il${index}.udp.ovpn;
    curl -H "Accept: application/json" -H "Accept-Language: en-US,en" -X GET https://downloads.nordcdn.com/configs/files/ovpn_udp/servers/uk${index}.nordvpn.com.udp.ovpn > uk/uk${index}.udp.ovpn;
    curl -H "Accept: application/json" -H "Accept-Language: en-US,en" -X GET https://downloads.nordcdn.com/configs/files/ovpn_udp/servers/us${index}.nordvpn.com.udp.ovpn > us/us${index}.udp.ovpn;
    index=$(( index + 1 ));
  else
    run=false
  fi
done
