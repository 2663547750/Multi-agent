import const_config as cc

def need_to_model(need_input):
    pass

def judge(model_input):
    pass

def FEM_model_infer(model_input, suffix):
    """
    Simulate a FEM model inference process.
    """
    
    model_output = """
    model.study.create('std1');
    model.study('std1').create('time', 'Transient');
    """
    m_text = cc.matlab_code1 + model_output + cc.matlab_code2
    m_text = m_text.replace("xxxxxxxxxxxx", cc.txt_files_path + suffix)
    
    m_path = cc.m_files_path + suffix

    with open(cc.m_files_path + suffix, 'w') as f:
        f.write(m_text)
    return m_path

def MD_DFT_model_infer(model_input, suffix):
    """
    Simulate a MD/DFT model inference process.
    """
    pass
