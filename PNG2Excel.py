# encoding=gbk
import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res

def png2xlsx(image_paths, output_folder='./output'):
    """
    将图片转换为Excel表格
    
    :param image_paths: 图片文件路径列表
    :param output_folder: 输出文件夹路径
    """
    table_engine = PPStructure(show_log=True)
    
    # 确保输出目录存在
    os.makedirs(output_folder, exist_ok=True)

    for image_path in image_paths:
        # 检查文件是否存在
        if not os.path.exists(image_path):
            print(f"文件 {image_path} 不存在")
            continue
            
        img = cv2.imread(image_path)
        if img is None:
            print(f"读取图片 {image_path} 失败")
            continue
            
        result = table_engine(img)
        save_structure_res(result, output_folder, os.path.basename(image_path).split('.')[0])
        print(f"图片 {image_path} 处理完成")


if __name__ == "__main__":
    # 示例用法
    images = ["ap105_1.png"]  # 替换为你的图片路径
    png2xlsx(images, "./output_excel")