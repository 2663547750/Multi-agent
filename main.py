from loop import judge, need_to_model, FEM_model_infer, MD_DFT_model_infer
from metric import evaluate

def main():
    suffix = "1"
    need_input = input("Enter your need: ")
    
    model_input = need_to_model(need_input)

    flag = judge(model_input)

    while not flag:
        # 准备走 MD，DFT 流程, 直到回到 FEM 流程
        model_input = MD_DFT_model_infer(model_input, suffix)
        flag = judge(model_input)
    
    # 走 FEM 流程
    m_file_path = FEM_model_infer(model_input, suffix)

    # 评估
    evaluate(m_file_path)

if __name__ == "__main__":
    main()