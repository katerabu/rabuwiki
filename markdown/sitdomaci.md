## 🏠 Domácí síť – firewall, segmentace, DNS ochrana

Domácí síť je často nejzranitelnějším místem v zabezpečení IT prostředí, zejména pokud je připojena k internetu a obsahuje více zařízení. Správné nastavení firewallu, segmentace sítě a DNS ochrana výrazně zvyšují bezpečnost.

---

### 🔥 Firewall v domácí síti

- **Co je firewall?**  
  Firewall je zařízení nebo software, které kontroluje příchozí a odchozí síťový provoz podle bezpečnostních pravidel (Carlson, 2022).  
- **Typy firewallů:**  
  - **Hardwarový firewall:** Vestavěný do routeru nebo samostatné zařízení.  
  - **Softwarový firewall:** Na jednotlivých zařízeních (např. Windows Defender Firewall).  
- **Doporučení:**  
  - Aktivuj firewall v routeru i na všech koncových zařízeních.  
  - Pravidelně aktualizuj firmware routeru pro opravy bezpečnostních chyb.  
  - Blokuj nepotřebné porty a služby (např. UPnP, Telnet).  

---

### 🌐 Segmentace domácí sítě

- **Co je segmentace?**  
  Rozdělení sítě na menší izolované části, které spolu mají omezenou komunikaci (NIST, 2023).  
- **Výhody:**  
  - Omezení šíření malware a útoků mezi zařízeními.  
  - Zvýšení kontroly a sledovatelnosti provozu.  
- **Praktická implementace:**  
  - Vytvoř samostatnou VLAN nebo Wi-Fi síť pro IoT zařízení (chytré žárovky, kamery apod.).  
  - Pro rodinné počítače a telefony použij jinou VLAN nebo SSID s odlišným heslem.  
  - Routery s podporou více SSID a VLAN toto umožňují (např. Ubiquiti, MikroTik, Asus).  

---

### 🛡️ DNS ochrana

- **Úloha DNS:**  
  DNS (Domain Name System) převádí domény na IP adresy, klíčová služba pro přístup na internet.  
- **Rizika:**  
  - Útoky typu DNS spoofing nebo cache poisoning mohou směrovat na škodlivé stránky.  
- **Ochrana DNS:**  
  - Používej zabezpečené DNS služby s podporou DNS-over-HTTPS (DoH) nebo DNS-over-TLS (DoT).  
  - Doporučené veřejné DNS servery:  
    - Cloudflare (1.1.1.1) – DoH/DoT podpora  
    - Google DNS (8.8.8.8)  
    - Quad9 (9.9.9.9) – filtrování škodlivých domén  
  - Konfiguruj router i zařízení na použití těchto DNS serverů.  
  - Některé routery a zařízení umožňují nastavit rodičovskou kontrolu nebo blokování škodlivých domén (např. OpenDNS).

---

### 🛠️ Praktické tipy a konfigurace

- Aktualizace firmware routeru: Pravidelně kontroluj a instaluj bezpečnostní aktualizace.  
- Změna výchozího hesla routeru: Použij silné a unikátní heslo.  
- Zakázání vzdálené správy (Remote Management): Zabraňuje přístupu k routeru z internetu.  
- Povolení WPA3 nebo WPA2 šifrování pro Wi-Fi: WPA3 je novější a bezpečnější (v závislosti na podpoře zařízení).  
- Vytvoření guest Wi-Fi sítě: Oddělená síť pro návštěvy bez přístupu k hlavní domácí síti.  
- Použití zařízení s podporou firewallu s pokročilými funkcemi: Například blokování útoků typu DoS, filtrování paketů.  

---

### 📊 ASCII diagram domácí sítě s segmentací a DNS ochranou

             [Internet]
                 |
            [Modem/ISP]
                 |
             [Router]
          /            \
     [VLAN1]          [VLAN2]
  (PC, notebook)  (IoT zařízení)
      |                |
  [Firewall]       [Firewall]
      |                |
  [Switch/Wi-Fi]   [Switch/Wi-Fi]
  
 DNS ochrana: Router používá DNS-over-HTTPS (DoH) s Cloudflare 1.1.1.1

---

### 📚 Citace (Harvard)

- Carlson, M. (2022). *Network Firewalls Explained*. Cybersecurity Journal, 15(3), pp. 45-53.  
- NIST (2023). *Guide to Network Segmentation*. NIST Special Publication 800-125B. [online] Available at: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-125b.pdf [Accessed 2025].  
- Cloudflare (2024). *What is DNS over HTTPS (DoH)?* [online] Available at: https://developers.cloudflare.com/1.1.1.1/dns-over-https/ [Accessed 2025].  

---

### 🔗 Doporučené zdroje a návody

- [Router security best practices – CISA](https://www.cisa.gov/news-events/news/securing-your-home-router)  
- [NIST Guide to Network Segmentation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-125b.pdf)  
- [Cloudflare 1.1.1.1 DNS](https://1.1.1.1/)  
- [OpenDNS FamilyShield](https://www.opendns.com/setupguide/) – rodičovská kontrola a blokování malwaru  
- [Ubiquiti UniFi VLAN Setup Guide](https://help.ui.com/hc/en-us/articles/204909754-UniFi-How-to-Create-a-VLAN)  

---

Správné nastavení domácí sítě je základem bezpečné práce z domova i ochrany všech připojených zařízení. Segmentace a DNS ochrana pomáhají minimalizovat dopad potenciálních útoků a zvyšují kontrolu nad síťovým provozem.
