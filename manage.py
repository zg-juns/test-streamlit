import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlitデモ')
st.write('Display Image')

left_column, right_column = st.columns(2)
btn = left_column.button('右カラムに文字を表示')
if btn:
  right_column.write('右カラム')

# アコーディオン
st.write('▼ アコーディオン ▼')
expander = st.expander('問い合わせ')
expander.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

# プログレスバー
# st.write('▼ プログレスバー ▼')
# 'プログレスバーの表示'
# 'Start!'
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# 'Done!'


# ==========

st.write('▼ チェックボタン ▼')
# チェックボタン
if st.checkbox('Show Image'):
  img = Image.open('imc.png')
  # use_column_width：レイアウトの横幅に合わせて表示
  st.image(img, caption = 'IMC', use_column_width = True)

st.write('▼ セレクトボックス ▼')
# セレクトボックス
option = st.selectbox(
  '好きな数字は？',
  list(range(1, 11))
)
'好きな数字は', option, 'です'

st.write('▼ テキストボックス ▼')
# テキストボックス
text = st.text_input('趣味は？')
'趣味は：', text

st.write('▼ スライダー ▼')
# スライダー(最小値, 最大値, 初期値)
condition = st.slider('調子は？', 0, 100, 50)
'コンディション：' , condition

# ==============================

# use_column_width：レイアウトの横幅に合わせて表示
st.image(img, caption = 'IMC', use_column_width = True)

df = pd.DataFrame({
  '1列目': [1, 2, 3, 4],
  '2列目': [10, 20, 30, 40],
})
# st.write(df)

# 表の幅と高さを指定できる
# st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)
# これはスタティックなテーブル
# st.table(df.style.highlight_max(axis=0))

# マジックコマンド
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


# 折れ線グラフ
st.write('▼ 折れ線グラフ ▼')
df2 = pd.DataFrame(
  np.random.rand(20, 3),
  columns=['a', 'b', 'c']
)
# df2
st.line_chart(df2)
st.write('▼ エリアチャート ▼')
st.area_chart(df2)

# マップのプロット
st.write('▼ マップのプロット ▼')
df3 = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon']
)
# df3
st.map(df3)

# 画像を表示
st.write('▼ マップのプロット ▼')