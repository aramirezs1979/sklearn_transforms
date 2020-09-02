from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class CustomImputer():
    def __init__(self, icols, tcol):
        self.icols = icols
        self.tcol = tcol
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        from sklearn.impute import SimpleImputer
        import pandas as pd
        si = SimpleImputer(
           missing_values=np.nan,  # los valores que faltan son del tipo ``np.nan`` (Pandas estándar)
           strategy='median',  # la estrategia elegida es cambiar el valor faltante por la mediana
          verbose=0,
         copy=True
        )
        ds= X[self.icols]
        si.fit(ds)
        return pd.concat([pd.DataFrame.from_records(
               data=si.transform(ds),  # el resultado SimpleImputer.transform (<< pandas dataframe >>)
               columns=self.icols), df2[self.tcol]], axis=1 )
