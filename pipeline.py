from src.extract import extract
from src.transform import transform
from src.load import load

df = extract()
df = transform(df)
df = load(df)

