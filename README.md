# Cyclops

**Türkçe** | [English](#cyclops-1)

---

## Türkçe

**Cyclops** - Gözlerinizle bilgisayarınızı kontrol edin!

[![Son Sürümü İndir](https://img.shields.io/github/v/release/mehmetaltunel/EyeMouse?label=Son%20Sürümü%20İndir&style=for-the-badge&color=blue)](https://github.com/mehmetaltunel/EyeMouse/releases/latest)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Mac%20|%20Linux-green.svg)

### Ne İşe Yarar?
- **Göz takibi ile fare kontrolü**: Kafanızı hareket ettirerek imleci kontrol edin
- **Göz kırpma ile tıklama**: Sol göz = sol tık, sağ göz = sağ tık
- **Kalibrasyon sistemi**: Kişiselleştirilmiş hassas kontrol

### İndir ve Çalıştır (Kurulumsuz)

**Windows (.exe) veya macOS (.dmg) indirmek için:**
1. [Releases](https://github.com/mehmetaltunel/EyeMouse/releases/latest) sayfasına gidin.
2. İşletim sisteminize uygun dosyayı indirin (`Cyclops_Windows.exe` veya `Cyclops_macOS.dmg`).
3. Çift tıklayıp çalıştırın. Hepsi bu kadar!

### Geliştirici Kurulumu (Python)
Eğer kodları değiştirmek isterseniz:
```bash
git clone https://github.com/mehmetaltunel/EyeMouse.git
cd EyeMouse
pip install -r requirements.txt
python run.py
```

---

## 🛠️ Sorun Giderme / Troubleshooting

### Windows
**Uygulama açılmadan kapanıyorsa:**
1. Klasörde `hata_logu.txt` dosyası oluşmuş mu bakın.
2. `Microsoft Visual C++ Redistributable` yüklü olduğundan emin olun.
3. Yönetici olarak çalıştırmayı deneyin.

### macOS
**"Dosya hasarlı" veya "Açılamıyor" hatası alırsanız:**
Apple güvenliği bazen internetten indirilen uygulamaları engeller. Terminal'i açıp şu komutu uygulayın:

```bash
xattr -cr /Applications/Cyclops.app
# Veya uygulamayı nereye koyduysanız o yolu yazın
```

---

## Cyclops

**Gaze-controlled mouse application** - Control your computer with your eyes!

[![Download Latest](https://img.shields.io/github/v/release/mehmetaltunel/EyeMouse?label=Download%20Latest&style=for-the-badge&color=blue)](https://github.com/mehmetaltunel/EyeMouse/releases/latest)

### Features
- **Gaze control**: Move cursor with head movements
- **Wink to click**: Left wink = Left click, Right wink = Right click
- **Calibration**: Personalized precision control

### Download & Run (No Installation)

**To download Windows (.exe) or macOS (.dmg):**
1. Go to the [Releases](https://github.com/mehmetaltunel/EyeMouse/releases/latest) page.
2. Download the file for your OS (`Cyclops_Windows.exe` or `Cyclops_macOS.dmg`).
3. Double click to run. That's it!

### Developer Setup (Python)
If you want to modify the code:
```bash
git clone https://github.com/mehmetaltunel/EyeMouse.git
cd EyeMouse
pip install -r requirements.txt
python run.py
```
