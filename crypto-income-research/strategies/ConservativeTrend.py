from freqtrade.strategy import IStrategy
from pandas import DataFrame
import talib.abstract as ta

class ConservativeTrend(IStrategy):
    INTERFACE_VERSION = 3
    timeframe = "1h"
    can_short = False
    startup_candle_count = 220
    minimal_roi = {"0": 0.06, "1440": 0.025, "2880": 0.0}
    stoploss = -0.04
    trailing_stop = True
    trailing_stop_positive = 0.02
    trailing_stop_positive_offset = 0.035
    trailing_only_offset_is_reached = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema50"] = ta.EMA(dataframe, timeperiod=50)
        dataframe["ema200"] = ta.EMA(dataframe, timeperiod=200)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        dataframe["volume_mean"] = dataframe["volume"].rolling(24).mean()
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        conditions = ((dataframe["close"] > dataframe["ema200"]) &
                      (dataframe["ema50"] > dataframe["ema200"]) &
                      (dataframe["rsi"] > 45) & (dataframe["rsi"] < 65) &
                      (dataframe["volume"] > dataframe["volume_mean"]) &
                      (dataframe["volume"] > 0))
        dataframe.loc[conditions, ["enter_long", "enter_tag"]] = (1, "trend_filter")
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[((dataframe["close"] < dataframe["ema50"]) |
                       (dataframe["rsi"] > 75)) &
                      (dataframe["volume"] > 0), "exit_long"] = 1
        return dataframe
