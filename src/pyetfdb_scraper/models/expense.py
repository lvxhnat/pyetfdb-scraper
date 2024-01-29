from pydantic import BaseModel
from typing import List

class _TaxAnalysis(BaseModel):
    max_short_term_capital_gains_rate: List[str]
    max_long_term_capital_gains_rate: List[str]
    tax_on_distributions: List[str]
    distributes_k1: List[str]
    
class ExpenseModel(BaseModel): 
    tax_analysis: _TaxAnalysis
    expense_ratio_analysis: List[str]
    