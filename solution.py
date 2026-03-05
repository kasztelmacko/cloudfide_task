import pandas as pd
import re

VALID_COLUMN_LABEL_PATTERN = r'[a-zA-Z_]+'

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """Return a copy of df with a new column computed from role.
    Role may use existing column labels, basic math operators and spaces."""
    if not _is_valid_label(new_column):
        return pd.DataFrame()

    used_columns = re.findall(VALID_COLUMN_LABEL_PATTERN, role)
    
    for col in used_columns:
        if not _is_valid_label(col) or col not in df.columns:
            return pd.DataFrame()

    try:
        result_df = df.copy()
        result_df[new_column] = df.eval(role)
        return result_df
    except Exception:
        return pd.DataFrame()

def _is_valid_label(label: str) -> bool:
    """Validates that column labels contain only letters and underscores."""
    return bool(re.fullmatch(VALID_COLUMN_LABEL_PATTERN, label))