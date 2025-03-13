import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

# 创建示例数据
data = {
    'durations': [5, 6, 6, 2, 4, 7, 3, 8],
    'events': [1, 0, 1, 1, 1, 0, 1, 1]
}
df = pd.DataFrame(data)

# 创建 Kaplan-Meier Fitter 实例
kmf = KaplanMeierFitter()

# 拟合数据



kmf.fit(durations=df['durations'], event_observed=df['events'])

# 绘制生存曲线
kmf.plot_survival_function()

# 显示图形
plt.title('Kaplan-Meier Survival Curve')
plt.xlabel('Time')
plt.ylabel('Survival Probability')

file_name = "KM_Survival_Curve1.png"


    # 保存图像
plt.savefig(file_name, dpi=400)

plt.show()

