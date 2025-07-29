## 📤 Šifrovaná komunikace a IM (Signal, Threema, Matrix)

Bezpečná a šifrovaná komunikace je základem ochrany soukromí a integrity dat při přenosu zpráv. Instant messaging (IM) aplikace s end-to-end šifrováním chrání obsah zpráv před odposlechem, modifikací i neoprávněným přístupem.

---

### 🔐 Význam end-to-end šifrování (E2EE)

End-to-end šifrování znamená, že zpráva je zašifrována na zařízení odesílatele a dešifrována až na zařízení příjemce. Ani poskytovatel služby nemůže obsah zpráv číst.

Výhody:  
- Zajišťuje důvěrnost komunikace.  
- Brání odposlechu ze strany třetích osob, včetně poskytovatele internetu nebo služeb.  
- Minimalizuje riziko zásahu do obsahu zpráv.

---

### 💬 Populární šifrované IM aplikace

| Aplikace | Platformy        | Protokol/Technologie                  | Klíčové vlastnosti                                  |
|----------|------------------|-------------------------------------|----------------------------------------------------|
| **Signal**  | Android, iOS, Desktop | Signal Protocol (open source)       | Silné E2EE, open source, nezávislá, ochrana metadat, volání a zprávy |
| **Threema** | Android, iOS      | Threema-proprietary protocol        | Anonymita uživatele, E2EE, minimalizace dat, bez nutnosti telefonu |
| **Matrix**  | Android, iOS, Desktop | Matrix protocol + Olm/Megolm E2EE   | Decentralizovaná síť, interoperabilita, otevřený standard |
| **Wire**    | Android, iOS, Desktop | Proteus Protocol (E2EE)              | Podniková bezpečnost, víceuživatelské chaty, šifrované hovory |
| **Session** | Android, iOS, Desktop | Loki Network (decentralizované)     | Anonymní chat bez telefonního čísla, odolné vůči sledování |

---

### 🛠️ Praktické návody k nasazení a používání

#### Signal - rychlý start

1. Stáhni a nainstaluj aplikaci Signal (https://signal.org/).  
2. Registrovat se pomocí telefonního čísla.  
3. Ověř identitu kontaktů pomocí bezpečnostních kódů v profilu kontaktu.  
4. Aktivuj **samodestrukční zprávy**: Otevři chat → klikni na jméno kontaktu → Nastavení → Samodestrukční zprávy → nastav čas.  
5. Nastav uzamčení aplikace PINem v Nastavení → Soukromí → Zámek aplikace.

#### Threema - anonymita a bezpečí

1. Stáhni aplikaci Threema (https://threema.ch/en).  
2. Vytvoř si Threema ID, bez nutnosti telefonu.  
3. Využij QR kódy pro ověření kontaktů.  
4. Aktivuj šifrované zálohy v Nastavení → Záloha a obnova.  
5. Používej PIN kód pro zabezpečení aplikace.

#### Matrix (Element klient) - decentralizované řešení

1. Stáhni Element (https://element.io/).  
2. Zaregistruj se na veřejném homeserveru nebo zprovozni vlastní.  
3. Přidej kontakty nebo vstup do místností.  
4. Aktivuj E2EE v nastavení místnosti.  
5. Pravidelně aktualizuj klienta a homeserver.

---

### 📊 ASCII diagram – Základní princip end-to-end šifrování

```
Odesílatel                          Příjemce
   │                                   │
   │  Zašifruje zprávu pomocí          │
   │  veřejného klíče příjemce         │
   │───────────────►                   │
   │                                   │
   │             Přijme zprávu        │
   │             a dešifruje pomocí   │
   │             svého soukromého klíče│
   │                                   │
   │          Obsah je chráněný       │
```

---

### 🔒 Další tipy pro bezpečnou komunikaci

- Nepoužívej „přihlášení přes Google/Facebook“ kvůli zbytečnému sdílení dat.  
- Neposílej citlivé informace přes nešifrované kanály.  
- Vyhýbej se ukládání dlouhodobých chatů s citlivými daty bez šifrované zálohy.  
- Aktivuj dvoufaktorové ověřování u účtů, kde je to možné.  
- Buď obezřetný při přijímání souborů a odkazů i od známých osob.

---

### 🔗 Užitečné odkazy

- [Signal – Oficiální stránky](https://signal.org/)  
- [Threema – Oficiální stránky](https://threema.ch/en)  
- [Matrix.org – Decentralizovaná komunikace](https://matrix.org/)  
- [Element – Matrix klient](https://element.io/)  
- [Electronic Frontier Foundation – Secure Messaging Scorecard](https://www.eff.org/pages/secure-messaging-scorecard)  

---

### 📚 Citace (Harvard)

- Marlinspike, M. and Perrin, T. (2016). *The Signal Protocol*. Open Whisper Systems.  
- Threema GmbH (2023). *Threema Security Whitepaper*.  
- Matrix.org Foundation (2023). *Matrix Specification and Protocol*.  
- Electronic Frontier Foundation (2023). *Secure Messaging Scorecard*.

## 🔐 Detailní konfigurace VPN + Signal pro maximální bezpečnost komunikace

Použití šifrované IM aplikace Signal v kombinaci s VPN zvyšuje ochranu soukromí, zabraňuje sledování datového provozu a skryje skutečnou IP adresu uživatele.

---

### 1. Proč používat VPN společně se Signalem?

- **Skrytí IP adresy:** Signal sám IP adresu ukazuje kontaktům (pokud to povolíš), VPN ji maskuje a zabraňuje sledování vaší skutečné polohy.  
- **Ochrana proti dohledovým a cenzurním opatřením:** VPN umožňuje obcházet blokace a šifruje veškerý internetový provoz mimo Signal.  
- **Zabezpečení na veřejných Wi-Fi:** VPN zabrání odposlechu a MITM útokům na veřejných sítích, kde se často Signal používá.

---

### 2. Výběr vhodné VPN služby

- Preferuj VPN služby s **no-log politikou**, silným šifrováním a rychlým připojením (např. WireGuard nebo OpenVPN).  
- Doporučené služby: [Mullvad](https://mullvad.net), [ProtonVPN](https://protonvpn.com), [NordVPN](https://nordvpn.com).  
- Vyhni se bezplatným VPN, často prodávají data nebo mají slabé zabezpečení.

---

### 3. Instalace a konfigurace VPN

#### a) WireGuard (doporučený moderní protokol)

1. Stáhni a nainstaluj WireGuard klienta na zařízení:  
   - [WireGuard pro Android](https://play.google.com/store/apps/details?id=com.wireguard.android)  
   - [WireGuard pro iOS](https://apps.apple.com/app/wireguard/id1441195209)  
   - [WireGuard pro Windows/macOS/Linux](https://www.wireguard.com/install/)

2. Zaregistruj se u VPN poskytovatele, který nabízí WireGuard konfigurace.

3. Importuj konfigurační soubor (.conf) do WireGuard klienta.

4. Aktivuj připojení VPN.

#### b) OpenVPN (alternativa)

1. Stáhni OpenVPN klienta (např. [OpenVPN Connect](https://openvpn.net/client-connect-vpn-for-windows/)).  
2. Importuj ověřený profil od VPN poskytovatele.  
3. Připoj se k VPN serveru dle potřeby.

---

### 4. Nastavení Signal pro práci s VPN

- Ve **Nastavení → Soukromí → IP adresa** můžeš zakázat „Ukázat mé IP kontaktům“, aby se při používání VPN neukazovala skutečná IP.  
- Aktivuj **Uzamčení aplikace PINem** pro další ochranu.  
- Zapni **samodestrukční zprávy** u citlivých konverzací.

---

### 5. Doporučený workflow při používání VPN + Signal

```
[Internet] ←→ [VPN Server] ←→ [Signal Server] ←→ [Kontakt]
```

VPN šifruje veškerý provoz, včetně signálu Signal, takže poskytovatel internetu ani žádná třetí strana nevidí, co přesně posíláš.

---

### 6. Další bezpečnostní tipy

- **Pravidelně aktualizuj** jak VPN klienta, tak Signal aplikaci.  
- Pokud používáš veřejné Wi-Fi, vždy nejdříve aktivuj VPN před spuštěním Signal.  
- Neukládej záložní klíče Signal mimo bezpečné místo (např. bezpečný password manager).  
- Pro maximální anonymitu zvaž používat VPN s **multi-hop** funkcí (např. Mullvad, ProtonVPN).

---

### 7. Diagram znázorňující VPN + Signal komunikaci
https://github.com/katerabu/rabuwiki/tree/main/markdown
```
+-----------+       +------------+       +--------------+       +---------+
|  Uživatel | <---> | VPN Server | <---> | Signal Server| <---> | Kontakt |
+-----------+       +------------+       +--------------+       +---------+
     │                    │                    │                    │
     │  Šifrovaný tunel    │                    │                    │
     │────────────────────>│                    │                    │
     │                    │  Zašifrovaná zpráva │                    │
     │                    │────────────────────>│                    │
     │                    │                    │  E2EE komunikace     │
     │                    │                    │────────────────────>│
```

---

### 8. Užitečné odkazy

- [Signal Official Site](https://signal.org/)  
- [WireGuard VPN](https://www.wireguard.com/)  
- [Mullvad VPN](https://mullvad.net/en/)  
- [ProtonVPN](https://protonvpn.com/)  
- [NordVPN](https://nordvpn.com/)  
- [Signal Safety Tips](https://signal.org/blog/safety-numbers/)

---

### 📚 Citace (Harvard)

- Marlinspike, M. and Perrin, T. (2016). *The Signal Protocol*. Open Whisper Systems.  
- WireGuard (2023). *WireGuard: A fast, modern VPN protocol*. [online] Available at: https://www.wireguard.com/ [Accessed 2025].  
- Mullvad VPN (2023). *Privacy and security*. [online] Available at: https://mullvad.net/en/ [Accessed 2025].

