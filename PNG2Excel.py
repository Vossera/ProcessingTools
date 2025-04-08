# encoding=gbk
import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res

def png2xlsx(image_paths, output_folder='./output'):
    """
    ��ͼƬת��ΪExcel���
    
    :param image_paths: ͼƬ�ļ�·���б�
    :param output_folder: ����ļ���·��
    """
    table_engine = PPStructure(show_log=True)
    
    # ȷ�����Ŀ¼����
    os.makedirs(output_folder, exist_ok=True)

    for image_path in image_paths:
        # ����ļ��Ƿ����
        if not os.path.exists(image_path):
            print(f"�ļ� {image_path} ������")
            continue
            
        img = cv2.imread(image_path)
        if img is None:
            print(f"��ȡͼƬ {image_path} ʧ��")
            continue
            
        result = table_engine(img)
        save_structure_res(result, output_folder, os.path.basename(image_path).split('.')[0])
        print(f"ͼƬ {image_path} �������")


if __name__ == "__main__":
    # ʾ���÷�
    images = ["ap105_1.png"]  # �滻Ϊ���ͼƬ·��
    png2xlsx(images, "./output_excel")