BIST30_SYMBOLS = {
    "AKBNK": "AKBANK",
    "ARCLK": "ARÇELİK",
    "ASELS": "ASELSAN",
    "BIMAS": "BİM MAĞAZALAR",
    "EKGYO": "EMLAK KONUT GMYO",
    "EREGL": "EREĞLİ DEMİR ÇELİK",
    "GARAN": "GARANTİ BANKASI",
    "GUBRF": "GÜBRE FABRİKALARI",
    "HEKTS": "HEKTAŞ",
    "ISCTR": "İŞ BANKASI C",
    "KCHOL": "KOÇ HOLDİNG",
    "KOZAA": "KOZA MADENCİLİK",
    "KOZAL": "KOZA ALTIN",
    "KRDMD": "KARDEMİR D",
    "PETKM": "PETKİM",
    "PGSUS": "PEGASUS",
    "SAHOL": "SABANCI HOLDİNG",
    "SASA": "SASA POLYESTER",
    "SISE": "ŞİŞE CAM",
    "TAVHL": "TAV HAVALİMANLARI",
    "TCELL": "TURKCELL",
    "THYAO": "TÜRK HAVA YOLLARI",
    "TOASO": "TOFAŞ OTO FAB.",
    "TSKB": "T.S.K.B.",
    "TUPRS": "TÜPRAŞ",
    "VAKBN": "VAKIFBANK",
    "VESTL": "VESTEL",
    "YKBNK": "YAPI KREDİ BANKASI",
    "YATAS": "YATAŞ",
    "ZOREN": "ZORLU ENERJİ"
}

# TradingView için sembol formatı
def get_tradingview_symbol(symbol):
    return f"BIST:{symbol}" 