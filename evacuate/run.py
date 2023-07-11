import os
import subprocess
import pandas as pd

# 待办事项列表
todo_list = []

while True:
    # 显示菜单选项
    print("1. 添加待办事项")
    print("2. 显示待办事项")
    print("3. 退出")

    # 获取用户选择
    choice = input("请选择操作：")

    if choice == "1":
        # 添加待办事项
        todo = input("请输入待办事项：")
        todo_list.append(todo)
        print("已添加待办事项：", todo)
    elif choice == "2":
        # 显示待办事项
        print("待办事项列表：")
        for idx, todo in enumerate(todo_list, start=1):
            print(f"{idx}. {todo}")
    elif choice == "3":
        # 退出程序
        print("谢谢使用，再见！")
        break
    else:
        print("无效的选择，请重新输入。")