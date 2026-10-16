# 🚢 Titanic Yo'lovchilari Demografiyasi va Omon Qolish Tahlili

Ushbu repozitoriy mashhur **Titanic** kemasi yo'lovchilarining tozalangan va yosh toifalariga ajratilgan ma'lumotlar to'plami (`TITANIC.xlsx`) hamda uning tahliliga bag'ishlangan. Loyiha **Exploratory Data Analysis (EDA)**, statistik tahlil, ma'lumotlarni vizualizatsiya qilish va **Machine Learning (Klassifikatsiya)** modellari uchun mo'ljallangan.

---

## 📁 Ma'lumotlar to'plami haqida qisqacha

* **Fayl nomi:** `TITANIC.xlsx` (Varoq nomi: `Sheet1`)
* **Yo'lovchilar soni (qatorlar):** 891 ta yozuv
* **Ustunlar soni:** 5 ta xususiyat (feature)
* **Bo'sh qiymatlar (Missing Values):** Yo'q (`0` ta — barcha ustunlar to'liq to'ldirilgan va tozalangan)
* **Umumiy omon qolish ko'rsatkichi:** `38.38%` (342 nafar yo'lovchi omon qolgan, 549 nafari halok bo'lgan)

---

## 📋 Ustunlar tavsifi (Data Dictionary)

| Ustun nomi | Ma'lumot turi | Tavsifi | Qiymatlar oralig'i / Namuna |
| :--- | :--- | :--- | :--- |
| `Name` | `string` (`object`) | Yo'lovchining to'liq ismi, familiyasi va unvoni (`Mr.`, `Mrs.`, `Miss.` va b.) | `891` ta unikal ism |
| `Sex` | `string` (`object`) | Yo'lovchining jinsi | `male` (577), `female` (314) |
| `Age` | `int64` | Yo'lovchining yoshi (butun sonlarda) | `0` – `80` yosh (O'rtacha: `29.75`, Mediana: `30.0`, Std: `13.00`) |
| `Survived` | `int64` | **Target (Maqsadli ustun):** Omon qolish holati | `0` = Halok bo'lgan (549), `1` = Omon qolgan (342) |
| `Age_Category` | `string` (`object`) | Yo'lovchining yosh guruhi | `Children`, `Youth&Adults`, `Seniors` |

---

## 📊 Asosiy Statistik Ko'rsatkichlar va Tahlil

### 1. Jins bo'yicha omon qolish ko'rsatkichi (`Sex`)
Kema halokatida *"Ayollar va bolalar birinchi"* qoidasi yaqqol namoyon bo'lgan:

| Jins (`Sex`) | Yo'lovchilar soni | Ulushi (%) | Omon qolganlar | Omon qolish foizi (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Ayollar (`female`)** | 314 | 35.24% | 233 | **74.20%** |
| **Erkaklar (`male`)** | 577 | 64.76% | 109 | **18.89%** |
| **Jami** | **891** | **100%** | **342** | **38.38%** |

### 2. Yosh toifalari bo'yicha tahlil (`Age_Category`)
Yo'lovchilar yoshiga qarab 3 ta asosiy demografik guruhga ajratilgan:

| Yosh toifasi (`Age_Category`) | Yosh oralig'i | O'rtacha yosh | Yo'lovchilar soni | Omon qolganlar | Omon qolish foizi (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Bolalar (`Children`)** | 0 – 14 yosh | 5.82 | 78 | 45 | **57.69%** |
| **Yoshlar va Kattalar (`Youth&Adults`)** | 15 – 64 yosh | 31.53 | 802 | 296 | **36.91%** |
| **Keksalar (`Seniors`)** | 65 – 80 yosh | 69.73 | 11 | 1 | **9.09%** |

---

## 🚀 Loyihani ishga tushirish

### 1. Repozitoriyani klonlash
```bash
git clone [https://github.com/username/titanic-analysis.git](https://github.com/username/titanic-analysis.git)
cd titanic-analysis
