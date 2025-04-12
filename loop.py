import const_config as cc
import re
import subprocess
import time

def need_to_model(need_input):
    return need_input

def judge(model_input):
    pattern = re.compile(r'([\u4e00-\u9fff]+?)(?:设定为|为)\s*([0-9.]+)')
    matches = pattern.findall(model_input)

    for key, value in matches:
        if key in cc.attribute:
            # 转换数值为int或float
            num = float(value) if '.' in value else int(value)
            cc.attribute[key] = num

    for key,val in cc.attribute.items():
        if val is None:
            return False
    return True

def FEM_model_infer(model_input, suffix):
    """
    Simulate a FEM model inference process.
    """
    
    model_output = """
model.study.create('std1');
model.study('std1').create('time', 'Transient');
    """
    m_text = cc.matlab_code1 + model_output + cc.matlab_code2
    m_text = m_text.replace("xxxxxxxxxxxx", cc.txt_files_path + "\\" + suffix)


    m_path = cc.m_files_path + "\\" + suffix + ".m"

    with open(m_path, 'w') as f:
        f.write(m_text)
    return m_path

def run_matlab_comsol(suffix):
    core_m_code = cc.m_run_m.replace('xxxxxxxx',suffix)
    m_path = cc.m_files_path

    with open(m_path + "\\core.m", 'w') as f:
        f.write(core_m_code)
    run_matlab_script(m_path, "core")

    # time.sleep(120)
    #return cc.txt_files_path + "\\" + suffix + ".txt"

def MD_DFT_model_infer(model_input, suffix):
    """
    Simulate a MD/DFT model inference process.
    """
    pass

def run_matlab_script(m_path, m_name):
    combined_command = f'cd /d "{m_path}" && matlab -nodesktop -nosplash -r "{m_name}; exit"'
    subprocess.run(combined_command, shell=True, check=True)