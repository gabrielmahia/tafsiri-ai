import streamlit as st
import urllib.request, json

st.set_page_config(page_title="Tafsiri AI", page_icon="🌍", layout="centered")
st.markdown("""<style>
.stApp{background:#0a0a14;color:#e8eaf6}
.t-card{background:#0d0d2b;border:1px solid #1a1a4e;border-radius:10px;padding:14px 18px;margin:8px 0}
.stButton>button{background:#4527a0;color:#fff;border:none;border-radius:8px;padding:10px 24px;font-weight:700;width:100%}
textarea{background:#0d0d2b!important;color:#e8eaf6!important}
</style>""", unsafe_allow_html=True)

API_KEY = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY","")

LANG_NAMES = {
    "sw":"Kiswahili","en":"English","ki":"Kikuyu",
    "luo":"Dholuo","kam":"Kamba","so":"Somali"
}
DOMAINS = {
    "Kawaida (General)":"",
    "Fedha (Financial/M-PESA)":"financial domain — M-PESA, banking, loans, SACCOs",
    "Afya (Health)":"medical and health domain — symptoms, medicines, hospitals",
    "Elimu (Education)":"education domain — KCSE, school subjects, exams",
    "Serikali (Government)":"Kenya government and civic domain — county, national, devolution",
    "Kilimo (Agriculture)":"agricultural domain — crops, livestock, weather",
}

def translate(text, src, tgt, domain_hint):
    if not API_KEY: return "❌ API key not configured."
    src_name = LANG_NAMES.get(src, src)
    tgt_name = LANG_NAMES.get(tgt, tgt)
    domain_str = f" This is {domain_hint} context." if domain_hint else ""
    prompt = f"Translate the following text from {src_name} to {tgt_name}.{domain_str} Preserve meaning exactly. Return only the translation, nothing else.\n\n{text}"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    body = {"contents":[{"role":"user","parts":[{"text":prompt}]}],
            "generationConfig":{"temperature":0.1,"maxOutputTokens":1000}}
    try:
        req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                     headers={"Content-Type":"application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e: return f"❌ {e}"

st.markdown("# 🌍 Tafsiri AI")
st.markdown("**Tafsiri kati ya lugha za Kenya**")

col1, col2 = st.columns(2)
with col1: src = st.selectbox("Kutoka (From)", list(LANG_NAMES.keys()),
                                format_func=lambda k: LANG_NAMES[k], key="src")
with col2: tgt = st.selectbox("Kwenda (To)", [k for k in LANG_NAMES if k != src],
                               format_func=lambda k: LANG_NAMES[k], key="tgt")

domain = st.selectbox("Muktadha (Domain)", list(DOMAINS.keys()))
text_in = st.text_area("Andika maandishi ya kutafsiriwa:", height=150,
                        placeholder="Weka maandishi hapa...")

c1, c2 = st.columns(2)
with c1:
    if st.button("🌍 Tafsiri", key="trans_btn") and text_in.strip():
        with st.spinner("Ninatafsiri..."):
            result = translate(text_in, src, tgt, DOMAINS[domain])
            st.session_state["translation"] = result
with c2:
    if st.button("🔄 Hakiki (Back-translate)", key="back_btn"):
        if "translation" in st.session_state:
            with st.spinner("Ninahakiki..."):
                back = translate(st.session_state["translation"], tgt, src, DOMAINS[domain])
                st.session_state["back_translation"] = back

if "translation" in st.session_state:
    st.markdown("### Tafsiri:")
    st.markdown(f'<div class="t-card">{st.session_state["translation"]}</div>', unsafe_allow_html=True)
if "back_translation" in st.session_state:
    st.markdown("### Hakiki (Back-translation):")
    st.markdown(f'<div class="t-card" style="border-color:#4527a0">{st.session_state["back_translation"]}</div>',
                unsafe_allow_html=True)

st.markdown("---")
st.caption("🌍 Tafsiri AI v1.0 | Lugha za Kenya | CC BY-NC-ND 4.0 | gabrielmahia.ai")
