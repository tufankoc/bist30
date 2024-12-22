# Teknik analiz yardımcı fonksiyonları
from tradingview_ta import TA_Handler
from tradingview_config import TRADINGVIEW_SETTINGS

def get_technical_analysis(symbol):
    """Bir hisse için teknik analiz verilerini çeker"""
    try:
        analysis = TA_Handler(
            symbol=symbol,
            screener=TRADINGVIEW_SETTINGS['screener'],
            exchange=TRADINGVIEW_SETTINGS['exchange'],
            interval=TRADINGVIEW_SETTINGS['interval']
        )
        
        return analysis.get_analysis()
    except Exception as e:
        print(f"Hata oluştu ({symbol}): {str(e)}")
        return None 