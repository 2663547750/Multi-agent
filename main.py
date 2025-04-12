# -*- coding:utf-8 -*-
from loop import judge, need_to_model, FEM_model_infer, MD_DFT_model_infer,run_matlab_comsol

def main():
    suffix = "hello"
    need_input = "左基板温度为310 K，右基板温度为308 K；左基板接触角为22度，右基板接触角为18度；表面张力设定为0.28 N/m。左基板密度为4500 kg/m³，右基板密度为550 kg/m³；左基板恒压热容为480 J/(kg·K)，右基板恒压热容为650 J/(kg·K)。左基板导热系数为180 W/(m·K)，右基板导热系数为50 W/(m·K)。左基板材料为Al2O3，右基板材料为SiO2；液滴名称为H2O，液滴密度为5200 kg/m³，动力黏度为0.18 Pa·s。仿真网格细度固定为4级。"
    
    model_input = need_to_model(need_input)

    flag = judge(model_input)

    while not flag:
        # 准备走 MD，DFT 流程, 直到回到 FEM 流程
        model_input = MD_DFT_model_infer(model_input, suffix)
        flag = judge(model_input)
    
    # 走 FEM 流程
    FEM_model_infer(model_input, suffix)

    # 跑通FEM
    reuslt_path = run_matlab_comsol(suffix)
    

if __name__ == "__main__":
    main()