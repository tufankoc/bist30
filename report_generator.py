# Rapor oluşturma fonksiyonları
def print_summary_report(df, rsi_limit=30):
    """Özet raporu yazdırır"""
    print("\n" + "="*50)
    print("ÖZET RAPOR")
    print("="*50)
    
    print(f"\nAşırı Satım Bölgesindeki Hisseler (RSI < {rsi_limit}):")
    asiri_satim = df[df['RSI'] < rsi_limit][['Sembol', 'Şirket Adı', 'RSI', 'Öneri']]
    if len(asiri_satim) > 0:
        print(asiri_satim.to_string())
    else:
        print("Aşırı satım bölgesinde hisse bulunmuyor.")
    
    print("\nGüçlü Al Önerisi Olan Hisseler:")
    guclu_al = df[df['Öneri'] == 'STRONG_BUY'][['Sembol', 'Şirket Adı', 'RSI', 'Öneri']]
    if len(guclu_al) > 0:
        print(guclu_al.to_string())
    else:
        print("Güçlü al önerisi olan hisse bulunmuyor.") 