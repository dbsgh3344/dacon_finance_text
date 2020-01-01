import pandas as pd

class Cust_pd():
    def __init__(self, var_df_base):
        self.df_base = var_df_base

    def f_keyword_compare(self, var_keyword, var_col_label='smishing', var_col_text='text'):
        print('*'*100)
        print('smishing')
        print(df_base[(df_base[var_col_label]==1) & (df_base[var_col_text].str.contains(var_keyword))][var_col_text])
        print('*'*100)
        print('normal text')
        print(df_base[(df_base[var_col_label]==0) & (df_base[var_col_text].str.contains(var_keyword))][var_col_text])
