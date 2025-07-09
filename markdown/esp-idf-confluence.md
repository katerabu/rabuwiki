h1. 🚀 ESP-IDF – Instalace a základní použití

Návod pro vývoj na ESP32 pomocí oficiálního frameworku Espressif – ESP-IDF.

h2. 🛠️ Instalace závislostí (Linux / Ubuntu / Kubuntu)

{code:bash}
sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
python3 --version  # mělo by být >= 3.7
{code}

h2. 📥 Stažení a instalace ESP-IDF

{code:bash}
mkdir -p ~/esp
cd ~/esp
git clone --recursive https://github.com/espressif/esp-idf.git
cd ~/esp/esp-idf
./install.sh all
{code}

h2. 🧠 Nastavení prostředí

{code:bash}
. $HOME/esp/esp-idf/export.sh
{code}

_Nezapomeň přidat do `~/.bashrc`:_

{code:bash}
alias get_idf='. $HOME/esp/esp-idf/export.sh'
{code}

h2. ✅ Testovací projekt – Hello World

{code:bash}
cd ~/esp
cp -r $IDF_PATH/examples/get-started/hello_world .
cd hello_world
idf.py set-target esp32
idf.py menuconfig
idf.py build
idf.py flash monitor
{code}

h2. 🔌 Zjištění sériového portu

{code:bash}
sudo dmesg | grep tty
ls /dev/ttyUSB*
ls /dev/ttyACM*
watch -n 0.5 ls /dev/ttyUSB* /dev/ttyACM*
{code}

h2. 🔍 Práce s esptool.py

{code:bash}
esptool.py --port /dev/ttyUSB0 chip_id
esptool.py --port /dev/ttyUSB0 flash_id
esptool.py --port /dev/ttyUSB0 read_mac
esptool.py --port /dev/ttyUSB0 read_flash_status
{code}

h2. 🧾 Přehled základních příkazů idf.py

|| Příkaz || Popis ||
| create-project <jméno> | Vytvoří nový projekt |
| set-target <čip>       | Nastaví cílový čip (esp32, esp32s3, ...) |
| menuconfig             | Spustí textové UI pro konfiguraci |
| build                  | Přeloží projekt |
| clean / fullclean      | Smaže výstupy / i konfiguraci |
| flash                  | Nahraje firmware |
| monitor                | Sériový výstup |
| flash monitor          | Kombinace nahrání a spuštění terminálu |
| erase-flash            | Vymaže celý flash čip |
| reconfigure            | Znovu vytvoří build systém |
| size / size-components | Zobrazí velikost výsledné binárky |

h2. ⚙️ Automatické rozpoznání portu

Od ESP-IDF v4.2:

{code:bash}
idf.py flash monitor
{code}

_Pokud je připojeno více zařízení, použij:_

{code:bash}
idf.py -p /dev/ttyUSB0 flash monitor
{code}

h2. 🧪 Ukázka celého průběhu

{code:bash}
idf.py create-project hello_world
cd hello_world
idf.py set-target esp32
idf.py menuconfig
idf.py build
idf.py -p /dev/ttyUSB0 flash monitor
{code}

h2. 🔄 Aktualizace ESP-IDF

{code:bash}
cd ~/esp
git clone -b v5.2 https://github.com/espressif/esp-idf.git esp-idf
cd esp-idf
./install.sh
. ./export.sh
{code}

h2. 📌 Tip

Pro rychlejší vývoj si vytvoř alias:

{code:bash}
alias get_idf='. $HOME/esp/esp-idf/export.sh'
{code}
