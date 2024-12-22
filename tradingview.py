from config import BIST30_SYMBOLS
import pandas as pd
from analysis_utils import get_technical_analysis
from data_processor import create_analysis_data, print_analysis_result
from report_generator import print_summary_report

def analyze_bist30(quiet=False):
    """BIST 30 hisselerini analiz eder"""
    sonuclar = []
    
    for symbol in BIST30_SYMBOLS.keys():
        if not quiet:
            print(f"{symbol} analiz ediliyor...")
        
        analiz = get_technical_analysis(symbol)
        if analiz:
            veri = create_analysis_data(symbol, BIST30_SYMBOLS[symbol], analiz)
            sonuclar.append(veri)
            if not quiet:
                print_analysis_result(veri)
    
    return pd.DataFrame(sonuclar)

if __name__ == "__main__":
    # Önce gerekli kütüphanelerin yüklü olduğundan emin olun:
    # pip install tradingview-ta pandas
    
    df = analyze_bist30()
    print_summary_report(df) 