# Xuanji Tu – Generador de poemas combinatorios (English ahead)

![Xuanji Tu Screenshot](https://github.com/mmoroca/xuanji-tu-generator/blob/main/xuanji-tu-screenshot.png "Xuanji Tu Screenshot")

## Español 🇪🇸

### 📜 Descripción

Este proyecto es un **generador de poemas aleatorios** basado en el **Xuanji Tu (璇玑图)**, una célebre obra de poesía combinatoria china del siglo IV atribuida a **Su Hui**.  
El Xuanji Tu consiste en una matriz de caracteres que puede leerse en múltiples direcciones, generando miles de poemas válidos.

El script permite:
- Extraer un poema válido de forma aleatoria.
- Mostrarlo en **caracteres chinos (hanzi)**, **pinyin** o **ambos**.
- Elegir pinyin **con o sin tonos**.
- Obtener una **traducción automática al español** (opcional).
- Controlar todo mediante **parámetros por línea de comandos**.

Este proyecto está pensado para **experimentación literaria, análisis fonético, usos artísticos y educativos**.

---

### ⚙️ Requisitos

- Python **3.8 o superior**
- Dependencias:

```bash
pip install pypinyin
pip install googletrans==4.0.0-rc1
```

> ⚠️ Nota: `googletrans` **no es una API oficial de Google**. Se usa únicamente con fines experimentales.

---

### 📂 Estructura del proyecto

```
xuanji-tu/
├── xuanji_tu.txt        # Texto del Xuanji Tu en formato matricial
├── xuanji_tu-3.py       # Script principal
└── README.md            # Este archivo
```

---

### ▶️ Uso básico

```bash
python xuanji_tu-3.py
```

Salida por defecto:
- Poema en caracteres chinos
- Pinyin sin tonos

---

### 🧩 Opciones por línea de comandos

#### Selección de salida

- `--hanzi` → solo caracteres chinos
- `--pinyin` → solo pinyin
- `--both` → hanzi + pinyin
- `--translation-only` → solo traducción

#### Pinyin

- `--tone` → pinyin con tonos (números)
- (sin `--tone`) → pinyin sin tonos

#### Traducción

- `--translate googletrans` → traducción automática al español

#### Longitud del poema

- `--min-len N` → longitud mínima
- `--max-len N` → longitud máxima

---

### 📌 Ejemplos

Poema con hanzi y pinyin:
```bash
python xuanji_tu-3.py --both
```

Poema con pinyin y tonos:
```bash
python xuanji_tu-3.py --pinyin --tone
```

Poema con traducción automática:
```bash
python xuanji_tu-3.py --both --translate googletrans
```

Solo traducción:
```bash
python xuanji_tu-3.py --translate googletrans --translation-only
```

---

### ⚠️ Nota sobre la traducción

- La traducción automática se basa en **chino moderno**, no chino clásico.
- El resultado es **orientativo**, no filológicamente exacto.
- El script indica explícitamente cuando una traducción es automática.

---

### 📜 Licencia

Proyecto de uso libre con fines educativos y artísticos.

---

## English 🇬🇧

### 📜 Description

This project is a **random poem generator** based on the **Xuanji Tu (璇玑图)**, a famous piece of Chinese combinatorial poetry from the 4th century, attributed to **Su Hui**.  
The Xuanji Tu is a square matrix of characters that can be read in multiple directions, producing thousands of valid poems.

The script allows you to:
- Extract a random valid poem.
- Display it in **Chinese characters (hanzi)**, **pinyin**, or **both**.
- Choose pinyin **with or without tones**.
- Obtain an **automatic Spanish translation** (optional).
- Control everything via **command-line arguments**.

This project is intended for **literary experimentation, phonetic analysis, artistic, and educational uses**.

---

### ⚙️ Requirements

- Python **3.8 or higher**
- Dependencies:

```bash
pip install pypinyin
pip install googletrans==4.0.0-rc1
```

> ⚠️ Note: `googletrans` is **not an official Google API** and is used here for experimental purposes only.

---

### 📂 Project structure

```
xuanji-tu/
├── xuanji_tu.txt        # Xuanji Tu matrix text
├── xuanji_tu-3.py       # Main script
└── README.md            # This file
```

---

### ▶️ Basic usage

```bash
python xuanji_tu-3.py
```

Default output:
- Poem in Chinese characters
- Pinyin without tones

---

### 🧩 Command-line options

#### Output selection

- `--hanzi` → Chinese characters only
- `--pinyin` → pinyin only
- `--both` → hanzi + pinyin
- `--translation-only` → translation only

#### Pinyin

- `--tone` → pinyin with tone numbers
- (without `--tone`) → pinyin without tones

#### Translation

- `--translate googletrans` → automatic Spanish translation

#### Poem length

- `--min-len N` → minimum length
- `--max-len N` → maximum length

---

### 📌 Examples

Hanzi + pinyin:
```bash
python xuanji_tu-3.py --both
```

Pinyin with tones:
```bash
python xuanji_tu-3.py --pinyin --tone
```

Poem with automatic translation:
```bash
python xuanji_tu-3.py --both --translate googletrans
```

Translation only:
```bash
python xuanji_tu-3.py --translate googletrans --translation-only
```

---

### ⚠️ Translation disclaimer

- Automatic translation is based on **modern Chinese**, not Classical Chinese.
- Results are **approximate**, not academically exact.
- The script clearly labels automatic translations.

---

### 📜 License

Free to use for educational and artistic purposes.

