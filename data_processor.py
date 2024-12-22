# Veri işleme fonksiyonları
from datetime import datetime
import pandas as pd

def create_analysis_data(symbol, company_name, analysis):
    """Analiz verilerinden sözlük oluşturur"""
    return {
        'Sembol': symbol,
        'Şirket Adı': company_name,
        'Tarih': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'RSI': analysis.indicators['RSI'],
        'MACD.macd': analysis.indicators['MACD.macd'],
        'MACD.signal': analysis.indicators['MACD.signal'],
        'MA20': analysis.indicators['SMA20'],
        'MA50': analysis.indicators['SMA50'],
        'MA200': analysis.indicators['SMA200'],
        'Öneri': analysis.summary['RECOMMENDATION']
    }

def print_analysis_result(veri):
    """Analiz sonuçlarını ekrana yazdırır"""
    print("\n" + "="*50)
    print(f"Sembol: {veri['Sembol']} ({veri['Şirket Adı']})")
    print(f"RSI: {veri['RSI']:.2f}")
    print(f"MACD: {veri['MACD.macd']:.2f} Sinyal: {veri['MACD.signal']:.2f}")
    print(f"MA20: {veri['MA20']:.2f}")
    print(f"MA50: {veri['MA50']:.2f}")
    print(f"MA200: {veri['MA200']:.2f}")
    print(f"Öneri: {veri['Öneri']}")
    print("="*50) 