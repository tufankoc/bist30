import argparse
from tradingview import analyze_bist30
from tradingview_config import AVAILABLE_INTERVALS, TRADINGVIEW_SETTINGS

def parse_arguments():
    """Komut satırı argümanlarını işler"""
    parser = argparse.ArgumentParser(description='BIST-30 Teknik Analiz Programı')
    
    parser.add_argument('--interval', 
                       choices=list(AVAILABLE_INTERVALS.keys()),
                       default='1_DAY',
                       help='Analiz aralığı (varsayılan: 1_DAY)')
    
    parser.add_argument('--rsi-limit',
                       type=float,
                       default=30,
                       help='RSI alt limiti (varsayılan: 30)')
    
    parser.add_argument('--quiet',
                       action='store_true',
                       help='Sadece özet raporu göster')
    
    return parser.parse_args()

def main():
    """Ana program"""
    # Argümanları al
    args = parse_arguments()
    
    # Interval değerini güncelle
    TRADINGVIEW_SETTINGS['interval'] = AVAILABLE_INTERVALS[args.interval]
    
    print("\nBIST-30 Teknik Analiz Programı")
    print("="*30)
    print(f"Analiz Aralığı: {args.interval}")
    print(f"RSI Limit: {args.rsi_limit}")
    print("="*30 + "\n")
    
    try:
        # Analizleri çalıştır
        df = analyze_bist30(quiet=args.quiet)
        
        # RSI limitini güncelle ve raporu yazdır
        from report_generator import print_summary_report
        print_summary_report(df, rsi_limit=args.rsi_limit)
        
    except KeyboardInterrupt:
        print("\nProgram kullanıcı tarafından sonlandırıldı.")
    except Exception as e:
        print(f"\nBir hata oluştu: {str(e)}")
    
if __name__ == "__main__":
    main() 