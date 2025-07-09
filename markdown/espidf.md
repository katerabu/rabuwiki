# Instalace:
sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
python --version # mel by byt vyssi nez 2.7.17
# Get ESP-IDF
mkdir -p ~/esp
cd ~/esp
git clone --recursive https://github.com/espressif/esp-idf.git
# Set up the Tools
cd ~/esp/esp-idf
./install.sh all
# set up the Environment Variables - do not forget DOT and SPACE!
. $HOME/esp/esp-idf/export.sh
# add to $HOME/.bashrc
alias get_idf='. $HOME/esp/esp-idf/export.sh'
# test installation = start the project:
cd ~/esp
cp -r $IDF_PATH/examples/get-started/hello_world .
cd ~/esp/hello_world
idf.py set-target esp32
idf.py menuconfig
idf.py build flash monitor
#########################################š

🔌 Zjištění sériového portu:
$ sudo dmesg | grep tty
# často pro USB-Serial převodníky (např. CH340, CP210x)
ls /dev/ttyUSB*
ls /dev/ttyACM*
# Sleduj připojení v reálném čase
watch -n 0.5 ls /dev/ttyUSB* /dev/ttyACM*

🔍 Zjištění čipu a flash info pomocí esptool.py:
(automaticky se nainstaluje s ESP-IDF)
esptool.py --port /dev/ttyUSB0 chip_id             # Zobrazí ID čipu
esptool.py --port /dev/ttyUSB0 flash_id            # Info o flash paměti
esptool.py --port /dev/ttyUSB0 read_mac            # Získá MAC adresu
esptool.py --port /dev/ttyUSB0 read_flash_status   # Stav flash paměti

✅ Základní příkazy idf.py:
Příkaz	Popis
create-project nazev
set-target <chip>	Nastaví cílový čip (např. esp32, esp32s3, esp8266, apod.).
menuconfig	Spustí konfigurátor (textové UI pro nastavení projektu).
build	Přeloží (buildne) projekt.
clean	Smaže výstupy překladu.
fullclean	Vyčistí i konfigurační soubory – reset projektu do výchozího stavu.
flash	Nahraje binárku do zařízení přes sériový port.
monitor	Otevře sériový terminál pro sledování výstupu z ESP.
flash monitor	Zkombinované nahrání firmware a následné otevření sériového monitoru.
erase-flash	Vymaže celý flash čip na zařízení.
reconfigure	Znovu vygeneruje build systém (užitečné např. po změně SDK).
size	Ukáže velikost výsledné binárky.
size-components	Ukáže velikost jednotlivých komponent.

⚙️ Automatické rozpoznání portu (idf.py od ESP-IDF v4.2+):
idf.py flash monitor
➡ Pokud je zařízení jediné připojené, IDF si port zjistí samo.
Pokud je víc zařízení, použij -p, např. -p /dev/ttyUSB0 nebo -p COM3.

🛠️ Příklad použití:
idf.py create-project hello_world
cd ~/esp/hello_world
idf.py set-target esp32
idf.py menuconfig
idf.py build
idf.py flash
idf.py -p /dev/ttyUSB0 flash monitor

cd ~/esp/projekt && idf.py set-target esp32 && idf.py build && idf.py -p /dev/ttyACM0 flash monitor

idf.py set-target esp32
idf.py menuconfig  # Nastavení Wi-Fi a MQTT parametrů
idf.py build       # Kompilace
idf.py flash       # Nahrání na zařízení
idf.py monitor     # Sledování výstupu

Přejdi na aktualni verzi ESP-IDF, aktualizuj ESP-IDF takto:
cd ~/esp
git clone -b v5.2 https://github.com/espressif/esp-idf.git esp-idf
cd esp-idf
./install.sh
. ./export.sh
