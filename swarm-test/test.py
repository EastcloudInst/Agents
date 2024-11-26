from datetime import datetime, timedelta

# 当前日期和时间
current_datetime = datetime(2024, 11, 25, 8, 0, 0)

# 偏移量：1.5天（1天 + 12小时）
offset = timedelta(days=1.5)

# 计算偏移后的日期和时间
new_datetime = current_datetime + offset

print("当前时间是：", current_datetime)
print("偏移后的时间是：", new_datetime)

print(type(current_datetime))
