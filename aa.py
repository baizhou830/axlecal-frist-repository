#!/usr/bin/env python3
"""
文件整理工具
自动整理文件夹中的文件，按类型分类
"""

import os
import shutil
from datetime import datetime

# 文件类型分类字典
FILE_CATEGORIES = {
    # 图片
    '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    
    # 文档
    '文档': ['.pdf', '.doc', '.docx', '.txt', '.md', '.ppt', '.pptx', '.xls', '.xlsx'],
    
    # 视频
    '视频': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
    
    # 音频
    '音频': ['.mp3', '.wav', '.flac', '.aac'],
    
    # 压缩包
    '压缩包': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    
    # 程序代码
    '代码': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css'],
    
    # 其他
    '其他': []  #匹配不到的文件 
    #因为作者实在没有能力覆盖到全部的文件类型 
    #于是只能将不常用的文件类型全部划到其他类别
    #在自定义类型时，您可以删除掉除 其他 外的类型，这不会导致错误
}
#如果你想要增加一个自定义类型，
#请在这个字典内添加类型以及相匹配的扩展名

def welcome():
    """显示信息"""
    print("=" * 50)
    print("        文件整理工具")
    print("=" * 50)
    print("自动按类型整理文件")
    print("可对图片、文档、视频、音频、压缩包、代码进行整理")
    print("=" * 50)
    #此函数用于输出此工具的基本信息
def get_folder_path():
    """获取用户要整理的文件夹"""
    print("\n请输入要整理的文件夹路径")
    while True:
        path = input("路径: ").strip()
        
        #在此处将相对路径转换为绝对路径
        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), path)
        
        # 检查路径是否存在
        if os.path.exists(path):
            return path
            #如果路径存在，那么就返回并停止循环
        else:
            print(f"路径不存在：{path}")
            print("请重新输入有效路径，或按 Ctrl+C 退出")

def organize_files(folder_path):
    """整理文件夹中的文件"""
    
    print(f"\n 开始整理文件夹：{folder_path}")
    
    # 统计信息
    stats = {category: 0 for category in FILE_CATEGORIES}
    stats['总计'] = 0
    
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        #不处理文件夹
        if os.path.isdir(file_path):
            continue
        
        #获取文件扩展名
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  #转为小写，防止出现大小写不同的问题
        
        #找到文件分类
        file_category = '其他'  # 默认分类为其他
        
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                file_category = category
                break
        
        # 创建分类文件夹（如果不存在）
        category_folder = os.path.join(folder_path, file_category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            print(f" 创建文件夹：{file_category}")
        
        # 移动文件到分类文件夹
        try:
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f"  文件 {filename} → {file_category}")
            stats[file_category] += 1
            stats['总计'] += 1
        except Exception as e:
            print(f"   移动失败：{filename} - {e}")
    
    return stats

def show_report(stats, folder_path):
    """显示整理报告"""
    print("\n" + "=" * 50)
    print("                整理报告")
    print("=" * 50)
    
    print(f"整理所用时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"目标文件夹：{folder_path}")
    print("-" * 50)
    
    # 显示各分类数量
    for category, count in stats.items():
        if category != '总计' and count > 0:
            print(f"{category:8s}：{count:3d} 个文件")
    
    print("-" * 50)
    print(f" 总计整理：{stats['总计']} 个文件")
    print("=" * 50)

def main():
    """主函数"""
    try:
        # 显示信息
        welcome()
        
        # 获取要整理的文件夹
        folder_path = get_folder_path()
        
        # 开始整理
        stats = organize_files(folder_path)
        
        # 显示报告
        show_report(stats, folder_path)
        
        # 结束
        print("\n 整理完成。文件已按类型分类。")
        print(" 你可以在每个分类文件夹中找到整理后的文件")
        
    except KeyboardInterrupt:
        print("\n\n用户中断，程序退出")
    except Exception as e:
        print(f"发生错误：{e}")
        print("请检查路径是否正确，或文件是否被占用")

#执行时直接执行主函数
if __name__ == "__main__":
    main()
