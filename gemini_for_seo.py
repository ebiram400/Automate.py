import pandas as pd
import google.generativeai as genai
import json

df = pd.read_csv('produce-2.csv')
df['Product_Description'] = ""
df['Short_Description'] = ""
df['SEO_Keywords'] = ""
df['Tags'] = ""

for i in range(6,913,1) :
    print("generate for",df.loc[i]['Name'],"...")
    genai.configure(api_key="AIzaSyDVnPkl4zaVSMKOiyCPz0GZh5lYSd1u4fo")
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "برای محصول "+df.loc[i]['Name']+' اطلاعات زیر را تولید کن:  1. **توضیحات محصول**: یک پاراگراف شامل 5 جمله خاص و مرتبط با محصول که برای سئو بهینه باشد.  2. **توضیح مختصر**: 1-2 جمله کوتاه و مفید درباره محصول.  3. **کلمات کلیدی مرتبط**: حداقل 5 کلمه یا عبارت خاص محصول برای سئو.  4. **برچسب‌ها (در صورت نیاز)**: اگر محصول مشابه دیگری در دسته مرتبط وجود دارد، برچسب مناسب ایجاد کن. در غیر این صورت، خالی بگذار.**فرمت خروجی**:[[توضیحات محصول با 5 جمله],[توضیح مختصر در 1-2 جمله],[{"keyword":"کلمه کلیدی","score":امتیاز}, ...],[برچسب‌ها (در صورت نیاز)]] شما موظفید فقط و فقط فرمت خروجی را مطابق دستور زیر تولید کنید. هر گونه انحراف از فرمت مورد قبول نیست. حتی اگر نتیجه‌ای وجود نداشته باشد، قالب باید دقیقاً حفظ شود و تمام اجزا (مانند لیست‌ها یا کلیدهای JSON) به‌طور کامل وجود داشته باشند. اگر نتیجه‌ای وجود ندارد، مقدارها را به صورت خالی (مثلاً لیست خالی یا مقادیر null) تولید کنید. هیچ توضیح، متن اضافی، یا پیامی خارج از این فرمت نباید تولید شود.توجه داشته باشید که حتی در صورت خطا یا نبود نتیجه، فرمت را تغییر ندهید.هیچ متن اضافی یا توضیحی در خروجی مجاز نیست. فقط و فقط JSON مورد نظر باید تولید شود.'
    response = model.generate_content(prompt)
    print("has given response...")
    res = response.text
    res = res.split('\n', 1)[1]
    res = res.replace('```', '')
    res = res.strip()
    content = json.loads(res)
    
    # اختصاص مقادیر به ستون‌های جدید
    df.loc[i, 'Product_Description'] = content[0][0] if len(content[0]) > 0 else ""
    df.loc[i, 'Short_Description'] = content[1][0] if len(content[1]) > 0 else ""
    df.loc[i, 'SEO_Keywords'] = ", ".join([item["keyword"] for item in content[2]]) if len(content[2]) > 0 else ""
    df.loc[i, 'Tags'] = ", ".join(content[3]) if len(content[3]) > 0 else ""
    
    df.to_excel('product.xlsx', index=False )

