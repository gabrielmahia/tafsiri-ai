# 🌍 Tafsiri AI — Kenya Language Translation

> *Tafsiri* (Swahili) = translation, interpretation

AI-powered translation bridging Kenya's language divide: Swahili ↔ English, with support for Kikuyu, Dholuo, Kamba, and Luo. Built for civic documents, financial communications, health information, and everyday use.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tafsiriai.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## The Problem

Kenya has 42+ ethnic groups and 3 official communication languages, yet most digital services exist only in English. A farmer in Kisii, a patient at a rural clinic, a voter reading a ballot — all face the same barrier: critical information locked behind a language they don't fully command. Unlike Google Translate, Tafsiri AI understands Kenyan context: M-PESA terms, KCSE subjects, county government vocabulary, and local idioms that general translators mangle.

## Languages Supported

| Language | Code | Direction | Notes |
|----------|------|-----------|-------|
| Kiswahili | sw | ↔ English | Full support |
| Kikuyu | ki | ↔ sw/en | Civic + financial |
| Dholuo | luo | ↔ sw/en | Civic + financial |
| Kamba | kam | ↔ sw/en | Civic + financial |
| Somali | so | ↔ sw/en | Northern Kenya |

## Features

| Feature | Description |
|---------|-------------|
| 📝 Text Translation | Real-time translation with domain awareness |
| 📄 Document Mode | Upload PDF or paste document text |
| 🎯 Domain Context | Civic, financial, health, education modes |
| 💬 Back-translation | Verify accuracy via back-translation |
| 📋 Glossary | Kenya-specific term glossary |

## Quickstart

```bash
git clone https://github.com/gabrielmahia/tafsiri-ai
pip install -r requirements.txt
streamlit run app.py
```

## Part of the East Africa Civic Tech Portfolio

Foundational tool supporting: [DarajaAI](https://github.com/gabrielmahia/daraja-ai) | [ShuleAI](https://github.com/gabrielmahia/shule-ai) | [Hati AI](https://github.com/gabrielmahia/hati-ai)

---

*gabrielmahia.github.io | MIT License*
