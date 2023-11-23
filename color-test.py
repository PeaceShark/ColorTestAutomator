from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 配置 Edge WebDriver
edge_service = Service(executable_path='./msedgedriver')
driver = webdriver.Edge(service=edge_service)

# 访问指定的网页
sign_in_url = "https://www.webhek.com/post/color-test/"
driver.get(sign_in_url)

# 等待页面加载完成
time.sleep(3)

# 点击覆盖按钮，进入游戏
cover_button = driver.find_element(By.ID, 'overlay99')
cover_button.click()

# 点击开始游戏按钮
start_button = driver.find_element(By.XPATH, '//*[@id="index"]/div[2]/button')
start_button.click()


def get_unique(styledict):
    """
    从给定的样式字典中找出唯一的样式。
    :param styledict: 字典，包含页面元素及其对应的样式。
    :return: 具有唯一样式的元素。
    """
    # 统计每种样式出现的次数
    cnt_dict = {}
    for style in styledict.values():
        cnt_dict[style] = cnt_dict.get(style, 0) + 1

    # 找到唯一出现的样式
    unique_style = next(
        (style for style, count in cnt_dict.items() if count == 1), "")
    return next((key for key, value in styledict.items() if value == unique_style), None)


try:
    # 获取所有颜色块
    blocks = driver.find_elements(By.XPATH, '//*[@id="box"]/span')
    while blocks:
        # 创建字典，存储元素及其样式
        dict_style = {block: block.get_attribute('style') for block in blocks}

        # 获取具有唯一样式的元素
        unique_tag = get_unique(dict_style)
        if unique_tag:
            # 点击具有唯一样式的元素
            unique_tag.click()

            # 重新获取颜色块以进行下一轮点击
            blocks = driver.find_elements(By.XPATH, '//*[@id="box"]/span')
        else:
            # 如果没有找到唯一的元素，退出循环
            break
except Exception as e:
    # 输出异常信息
    print(f"发生错误: {e}")

# 完成所有操作后暂停
time.sleep(200)

# 关闭浏览器
driver.quit()
