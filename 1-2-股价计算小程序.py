name="铮羽宇宙无敌大公司"
stock_price=666.66789
stock_code="0702"
stock_price_daily_growth_factor=1.2
growth_days=2
print(f"公司：{name}，股票代码：{stock_code}，当前股价{stock_price}")
print("每日增长系数是：%.2f，经过%d天的增长后，股价达到了：%9.8f"%(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))