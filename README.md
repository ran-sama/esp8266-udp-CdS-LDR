# esp8266-udp-CdS-LDR
Use the internal ADC of the esp8266 to read light intensity from a Cadmium sulfide sensor.

tl;dr: Get rrdtool and python bindings, create a round robin DB yourself
```
sudo apt install rrdtool
sudo apt install python-rrd
rrdtool create ldr_data.rrd --step 60 DS:light:GAUGE:600:0:320 RRA:MAX:0.5:1:1080
```
![alt text](https://raw.githubusercontent.com/ran-sama/udp_CdS_ldr_v2/master/light.png)
![alt text](https://raw.githubusercontent.com/ran-sama/udp_CdS_ldr_v2/master/wiring.png)

## License
Licensed under the WTFPL license.
