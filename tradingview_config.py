from tradingview_ta import Interval

# TradingView analiz ayarları
TRADINGVIEW_SETTINGS = {
    'screener': 'turkey',
    'exchange': 'BIST',
    'interval': Interval.INTERVAL_1_DAY
}

# Kullanılabilir diğer interval seçenekleri
AVAILABLE_INTERVALS = {
    '1_MINUTE': Interval.INTERVAL_1_MINUTE,
    '5_MINUTES': Interval.INTERVAL_5_MINUTES,
    '15_MINUTES': Interval.INTERVAL_15_MINUTES,
    '30_MINUTES': Interval.INTERVAL_30_MINUTES,
    '1_HOUR': Interval.INTERVAL_1_HOUR,
    '2_HOURS': Interval.INTERVAL_2_HOURS,
    '4_HOURS': Interval.INTERVAL_4_HOURS,
    '1_DAY': Interval.INTERVAL_1_DAY,
    '1_WEEK': Interval.INTERVAL_1_WEEK,
    '1_MONTH': Interval.INTERVAL_1_MONTH
} 