import pandas as pd
import json

# خواندن فایل خروجی (product.xlsx)
df = pd.read_excel('product.xlsx')

# تعریف ستون‌های جدید برای محتوای جدا شده
df['Product_Description'] = ""
df['Short_Description'] = ""
df['SEO_Keywords'] = ""
df['Tags'] = ""

# پردازش هر ردیف
for i in range(len(df)):
    try:
        res = df.loc[i, 'Description']
        res = res.split('\n', 1)[1]
        res = res.replace('```', '')
        res = res.strip()
        content = json.loads(res)
        
        # اختصاص مقادیر به ستون‌های جدید
        df.loc[i, 'Product_Description'] = content[0][0] if len(content[0]) > 0 else ""
        df.loc[i, 'Short_Description'] = content[1][0] if len(content[1]) > 0 else ""
        df.loc[i, 'SEO_Keywords'] = ", ".join(content[2]) if len(content[2]) > 0 else ""
        df.loc[i, 'Tags'] = ", ".join(content[3]) if len(content[3]) > 0 else ""
    
    except Exception as e:
        print(f"Error processing row {i}: {e}")

# ذخیره فایل جدید
df.to_excel('product_split.xlsx', index=False)
print("Data split completed and saved to 'product_split.xlsx'.")
