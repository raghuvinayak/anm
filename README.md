

                                                      ReadMe

This program is designed in Python environment. For the capturing stream, and then output will be stored in Influxdb directly and monitor in Grafana.
#  Installation:
1. First you need to clone DPMI_Utils from "https://github.com/DPMI/libcap_utils.git" 
2. See Installing for details.
		autoreconf -si
		mkdir build; cd build
		../configure 
		make
		sudo make install

3. Next you need to clone MP smoke from “https://github.com/DPMI/mp.git” 
		autoreconf -si # if from git repo
		./configure [--with-dag=PREFIX] [--with-pcap] [--without-raw]
		make
		make install
		wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana_4.4.3_amd64.deb sudo apt-get install -y adduser libfontconfig sudo dpkg -i grafana_4.4.3_amd64.deb

4. Clone Marcd from “https://github.com/DPMI/marcd.git”
autoreconf --install
1. mkdir build
2. ../configure [--prefix /path/to/prefix]
3. make && make install


5. install Grafana as shown bellow
wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana_4.4.3_amd64.deb 
sudo apt-get install -y adduser libfontconfig 
sudo dpkg -i grafana_4.4.3_amd64.deb




6. install influxdb as shown bellow
		curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
		source /etc/lsb-release
		echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
		sudo apt-get update && sudo apt-get install influxdb

7. install Flask as shown bellow
		sudo pip install Flask

Usage:
This tool is designed for calculating
                1.Bitrates.
These values are plotted in Grafana by grouping technique.
RestApi manual:
we are provided different facilities to analyse stream statistics.
1. Run stream
		curl http://localhost:5000/run/ethvalue_stream1_stream_2 ....
2. Change stream
		curl http://localhost:5000/change/ethvalue_stream1_stream_2 ....
3. Stop stream
		curl http://localhost:5000/stop
4. Show active streams
		curl http://localhost:5000/showstream
5. Add stream
		curl http://localhost:5000/add/ethvalue_stream1_stream_2 ....
6. Delete stream
		curl http://localhost:5000/delete/etvalue_stream1_stream_2 ....


		Run mp(Measuring point) in /home/user/mp/build/ using  ./mp --local -v -i eth0 -s eth1 -o 01::01


		Next run Python api.py in /home/user/consumer-bitrate/

