from pydantic import BaseModel, Field
from typing import List

class BaseInfoModel(BaseModel):
    etf_name: str
        
class _InfoVitals(BaseModel):
    issuer: str 
    issuer_link: str 
    brand: str 
    brand_link: str 
    structure: str 
    structure_link: str 
    expense_ratio: str 
    hompage_link: str 
    inception: str 
    index_tracked: str 
    index_tracked_link: str 
    
class _DBTheme(BaseModel):
    category: str
    category_link: str
    asset_class:  str
    asset_class_link:  str
    asset_class_size:  str
    asset_class_size_link: str
    asset_class_style: str
    asset_class_style_link: str
    general_region: str
    general_region_link: str
    specific_region: str
    specific_region_link: str
    
class _FactSet(BaseModel):
    segment: str
    category: str
    focus: str
    niche: str
    strategy: str
    weighting_scheme: str

class _TradeData(BaseModel): 
    open: str
    volume: str
    day_low: str
    day_high: str
    _52_week_low: Field(..., alias="52_week_low")
    _52_week_high: Field(..., alias="52_week_high")
    aum: str
    shares: str
    
class _HistoricalTradeData(BaseModel): 
    _1_month_avg_volume: Field(..., alias="1_month_avg_volume")
    _3_month_avg_volume: Field(..., alias="3_month_avg_volume")

class _AlternativeETFs(BaseModel): 
    type: str
    ticker: str
    expense_ratio: str
    assets: str
    avg_daily_volume: str
    ytd_return: str
    
class _OtherAlternativeETFs(_AlternativeETFs): 
    pass

class InfoModel(BaseModel):
    vitals: _InfoVitals
    dbtheme: _DBTheme
    fact_set: _FactSet
    analyst_report: str
    trade_data: _TradeData
    historical_trade_data: _HistoricalTradeData
    alternative_etfs: List[_AlternativeETFs]
    other_alternative_etfs: List[_OtherAlternativeETFs]