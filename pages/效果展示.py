import streamlit as st
import pandas as pd
import joblib

# 模拟搜索功能
def search(query):
    # 这里应该是与搜索引擎的交互，比如使用Elasticsearch或者其他数据库查询
    # 为了示例，我们使用随机数据
    return pd.DataFrame(
        {'商家名称': ['商家'+str(i) for i in range(1, 11)],
         '地址': ['地址'+str(i) for i in range(1, 11)],
         '评分': [i for i in range(1, 11)]}
    )


# 页面初始设置
st.set_page_config(page_title="效果展示", layout="wide")
st.title("效果展示")

# 侧边栏模型数据选择
file_list = ["1.csv", "2.csv"]
model_list = ["1.pkl", "2.pkl"]
st.sidebar.selectbox(
    "当前目录下需要加载的数据",
    file_list
)
st.sidebar.selectbox(
    "当前目录下需要加载的模型",
    model_list
)
# 搜索框
if "SEARCH_API_KEY" not in st.session_state:
    st.session_state["SEARCH_API_KEY"] = ""
query = st.text_input("请输入搜索词", value=st.session_state["SEARCH_API_KEY"], max_chars=None, key=None, type='default')
# 按钮
searched = st.button("Search")

# 按下按钮后执行操作
if searched:
    # 转变成DataFrame格式
    weight = float(query)
    X = pd.DataFrame([[weight]], columns=["Weight"])
    # results = search(st.session_state["SEARCH_API_KEY"])
    clf = joblib.load('model\clf.pkl')
    # 获取预测值
    prediction = clf.predict(X)[0]
    st.text(prediction)


